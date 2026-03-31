import os
import datetime
import yfinance as yf
import streamlit as st
from tavily import TavilyClient
from crewai.tools import tool
from crewai import Agent, Task, Crew, Process

try:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
    os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]
except KeyError:
    st.error("API Keys missing! Please add them to Streamlit secrets.")

TODAY = datetime.datetime.now().strftime("%B %d, %Y")
MODEL = "gemini/gemini-3-flash-preview" 

POPULAR_STOCKS = {
    "Reliance Industries": "RELIANCE.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "Tata Consultancy Services (TCS)": "TCS.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "Infosys": "INFY.NS",
    "State Bank of India (SBI)": "SBIN.NS",
    "Bharti Airtel": "BHARTIARTL.NS",
    "ITC Limited": "ITC.NS",
    "Larsen & Toubro (L&T)": "LT.NS",
    "Bajaj Finance": "BAJFINANCE.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "Mahindra & Mahindra": "M&M.NS",
    "Hindustan Unilever": "HINDUNILVR.NS",
    "Axis Bank": "AXISBANK.NS",
    "Zomato": "ZOMATO.NS"
}


def check_daily_limit():
    today_date = datetime.date.today()
    
    if 'last_used_date' not in st.session_state:
        st.session_state['last_used_date'] = today_date
        st.session_state['usage_count'] = 0

    if st.session_state['last_used_date'] != today_date:
        st.session_state['last_used_date'] = today_date
        st.session_state['usage_count'] = 0

    return st.session_state['usage_count'] < 2

tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY", ""))

@tool("web_search_tool")
def web_search_tool(query: str) -> str:
    """Searches for current news. Use if YFinance fails."""
    try:
        search_query = f"{query} stock news {TODAY}"
        response = tavily_client.search(query=search_query, max_results=5)
        return str(response)
    except Exception as e:
        return f"Error fetching news: {str(e)}"

@tool("yfinance_data_tool")
def yfinance_data_tool(ticker: str) -> str:
    """Fetches real-time financial data safely."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="5d")
        if hist.empty:
            raise ValueError("No price history found.")
        
        last_price = round(hist['Close'].iloc[-1], 2)
        info = stock.info
        market_cap = info.get("marketCap", info.get("market_cap", "N/A"))
        
        return (
            f"Ticker: {ticker} (Data as of {TODAY})\n"
            f"Current Price: ₹{last_price}\n"
            f"Market Cap: ₹{market_cap}\n"
        )
    except Exception as e:
        return f"YFinance failed ({str(e)}). CRITICAL: Use web_search_tool for live price."

def run_analysis(ticker):
    """Executes the CrewAI workflow."""
    research_agent = Agent(
        role="Senior Market Researcher",
        goal=f"Gather live news and financial data for {ticker} as of {TODAY}.",
        backstory="Expert researcher. You use web search if YFinance is down.",
        tools=[web_search_tool, yfinance_data_tool],
        llm=MODEL
    )
    
    sentiment_agent = Agent(
        role="Market Sentiment Analyst",
        goal="Determine if investor sentiment is Bullish, Bearish, or Neutral.",
        backstory="Behavioral economist analyzing news cycles.",
        llm=MODEL
    )
    
    risk_agent = Agent(
        role="Chief Risk Officer",
        goal=f"Identify 3 major regulatory or macro risks for {ticker}.",
        backstory="Highly cautious risk officer looking for downside triggers.",
        llm=MODEL
    )
    
    analyst_agent = Agent(
        role="Lead Financial Analyst",
        goal="Synthesize findings into an executive summary in ₹ (INR).",
        backstory="Top-tier analyst writing professional reports.",
        llm=MODEL
    )
    
    tasks = [
        Task(description=f"Find current price and 5 news articles for {ticker}.", expected_output="Data dossier.", agent=research_agent),
        Task(description="Analyze news for sentiment.", expected_output="Sentiment report.", agent=sentiment_agent),
        Task(description="Identify 3 major risks.", expected_output="Risk list.", agent=risk_agent),
        Task(description=f"Draft the final Executive Summary. Use Date: {TODAY}.", expected_output="Markdown report.", agent=analyst_agent)
    ]
    
    crew = Crew(agents=[research_agent, sentiment_agent, risk_agent, analyst_agent], tasks=tasks, process=Process.sequential)
    return crew.kickoff(inputs={"company": ticker})

st.set_page_config(page_title="AI Hedge Fund Analyst", page_icon="🏦", layout="centered")

st.title("🏦 AI Hedge Fund Strategy Desk")
st.markdown("Generate institutional-grade investment memos powered by AI.")

with st.sidebar:
    st.header("Account Status")
    usage = st.session_state.get('usage_count', 0)
    st.metric(label="Reports Generated Today", value=f"{usage} / 2")
    st.progress(usage / 2)
    if usage >= 2:
        st.error("Daily limit reached. Come back tomorrow!")

st.info("💡 **Don't see your company?** [Click here to search Yahoo Finance for the symbol](https://finance.yahoo.com/lookup). Look for symbols ending in `.NS` (NSE) or `.BO` (BSE).")

st.subheader("Select Asset for Analysis")

selection = st.selectbox(
    "Search or select a company:", 
    options=list(POPULAR_STOCKS.keys()) + ["➕ Other (Enter Ticker manually)"]
)

if selection == "➕ Other (Enter Ticker manually)":
    target_ticker = st.text_input("Enter Yahoo Finance Ticker (e.g., TATAPOWER.NS)").upper()
else:
    target_ticker = POPULAR_STOCKS[selection]
    st.caption(f"Mapped to Ticker: `{target_ticker}`")

can_run = check_daily_limit()

if st.button(" Generate Investment Memo", type="primary", disabled=not can_run):
    if not target_ticker:
        st.warning("Please enter a valid ticker.")
    else:
        st.session_state['usage_count'] += 1
        
        with st.status(" AI is analyzing the market... (This takes 30-60 seconds)", expanded=True):
            st.write("1.  Fetching live market data...")
            st.write("2.  Reading today's news headlines...")
            st.write("3.  Assessing risk and sentiment...")
            
            report = run_analysis(target_ticker)
           
        st.success("Analysis Complete!")
        st.markdown("---")
 
        col1, col2 = st.columns([1, 4])
        with col1:
            st.write("**TO:**")
            st.write("**FROM:**")
            st.write("**DATE:**")
            st.write("**SUBJECT:**")
            st.write("**ASSET:**")
        with col2:
            st.write("Investment Committee")
            st.write("Lead Financial Analyst (AI)")
            st.write(TODAY)
            st.write("Real-Time Strategic Outlook & Risk Assessment")
            st.write(f"**{selection}** (`{target_ticker}`)")
        
        st.markdown("---")
        
        # Render the AI Output
        st.markdown(str(report))
        
        # --- COMPLIANCE DISCLAIMER ---
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.warning("""
        **⚠️ REGULATORY & COMPLIANCE DISCLAIMER**
        
        * **Not SEBI Registered:** We are NOT registered with the Securities and Exchange Board of India (SEBI) as Investment Advisors.
        * **No Financial Advice:** This document is for educational purposes only and does not constitute a recommendation to buy or sell securities.
        * **AI-Generated Content:** This report was synthesized by Artificial Intelligence. Data may be delayed or subject to hallucinations. Please independently verify all metrics.
        * **Market Risk:** Equity investments are subject to market risks. Consult a certified financial advisor before deploying capital.
        """, icon="⚖️")

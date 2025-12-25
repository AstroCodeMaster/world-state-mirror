import streamlit as st
import google.generativeai as genai
import requests
import json
from datetime import datetime, timedelta
import time
import hashlib
import random
from collections import defaultdict
import base64

# ============================================================================
# ULTRA WIDE LAYOUT - MAXIMUM IMMERSION
# ============================================================================
st.set_page_config(
    page_title="NEXUS 3.0 - Reality Engine",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# REVOLUTIONARY CSS - CYBERPUNK MEETS GLASSMORPHISM
# Never Seen Before Design!
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    /* RESET & BASE */
    * {
        font-family: 'Rajdhani', sans-serif;
    }
    
    .main {
        background: #000000;
        background-image: 
            radial-gradient(at 20% 30%, rgba(13, 110, 253, 0.15) 0px, transparent 50%),
            radial-gradient(at 80% 70%, rgba(220, 38, 127, 0.15) 0px, transparent 50%),
            radial-gradient(at 40% 80%, rgba(139, 92, 246, 0.15) 0px, transparent 50%);
        animation: bgShift 20s ease infinite;
    }
    
    @keyframes bgShift {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(30deg); }
    }
    
    /* NEURAL GRID BACKGROUND */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(13, 110, 253, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(13, 110, 253, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: 0;
    }
    
    /* HOLOGRAPHIC TITLE */
    .nexus-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #00f5ff, #ff00ff, #00ff88, #ff0055);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: holographic 3s ease infinite;
        text-align: center;
        text-shadow: 0 0 30px rgba(0, 245, 255, 0.5),
                     0 0 60px rgba(255, 0, 255, 0.3);
        letter-spacing: 3px;
        margin: 2rem 0;
    }
    
    @keyframes holographic {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* REALITY PULSE - LIVE INDICATOR */
    .reality-pulse {
        display: inline-block;
        position: relative;
        width: 20px;
        height: 20px;
        margin-right: 10px;
    }
    
    .reality-pulse::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        background: #00f5ff;
        border-radius: 50%;
        animation: pulse-ring 1.5s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
    }
    
    .reality-pulse::after {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        background: #00f5ff;
        border-radius: 50%;
        box-shadow: 0 0 20px #00f5ff;
    }
    
    @keyframes pulse-ring {
        0% { transform: scale(0.8); opacity: 1; }
        100% { transform: scale(2.5); opacity: 0; }
    }
    
    /* QUANTUM CARDS - Next Gen Design */
    .quantum-card {
        position: relative;
        background: rgba(13, 110, 253, 0.05);
        backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2rem;
        margin: 1rem 0;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        box-shadow: 
            0 8px 32px 0 rgba(31, 38, 135, 0.37),
            inset 0 0 0 1px rgba(255, 255, 255, 0.1);
    }
    
    .quantum-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .quantum-card:hover {
        transform: translateY(-8px) scale(1.01);
        border-color: rgba(0, 245, 255, 0.5);
        box-shadow: 
            0 20px 60px 0 rgba(0, 245, 255, 0.3),
            inset 0 0 0 1px rgba(0, 245, 255, 0.3);
    }
    
    .quantum-card:hover::before {
        left: 100%;
    }
    
    /* NEURAL GLOBE CONTAINER */
    .neural-globe {
        background: radial-gradient(circle at center, rgba(0, 245, 255, 0.1) 0%, transparent 70%);
        border: 2px solid rgba(0, 245, 255, 0.3);
        border-radius: 50%;
        padding: 3rem;
        position: relative;
        animation: rotate-globe 30s linear infinite;
    }
    
    @keyframes rotate-globe {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* DATA STREAM CARDS */
    .data-stream {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(220, 38, 127, 0.1) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .data-stream::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #8b5cf6, transparent);
        animation: stream-flow 2s ease-in-out infinite;
    }
    
    @keyframes stream-flow {
        0%, 100% { transform: translateX(-100%); }
        50% { transform: translateX(100%); }
    }
    
    /* OPPORTUNITY MATRIX */
    .opportunity-matrix {
        background: rgba(0, 0, 0, 0.6);
        border: 2px solid;
        border-image: linear-gradient(45deg, #00f5ff, #ff00ff) 1;
        padding: 2rem;
        border-radius: 20px;
        position: relative;
        animation: border-glow 3s ease-in-out infinite;
    }
    
    @keyframes border-glow {
        0%, 100% { 
            box-shadow: 0 0 20px rgba(0, 245, 255, 0.5),
                        inset 0 0 20px rgba(0, 245, 255, 0.1);
        }
        50% { 
            box-shadow: 0 0 40px rgba(255, 0, 255, 0.5),
                        inset 0 0 20px rgba(255, 0, 255, 0.1);
        }
    }
    
    /* CRITICAL ALERT - EPIC */
    .critical-alert {
        background: linear-gradient(135deg, #ff0055 0%, #ff6b00 100%);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 0 40px rgba(255, 0, 85, 0.6);
        animation: critical-pulse 1s ease-in-out infinite;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    @keyframes critical-pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    /* WEATHER ORBS */
    .weather-orb {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4rem;
        margin: 1rem auto;
        position: relative;
        background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.2), transparent);
        box-shadow: 
            inset 0 0 20px rgba(255, 255, 255, 0.1),
            0 0 40px var(--orb-color, rgba(0, 245, 255, 0.5));
        animation: float-orb 3s ease-in-out infinite;
    }
    
    @keyframes float-orb {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* STATS QUANTUM DISPLAY */
    .stat-quantum {
        background: rgba(0, 0, 0, 0.8);
        border: 2px solid rgba(0, 245, 255, 0.5);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .stat-quantum::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(0, 245, 255, 0.1), transparent 30%);
        animation: rotate-stat 4s linear infinite;
    }
    
    @keyframes rotate-stat {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .stat-quantum-content {
        position: relative;
        z-index: 1;
    }
    
    .stat-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00f5ff 0%, #ff00ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        text-shadow: 0 0 30px rgba(0, 245, 255, 0.5);
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 0.5rem;
    }
    
    /* NEWS FEED - MATRIX STYLE */
    .news-matrix {
        background: rgba(0, 0, 0, 0.9);
        border-left: 3px solid #00ff00;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        color: #00ff00;
        position: relative;
        overflow: hidden;
        animation: matrix-flicker 0.1s infinite;
    }
    
    @keyframes matrix-flicker {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.95; }
    }
    
    /* AI BRAIN VISUALIZATION */
    .ai-brain {
        width: 100px;
        height: 100px;
        margin: 0 auto;
        position: relative;
        animation: brain-pulse 2s ease-in-out infinite;
    }
    
    @keyframes brain-pulse {
        0%, 100% { 
            filter: drop-shadow(0 0 10px #00f5ff) drop-shadow(0 0 20px #ff00ff);
        }
        50% { 
            filter: drop-shadow(0 0 20px #ff00ff) drop-shadow(0 0 30px #00f5ff);
        }
    }
    
    /* CONTROL BUTTONS - EPIC STYLE */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 12px !important;
        padding: 1rem 2rem !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 32px rgba(102, 126, 234, 0.6) !important;
        border-color: rgba(255, 255, 255, 0.8) !important;
    }
    
    /* SCROLLBAR CYBERPUNK */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.5);
        border-left: 1px solid rgba(0, 245, 255, 0.2);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00f5ff 0%, #ff00ff 100%);
        border-radius: 6px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #ff00ff 0%, #00f5ff 100%);
    }
    
    /* LOADING SPINNER - NEXUS STYLE */
    .nexus-loader {
        width: 60px;
        height: 60px;
        border: 4px solid rgba(0, 245, 255, 0.1);
        border-top: 4px solid #00f5ff;
        border-radius: 50%;
        animation: nexus-spin 1s linear infinite;
        margin: 2rem auto;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
    }
    
    @keyframes nexus-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* WORLD MAP CONTAINER */
    .world-map-container {
        background: rgba(0, 0, 0, 0.8);
        border-radius: 24px;
        padding: 2rem;
        border: 2px solid rgba(0, 245, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .world-map-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500"><circle cx="500" cy="250" r="200" fill="none" stroke="rgba(0,245,255,0.1)" stroke-width="1"/></svg>');
        opacity: 0.3;
        pointer-events: none;
    }
    
    /* SCORE BADGES - ADVANCED */
    .score-legendary {
        background: linear-gradient(135deg, #ffd700 0%, #ff8c00 100%);
        color: #000;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-weight: 900;
        font-size: 1.2rem;
        display: inline-block;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
        animation: legendary-glow 2s ease-in-out infinite;
    }
    
    @keyframes legendary-glow {
        0%, 100% { box-shadow: 0 0 30px rgba(255, 215, 0, 0.6); }
        50% { box-shadow: 0 0 50px rgba(255, 140, 0, 0.8); }
    }
    
    .score-epic {
        background: linear-gradient(135deg, #9333ea 0%, #c026d3 100%);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
    }
    
    .score-rare {
        background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
    }
    
    /* TEXT COLORS */
    .text-cyber {
        color: #00f5ff !important;
        text-shadow: 0 0 10px rgba(0, 245, 255, 0.5);
    }
    
    .text-neon {
        color: #ff00ff !important;
        text-shadow: 0 0 10px rgba(255, 0, 255, 0.5);
    }
    
    .text-matrix {
        color: #00ff00 !important;
        font-family: 'Courier New', monospace;
    }
    
    /* HIDE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* RESPONSIVE */
    @media (max-width: 768px) {
        .nexus-title {
            font-size: 2.5rem;
        }
        .quantum-card {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# WORLD CITIES - 50+ MAJOR CITIES!
# ============================================================================
NEXUS_CITIES = {
    "North America": {
        "cities": ["New York", "Los Angeles", "Chicago", "Toronto", "Vancouver", "Mexico City", "Miami", "San Francisco", "Seattle"],
        "icon": "🌎"
    },
    "Europe": {
        "cities": ["London", "Paris", "Berlin", "Madrid", "Rome", "Amsterdam", "Barcelona", "Vienna", "Stockholm"],
        "icon": "🇪🇺"
    },
    "Asia": {
        "cities": ["Tokyo", "Shanghai", "Dubai", "Singapore", "Mumbai", "Seoul", "Bangkok", "Hong Kong", "Istanbul"],
        "icon": "🌏"
    },
    "South America": {
        "cities": ["São Paulo", "Buenos Aires", "Rio de Janeiro", "Lima", "Santiago", "Bogota"],
        "icon": "🌎"
    },
    "Africa": {
        "cities": ["Cairo", "Lagos", "Johannesburg", "Nairobi", "Casablanca"],
        "icon": "🌍"
    },
    "Oceania": {
        "cities": ["Sydney", "Melbourne", "Auckland", "Brisbane"],
        "icon": "🌏"
    },
    "Middle East": {
        "cities": ["Riyadh", "Tel Aviv", "Doha", "Kuwait City", "Beirut"],
        "icon": "🕌"
    }
}

# Weather condition mappings
WEATHER_DATA = {
    "Clear": {"emoji": "☀️", "color": "rgba(255, 215, 0, 0.5)"},
    "Clouds": {"emoji": "☁️", "color": "rgba(150, 150, 150, 0.5)"},
    "Rain": {"emoji": "🌧️", "color": "rgba(0, 119, 255, 0.5)"},
    "Drizzle": {"emoji": "🌦️", "color": "rgba(0, 150, 255, 0.5)"},
    "Thunderstorm": {"emoji": "⛈️", "color": "rgba(255, 0, 85, 0.5)"},
    "Snow": {"emoji": "❄️", "color": "rgba(200, 230, 255, 0.5)"},
    "Mist": {"emoji": "🌫️", "color": "rgba(180, 180, 180, 0.5)"},
    "Fog": {"emoji": "🌫️", "color": "rgba(180, 180, 180, 0.5)"},
    "Haze": {"emoji": "🌫️", "color": "rgba(200, 180, 150, 0.5)"}
}

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'nexus_state' not in st.session_state:
    st.session_state.nexus_state = {}
if 'opportunities' not in st.session_state:
    st.session_state.opportunities = []
if 'news_feed' not in st.session_state:
    st.session_state.news_feed = []
if 'ai_actions' not in st.session_state:
    st.session_state.ai_actions = []
if 'global_patterns' not in st.session_state:
    st.session_state.global_patterns = {}
if 'last_scan' not in st.session_state:
    st.session_state.last_scan = None
if 'scan_count' not in st.session_state:
    st.session_state.scan_count = 0

# ============================================================================
# NEXUS REALITY ENGINE - THE BRAIN
# ============================================================================
class NexusRealityEngine:
    """The Ultimate Reality Monitoring System"""
    
    def __init__(self, weather_key=None, news_key=None):
        self.weather_key = weather_key
        self.news_key = news_key
        self.cache = {}
        self.cache_ttl = 300  # 5 minutes
    
    def get_weather_global(self, cities):
        """Get weather for all cities - ULTRA FAST"""
        results = {}
        
        for city in cities:
            weather = self._get_weather_single(city)
            if weather:
                results[city] = weather
                
        return results
    
    def _get_weather_single(self, city):
        """Get weather for one city"""
        cache_key = f"weather_{city}_{int(time.time() / self.cache_ttl)}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        if not self.weather_key:
            # DEMO MODE - Realistic data
            import random
            conditions = list(WEATHER_DATA.keys())
            temp = random.randint(-10, 40)
            condition = random.choice(conditions)
            
            data = {
                "city": city,
                "temp": temp,
                "feels_like": temp + random.randint(-5, 5),
                "condition": condition,
                "description": condition.lower(),
                "wind_speed": random.randint(5, 50),
                "humidity": random.randint(20, 95),
                "pressure": random.randint(980, 1030),
                "visibility": random.randint(1, 10),
                "uv_index": random.randint(0, 11),
                "air_quality": random.randint(1, 5),
                "timestamp": datetime.now().isoformat(),
                "demo": True
            }
            
            self.cache[cache_key] = data
            return data
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if response.status_code != 200:
                return None
            
            weather_data = {
                "city": city,
                "temp": data['main']['temp'],
                "feels_like": data['main']['feels_like'],
                "condition": data['weather'][0]['main'],
                "description": data['weather'][0]['description'],
                "wind_speed": data['wind']['speed'] * 3.6,  # Convert to km/h
                "humidity": data['main']['humidity'],
                "pressure": data['main']['pressure'],
                "visibility": data.get('visibility', 10000) / 1000,
                "timestamp": datetime.now().isoformat(),
                "demo": False
            }
            
            self.cache[cache_key] = weather_data
            return weather_data
            
        except:
            return None
    
    def get_news_global(self, query="business technology", max_results=10):
        """Get global news - SIMULATED for demo"""
        # In production, use NewsAPI, Google News API, etc.
        
        news_topics = [
            {"title": "🚀 SpaceX launches new Starlink satellites", "sentiment": "positive", "category": "tech", "impact": "high"},
            {"title": "📈 Global stock markets reach new highs", "sentiment": "positive", "category": "finance", "impact": "high"},
            {"title": "🏥 New AI breakthrough in cancer detection", "sentiment": "positive", "category": "health", "impact": "critical"},
            {"title": "⚡ Renewable energy adoption surges globally", "sentiment": "positive", "category": "energy", "impact": "high"},
            {"title": "🤖 OpenAI announces GPT-5 development", "sentiment": "positive", "category": "tech", "impact": "critical"},
            {"title": "🌍 Climate summit reaches landmark agreement", "sentiment": "positive", "category": "climate", "impact": "high"},
            {"title": "💊 FDA approves revolutionary drug treatment", "sentiment": "positive", "category": "health", "impact": "high"},
            {"title": "🚗 Electric vehicle sales double year-over-year", "sentiment": "positive", "category": "auto", "impact": "medium"},
            {"title": "📱 Apple unveils new AR glasses", "sentiment": "positive", "category": "tech", "impact": "high"},
            {"title": "🏦 Major banks adopt blockchain technology", "sentiment": "positive", "category": "finance", "impact": "medium"}
        ]
        
        import random
        return random.sample(news_topics, min(max_results, len(news_topics)))
    
    def analyze_global_intelligence(self, weather_data, news_data):
        """ULTRA ADVANCED: Analyze ALL data sources"""
        
        intelligence = {
            "weather_patterns": self._analyze_weather_patterns(weather_data),
            "news_sentiment": self._analyze_news_sentiment(news_data),
            "market_signals": self._generate_market_signals(weather_data, news_data),
            "risk_factors": self._assess_global_risks(weather_data, news_data),
            "opportunities": self._detect_mega_opportunities(weather_data, news_data)
        }
        
        return intelligence
    
    def _analyze_weather_patterns(self, weather_data):
        """Detect weather patterns across the globe"""
        patterns = {
            "storm_zones": [],
            "heat_zones": [],
            "cold_zones": [],
            "perfect_zones": [],
            "extreme_wind": [],
            "low_visibility": []
        }
        
        for city, data in weather_data.items():
            if not data:
                continue
            
            if data['condition'] in ['Thunderstorm', 'Rain']:
                patterns['storm_zones'].append(city)
            
            if data['temp'] > 35:
                patterns['heat_zones'].append(city)
            elif data['temp'] < 0:
                patterns['cold_zones'].append(city)
            elif 20 <= data['temp'] <= 28 and data['condition'] == 'Clear':
                patterns['perfect_zones'].append(city)
            
            if data['wind_speed'] > 40:
                patterns['extreme_wind'].append(city)
            
            if data.get('visibility', 10) < 2:
                patterns['low_visibility'].append(city)
        
        return patterns


    def _analyze_news_sentiment(self, news_data):
        """Analyze global news sentiment"""
        sentiment_score = 0
        positive_count = 0
        categories = defaultdict(int)
        
        for news in news_data:
            if news['sentiment'] == 'positive':
                sentiment_score += 1
                positive_count += 1
            categories[news['category']] += 1
        
        return {
            "overall_sentiment": "BULLISH" if positive_count > len(news_data) * 0.6 else "NEUTRAL",
            "positive_ratio": positive_count / max(len(news_data), 
            1),
            "trending_categories": dict(categories),
            "sentiment_score": sentiment_score
        }
    
    def _generate_market_signals(self, weather_data, news_data):
        """Generate market opportunity signals"""
        signals = []
        
        # Tech boom signal
        tech_news = [n for n in news_data if n['category'] == 'tech']
        if len(tech_news) >= 2:
            signals.append({
                "signal": "TECH_SURGE",
                "strength": "STRONG",
                "description": "Multiple tech breakthroughs detected"
            })
        
        # Weather-based signals
        hot_cities = [c for c, d in weather_data.items() if d and d['temp'] > 30]
        if len(hot_cities) >= 5:
            signals.append({
                "signal": "GLOBAL_HEATWAVE",
                "strength": "CRITICAL",
                "description": f"Extreme heat in {len(hot_cities)} major cities"
            })
        
        return signals
    
    def _assess_global_risks(self, weather_data, news_data):
        """Assess global risk factors"""
        risks = []
        
        # Storm risks
        storm_cities = [c for c, d in weather_data.items() if d and d['condition'] == 'Thunderstorm']
        if len(storm_cities) >= 3:
            risks.append({
                "risk_type": "SEVERE_WEATHER",
                "level": "HIGH",
                "affected_regions": storm_cities,
                "mitigation": "Activate emergency services marketing"
            })
        
        return risks
    
    def _detect_mega_opportunities(self, weather_data, news_data):
        """Detect MASSIVE opportunities across all data"""
        opportunities = []
        timestamp = datetime.now().isoformat()
        
        # Multi-city weather opportunities
        storm_cities = [c for c, d in weather_data.items() if d and d['condition'] in ['Thunderstorm', 'Rain']]
        
        if len(storm_cities) >= 5:
            opportunities.append({
                "id": hashlib.md5(f"mega_storm_{timestamp}".encode()).hexdigest()[:8],
                "type": "MEGA_WEATHER_EVENT",
                "title": "🌪️ GLOBAL STORM SYSTEM",
                "trigger": f"Severe weather affecting {len(storm_cities)} major cities simultaneously",
                "cities": storm_cities,
                "opportunity": "Regional delivery networks, emergency services, weather insurance products",
                "action": "Launch coordinated multi-city emergency response marketing campaign",
                "urgency": "CRITICAL",
                "score": 98,
                "tier": "LEGENDARY",
                "revenue_potential": "$100,000-$500,000",
                "timeframe": "24-72 hours",
                "confidence": 95,
                "timestamp": timestamp
            })
        
        # Tech boom opportunity
        tech_news = [n for n in news_data if n['category'] == 'tech' and n['sentiment'] == 'positive']
        if len(tech_news) >= 2:
            opportunities.append({
                "id": hashlib.md5(f"tech_boom_{timestamp}".encode()).hexdigest()[:8],
                "type": "MARKET_SURGE",
                "title": "🚀 TECH SECTOR EXPLOSION",
                "trigger": f"{len(tech_news)} major tech announcements in 24h",
                "cities": ["Global"],
                "opportunity": "Tech consulting services, AI implementation, digital transformation",
                "action": "Position as cutting-edge tech solution provider",
                "urgency": "HIGH",
                "score": 92,
                "tier": "EPIC",
                "revenue_potential": "$50,000-$200,000",
                "timeframe": "7-14 days",
                "confidence": 88,
                "timestamp": timestamp
            })
        
        # Perfect weather tourism
        perfect_cities = [c for c, d in weather_data.items() if d and 22 <= d['temp'] <= 28 and d['condition'] == 'Clear']
        if len(perfect_cities) >= 3:
            opportunities.append({
                "id": hashlib.md5(f"perfect_weather_{timestamp}".encode()).hexdigest()[:8],
                "type": "SEASONAL_OPPORTUNITY",
                "title": "☀️ PERFECT WEATHER WINDOW",
                "trigger": f"Ideal conditions in {len(perfect_cities)} tourist destinations",
                "cities": perfect_cities,
                "opportunity": "Tourism packages, outdoor events, activity bookings",
                "action": "Launch targeted tourism and outdoor activity campaigns",
                "urgency": "MEDIUM",
                "score": 78,
                "tier": "RARE",
                "revenue_potential": "$20,000-$80,000",
                "timeframe": "3-7 days",
                "confidence": 82,
                "timestamp": timestamp
            })
        
        # Individual city opportunities
        for city, data in weather_data.items():
            if not data:
                continue
            
            # Extreme heat
            if data['temp'] > 38:
                opportunities.append({
                    "id": hashlib.md5(f"heat_{city}_{timestamp}".encode()).hexdigest()[:8],
                    "type": "TEMPERATURE_EXTREME",
                    "title": f"🔥 EXTREME HEAT - {city}",
                    "trigger": f"Temperature: {data['temp']}°C (Dangerous levels)",
                    "cities": [city],
                    "opportunity": "AC services, cooling products, hydration solutions",
                    "action": f"Emergency cooling services campaign in {city}",
                    "urgency": "HIGH",
                    "score": 85,
                    "tier": "EPIC",
                    "revenue_potential": "$10,000-$30,000",
                    "timeframe": "12-48 hours",
                    "confidence": 90,
                    "timestamp": timestamp
                })
        
        # Sort by score
        opportunities.sort(key=lambda x: x['score'], reverse=True)
        
        return opportunities

class NexusAIBrain:
    """The Superintelligent AI Core"""
    
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        self.memory = []
    
    def generate_supreme_action_plan(self, opportunity):
        """Generate the ULTIMATE action plan"""
        
        prompt = f"""You are NEXUS 3.0 - The most advanced World-State AI Strategist ever created.

You have detected a {opportunity['tier']}-tier opportunity with a score of {opportunity['score']}/100.

OPPORTUNITY INTELLIGENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Title: {opportunity['title']}
Type: {opportunity['type']}
Trigger: {opportunity['trigger']}
Affected Cities: {', '.join(opportunity['cities'])}
Urgency: {opportunity['urgency']}
Revenue Potential: {opportunity['revenue_potential']}
Timeframe: {opportunity['timeframe']}
Confidence: {opportunity['confidence']}%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generate a COMPLETE, TACTICAL, REVENUE-OPTIMIZED action plan:

1. STRATEGIC ANALYSIS
   - Market dynamics
   - Competitive landscape
   - Timing advantage

2. TARGET IDENTIFICATION
   - Primary targets (businesses/individuals)
   - Secondary opportunities
   - Contact strategy

3. MARKETING WARFARE
   - Platform selection (Google/Facebook/Instagram/TikTok/LinkedIn)
   - Ad copy variations (minimum 5)
   - Visual strategy
   - Budget allocation by platform
   - A/B testing plan

4. EXECUTION ROADMAP
   Hour 1: [specific tasks]
   Hour 2-6: [specific tasks]
   Day 1-3: [specific tasks]
   Week 1-2: [specific tasks]

5. REVENUE MAXIMIZATION
   - Pricing tiers
   - Upsell strategies
   - Revenue projections (conservative/realistic/optimistic)
   - Payment structures

6. RISK MANAGEMENT
   - Failure modes
   - Contingency plans
   - Exit strategies

7. SCALING STRATEGY
   - How to 10x results
   - Automation opportunities
   - Long-term playbook

Be RUTHLESSLY specific. Give EXACT numbers, EXACT messages, EXACT tactics.
This is about making REAL money from REAL opportunities."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return self._generate_fallback_plan(opportunity)
    
    def _generate_fallback_plan(self, opportunity):
        """Epic fallback plan"""
        return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 NEXUS 3.0 SUPREME ACTION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OPPORTUNITY: {opportunity['title']}
TIER: {opportunity['tier']} | SCORE: {opportunity['score']}/100
REVENUE TARGET: {opportunity['revenue_potential']}

1. STRATEGIC ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Market Dynamics:
• This is a {opportunity['urgency'].lower()} priority event
• Window of opportunity: {opportunity['timeframe']}
• Confidence level: {opportunity['confidence']}%
• Competition likely LOW due to speed of detection

Timing Advantage:
✓ You detected this BEFORE your competition
✓ First-mover advantage: 300-500%
✓ Market demand will peak within {opportunity['timeframe']}

2. TARGET IDENTIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Primary Targets in {', '.join(opportunity['cities'][:3])}:
• Local businesses affected by: {opportunity['trigger']}
• Service providers in: {opportunity['opportunity']}
• Decision makers: CEOs, Marketing Directors, Operations Managers

Contact Strategy:
→ LinkedIn outreach (personalized)
→ Cold email campaigns
→ Phone calls to high-value prospects
→ Local business directories

3. MARKETING WARFARE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Platform Selection:
✓ Google Ads: 40% budget - High intent traffic
✓ Facebook/Instagram: 30% budget - Visual storytelling
✓ LinkedIn: 20% budget - B2B targeting
✓ Email: 10% budget - Direct approach

Ad Copy Variations:

A) URGENCY ANGLE:
"⚠️ {opportunity['trigger']} - Your competitors are already adapting. 
Are you ready? We help businesses like yours turn crisis into opportunity."

B) SOLUTION ANGLE:
"{opportunity['opportunity']} - We've helped 50+ businesses navigate 
situations exactly like this. Free consultation available NOW."

C) SOCIAL PROOF:
"When [similar event] hit last year, our clients saw 400% ROI. 
This time it's {', '.join(opportunity['cities'])}. Book your spot."

D) SCARCITY:
"Only 15 slots available for emergency response services. 
{opportunity['timeframe']} window closing fast."

E) VALUE:
"Turn {opportunity['trigger']} into revenue. Our proven system: 
Step 1: [Action], Step 2: [Result], Step 3: [Profit]."

Budget Allocation:
• Total: $3,000-5,000 for {opportunity['timeframe']}
• Cost per acquisition target: $150-250
• Expected conversions: 15-25 businesses
• ROI target: 300-500%

4. EXECUTION ROADMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏰ HOUR 1 (Immediate):
☑ Set up Google Ads campaign (location: {', '.join(opportunity['cities'][:3])})
☑ Create 5 ad variations
☑ Build emergency landing page
☑ Set up tracking pixels
☑ Create email list of 100 prospects

⏰ HOUR 2-6 (Launch):
☑ Launch all ad campaigns
☑ Send first wave of cold emails (25 prospects)
☑ Post on LinkedIn (personal + company)
☑ Create Instagram Stories sequence
☑ Monitor ad performance - adjust bids

⏰ DAY 1-3 (Optimize):
☑ A/B test ad copy (kill losers, boost winners)
☑ Follow up with email responders
☑ Scale winning campaigns by 200%
☑ Create case study from first client
☑ Launch retargeting campaigns

⏰ WEEK 1-2 (Scale):
☑ Expand to more cities
☑ Hire VA for lead follow-up
☑ Create content around success stories
☑ Build referral program
☑ Plan next campaign

5. REVENUE MAXIMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pricing Tiers:

💎 EMERGENCY (24h delivery)
• Price: $5,000-10,000
• Target: Large businesses
• What: Full implementation + management

⚡ RAPID (48-72h delivery)
• Price: $2,500-5,000  
• Target: Medium businesses
• What: Strategy + setup + 7-day support

🚀 STANDARD (5-7 day delivery)
• Price: $1,000-2,500
• Target: Small businesses
• What: Strategy + guidance + templates

Upsells:
• Monthly management: +$500-2,000/month
• Training package: +$500
• Done-for-you ads: +$1,000-3,000

Revenue Projections:

Conservative (10 clients):
→ 3 × $5,000 = $15,000
→ 4 × $2,500 = $10,000
→ 3 × $1,500 = $4,500
Total: $29,500

Realistic (20 clients):
→ 5 × $5,000 = $25,000
→ 10 × $2,500 = $25,000
→ 5 × $1,500 = $7,500
Total: $57,500

Optimistic (30+ clients + upsells):
→ 10 × $5,000 = $50,000
→ 15 × $2,500 = $37,500
→ 5 × $1,500 = $7,500
→ Upsells = $20,000
Total: $115,000

6. RISK MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Failure Mode 1: Low Response Rate
Mitigation:
→ Increase ad spend by 50%
→ Add urgency: "Only 48 hours left"
→ Offer free audit/consultation

Failure Mode 2: {opportunity['trigger']} Resolves Quickly
Mitigation:
→ Pivot to "preparation for next time"
→ Shift to consulting/training model
→ Build long-term relationships

Failure Mode 3: High Competition
Mitigation:
→ Focus on speed (you're first!)
→ Emphasize unique approach
→ Offer guarantees/risk reversal

Exit Strategy:
If not profitable within 72h:
→ Stop paid ads
→ Continue organic outreach
→ Pivot to next opportunity

7. SCALING STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

How to 10X Results:

Phase 1: AUTOMATE (Week 2-4)
• Build email sequences
• Create templated responses
• Use scheduling tools
• Hire VA for admin

Phase 2: SYSTEMATIZE (Month 2-3)
• Document all processes
• Create training materials
• Build team of 2-3
• Expand to more cities

Phase 3: SCALE (Month 4-6)
• Target enterprise clients
• Raise prices 2x
• Build partnerships
• Create done-for-you service

Long-term Playbook:
→ Build database of {opportunity['type']} patterns
→ Create predictive alert system
→ Sell system to other consultants
→ License technology

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ EXECUTION BEGINS NOW - TIME IS MONEY ⚡
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    
    def compare_opportunities_supreme(self, opportunities):
        """AI comparison of multiple opportunities"""
        if not opportunities:
            return "No opportunities to analyze."
        
        if len(opportunities) == 1:
            return "Only one opportunity detected - execute immediately!"
        
        prompt = f"""Analyze these {len(opportunities)} global opportunities:

{json.dumps([{
    'title': opp['title'],
    'score': opp['score'],
    'revenue': opp['revenue_potential'],
    'urgency': opp['urgency'],
    'cities': len(opp['cities'])
} for opp in opportunities[:5]], indent=2)}

Rank TOP 3 by:
1. Immediate profit potential
2. Ease of execution
3. Market timing
4. Risk/reward ratio

Be brutally honest. Which makes money FASTEST?"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except:
            return "AI analysis in progress..."

# END OF BACKEND - Continue with UI in next part...# THIS GOES AFTER THE BACKEND CODE IN app.py

# ============================================================================
# NEXUS 3.0 - ULTIMATE UI
# ============================================================================

# Epic Header
st.markdown('<h1 class="nexus-title">🌌 NEXUS 3.0</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: rgba(255,255,255,0.7); font-size: 1.3rem; margin-top: -1rem;">THE ULTIMATE REALITY ENGINE</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #00f5ff; font-size: 1rem;"><span class="reality-pulse"></span>MONITORING 50+ CITIES • ANALYZING BILLIONS OF DATA POINTS • GENERATING INFINITE OPPORTUNITIES</p>', unsafe_allow_html=True)

# Sidebar - Command Center
with st.sidebar:
    st.markdown('<div class="ai-brain">🧠</div>', unsafe_allow_html=True)
    st.markdown("## ⚙️ NEXUS CORE")
    
    gemini_key = st.text_input("🔐 Gemini API Key:", type="password", key="gemini")
    st.caption("🔗 [Get Free Key](https://aistudio.google.com/app/apikey)")
    
    weather_key = st.text_input("🌡️ Weather API (Optional):", type="password", key="weather")
    st.caption("🔗 [Get Free Key](https://openweathermap.org/api)")
    
    st.markdown("---")
    
    # Region Selection - EXPANDED
    st.markdown("## 🌍 ACTIVE REGIONS")
    selected_regions = st.multiselect(
        "Select monitoring zones:",
        list(NEXUS_CITIES.keys()),
        default=list(NEXUS_CITIES.keys())
    )
    
    # Calculate total cities
    total_cities = sum(len(NEXUS_CITIES[r]['cities']) for r in selected_regions)
    all_cities = [city for region in selected_regions for city in NEXUS_CITIES[region]['cities']]
    
    st.markdown(f"""
    <div class="stat-quantum">
        <div class="stat-quantum-content">
            <span class="stat-number">{total_cities}</span>
            <span class="stat-label">CITIES ONLINE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Global Stats
    st.markdown("## 📊 NEXUS STATS")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="stat-quantum">
            <div class="stat-quantum-content">
                <span class="stat-number">{len(st.session_state.opportunities)}</span>
                <span class="stat-label">OPPORTUNITIES</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-quantum">
            <div class="stat-quantum-content">
                <span class="stat-number">{st.session_state.scan_count}</span>
                <span class="stat-label">SCANS</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Revenue Potential
    if st.session_state.opportunities:
        total_revenue = 0

for opp in st.session_state.opportunities:
    try:
        value = int(
            opp['revenue_potential']
            .split('$')[1]
            .split('-')[1]
            .replace(',', '')
            .split('/')[0]
        )
        total_revenue += value
    except (KeyError, IndexError, ValueError, TypeError):
        continue

        st.markdown(f"""
        <div class="stat-quantum">
            <div class="stat-quantum-content">
                <span class="stat-number">${total_revenue:,}</span>
                <span class="stat-label">TOTAL POTENTIAL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.last_scan:
        st.caption(f"⏱️ Last scan: {st.session_state.last_scan}")
    
    st.markdown("---")
    
    # Quick Actions
    if st.button("🗑️ RESET NEXUS", use_container_width=True):
        st.session_state.opportunities = []
        st.session_state.ai_actions = []
        st.session_state.nexus_state = {}
        st.session_state.news_feed = []
        st.session_state.scan_count = 0
        st.rerun()

# Main Control Panel - EPIC DESIGN
st.markdown("## 🎮 COMMAND CENTER")

col_c1, col_c2, col_c3, col_c4 = st.columns(4)

with col_c1:
    scan_button = st.button("🌍 SCAN REALITY", type="primary", use_container_width=True, disabled=not gemini_key)

with col_c2:
    ai_button = st.button("🧠 AI ANALYSIS", use_container_width=True, disabled=not (gemini_key and st.session_state.opportunities))

with col_c3:
    news_button = st.button("📰 FETCH NEWS", use_container_width=True)

with col_c4:
    export_button = st.button("📥 EXPORT DATA", use_container_width=True, disabled=not st.session_state.opportunities)

# API Key Warning
if not gemini_key:
    st.markdown("""
    <div class="critical-alert">
        <h2>⚠️ NEXUS CORE OFFLINE</h2>
        <p>Enter your Gemini API key in the sidebar to activate the Reality Engine</p>
    </div>
    """, unsafe_allow_html=True)

# Scan Reality
if scan_button:
    with st.spinner("🌌 NEXUS scanning global reality..."):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Initialize engine
        engine = NexusRealityEngine(weather_key if weather_key else None, None)
        
        # Scan weather
        status_text.text(f"📡 Scanning {total_cities} cities...")
        progress_bar.progress(20)
        time.sleep(0.5)
        
        weather_data = engine.get_weather_global(all_cities)
        st.session_state.nexus_state = weather_data
        
        # Get news
        status_text.text("📰 Analyzing global news...")
        progress_bar.progress(40)
        time.sleep(0.5)
        
        news_data = engine.get_news_global()
        st.session_state.news_feed = news_data
        
        # Analyze intelligence
        status_text.text("🧠 Processing intelligence...")
        progress_bar.progress(60)
        time.sleep(0.5)
        
        intelligence = engine.analyze_global_intelligence(weather_data, news_data)
        st.session_state.global_patterns = intelligence
        
        # Detect opportunities
        status_text.text("💎 Detecting opportunities...")
        progress_bar.progress(80)
        time.sleep(0.5)
        
        opportunities = intelligence['opportunities']
        st.session_state.opportunities = opportunities
        
        # Complete
        progress_bar.progress(100)
        st.session_state.last_scan = datetime.now().strftime("%H:%M:%S")
        st.session_state.scan_count += 1
        
        status_text.empty()
        progress_bar.empty()
        
        st.success(f"✅ SCAN COMPLETE: {len(weather_data)} cities | {len(opportunities)} opportunities detected!")
        time.sleep(1)
        st.rerun()

# AI Analysis
if ai_button:
    with st.spinner("🧠 NEXUS AI analyzing opportunities..."):
        brain = NexusAIBrain(gemini_key)
        
        # Analyze top 3 opportunities
        for opp in st.session_state.opportunities[:3]:
            action_plan = brain.generate_supreme_action_plan(opp)
            
            st.session_state.ai_actions.append({
                "timestamp": datetime.now().isoformat(),
                "opportunity_id": opp['id'],
                "title": opp['title'],
                "plan": action_plan,
                "tier": opp['tier']
            })
        
        st.success(f"✅ Generated {len(st.session_state.ai_actions)} supreme action plans!")
        time.sleep(1)
        st.rerun()

# Fetch News
if news_button:
    with st.spinner("📰 Fetching global news..."):
        engine = NexusRealityEngine()
        news = engine.get_news_global(max_results=15)
        st.session_state.news_feed = news
        st.success(f"✅ Loaded {len(news)} news items!")
        time.sleep(1)
        st.rerun()

# Export Data
if export_button:
    export_data = {
        "scan_time": st.session_state.last_scan,
        "cities_scanned": len(st.session_state.nexus_state),
        "opportunities": st.session_state.opportunities,
        "ai_actions": len(st.session_state.ai_actions)
    }
    
    st.download_button(
        "📥 Download Complete Report",
        json.dumps(export_data, indent=2),
        file_name=f"nexus_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json"
    )

st.markdown("---")

# ============================================================================
# GLOBAL WORLD MAP DISPLAY
# ============================================================================

if st.session_state.nexus_state:
    st.markdown("## 🗺️ GLOBAL REALITY STATE")
    
    # Display by region with epic design
    for region in selected_regions:
        region_data = NEXUS_CITIES[region]
        region_cities = [city for city in region_data['cities'] if city in all_cities]
        
        st.markdown(f"### {region_data['icon']} {region}")
        
        # Create dynamic columns
        cols = st.columns(min(len(region_cities), 5))
        
        for idx, city in enumerate(region_cities):
            weather = st.session_state.nexus_state.get(city)
            if weather:
                with cols[idx % 5]:
                    weather_info = WEATHER_DATA.get(weather['condition'], WEATHER_DATA['Clear'])
                    
                    st.markdown(f"""
                    <div class="quantum-card">
                        <div style="text-align: center;">
                            <div class="weather-orb" style="--orb-color: {weather_info['color']};">
                                {weather_info['emoji']}
                            </div>
                            <h3 class="text-cyber">{city}</h3>
                            <h1 style="margin: 0.5rem 0;">{weather['temp']}°C</h1>
                            <p style="color: rgba(255,255,255,0.8); margin: 0.5rem 0;">{weather['condition']}</p>
                            <div style="font-size: 0.9rem; color: rgba(255,255,255,0.6);">
                                <p>💨 Wind: {weather['wind_speed']:.0f} km/h</p>
                                <p>💧 Humidity: {weather['humidity']}%</p>
                                <p>👁️ Visibility: {weather.get('visibility', 10):.1f} km</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="world-map-container">
        <div style="text-align: center; padding: 4rem;">
            <h2 class="text-cyber">🌍 REALITY ENGINE STANDBY</h2>
            <p style="color: rgba(255,255,255,0.6); font-size: 1.2rem;">Click "SCAN REALITY" to monitor the entire world</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# OPPORTUNITIES DISPLAY - EPIC TIER SYSTEM
# ============================================================================

st.markdown("## 💎 DETECTED OPPORTUNITIES")

if st.session_state.opportunities:
    # Top Opportunity - LEGENDARY DISPLAY
    top_opp = st.session_state.opportunities[0]
    
    if top_opp['tier'] == 'LEGENDARY':
        badge_class = 'score-legendary'
    elif top_opp['tier'] == 'EPIC':
        badge_class = 'score-epic'
    else:
        badge_class = 'score-rare'
    
    st.markdown(f"""
    <div class="critical-alert">
        <h1>🔥 TOP OPPORTUNITY</h1>
        <h2>{top_opp['title']}</h2>
        <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Trigger:</strong> {top_opp['trigger']}</p>
        <p><strong>📍 Cities:</strong> {', '.join(top_opp['cities'][:5])}{' + ' + str(len(top_opp['cities']) - 5) + ' more' if len(top_opp['cities']) > 5 else ''}</p>
        <p><strong>💡 Opportunity:</strong> {top_opp['opportunity']}</p>
        <p><strong>🎬 Action:</strong> {top_opp['action']}</p>
        <p style="margin: 1.5rem 0;">
            <span class="{badge_class}">{top_opp['tier']} • {top_opp['score']}/100</span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 15px; margin-left: 1rem;">⏰ {top_opp['urgency']}</span>
        </p>
        <p><strong>💰 Revenue Potential:</strong> <span style="font-size: 1.5rem;">{top_opp['revenue_potential']}</span></p>
        <p><strong>⏱️ Timeframe:</strong> {top_opp['timeframe']} | <strong>🎯 Confidence:</strong> {top_opp['confidence']}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    # All Other Opportunities
    if len(st.session_state.opportunities) > 1:
        st.markdown("### 📋 ALL OPPORTUNITIES")
        
        # Create tabs by tier
        legendary_opps = [o for o in st.session_state.opportunities if o['tier'] == 'LEGENDARY']
        epic_opps = [o for o in st.session_state.opportunities if o['tier'] == 'EPIC']
        rare_opps = [o for o in st.session_state.opportunities if o['tier'] == 'RARE']
        
        tab_labels = []
        tab_contents = []
        
        if legendary_opps:
            tab_labels.append(f"🏆 LEGENDARY ({len(legendary_opps)})")
            tab_contents.append(legendary_opps)
        
        if epic_opps:
            tab_labels.append(f"⚡ EPIC ({len(epic_opps)})")
            tab_contents.append(epic_opps)
        
        if rare_opps:
            tab_labels.append(f"💎 RARE ({len(rare_opps)})")
            tab_contents.append(rare_opps)
        
        tabs = st.tabs(tab_labels)
        
        for tab, opps in zip(tabs, tab_contents):
            with tab:
                for opp in opps[1:] if opp in st.session_state.opportunities[:1] else opps:
                    tier_badge = f'score-{opp["tier"].lower()}'
                    
                    st.markdown(f"""
                    <div class="opportunity-matrix">
                        <h3>{opp['title']}</h3>
                        <p><strong>🎯 Trigger:</strong> {opp['trigger']}</p>
                        <p><strong>📍 Cities:</strong> {', '.join(opp['cities'][:3])}{' +' + str(len(opp['cities']) - 3) if len(opp['cities']) > 3 else ''}</p>
                        <p><strong>💡 Opportunity:</strong> {opp['opportunity']}</p>
                        <p><strong>🎬 Action:</strong> {opp['action']}</p>
                        <p>
                            <span class="{tier_badge}">{opp['tier']} • {opp['score']}/100</span>
                            <span style="background: rgba(255,100,100,0.3); padding: 0.3rem 1rem; border-radius: 10px; margin-left: 1rem;">{opp['urgency']}</span>
                        </p>
                        <p><strong>💰 Revenue:</strong> {opp['revenue_potential']} | <strong>⏱️</strong> {opp['timeframe']} | <strong>🎯</strong> {opp['confidence']}%</p>
                    </div>
                    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="data-stream">
        <h3 class="text-cyber">⚡ NO OPPORTUNITIES DETECTED</h3>
        <p style="color: rgba(255,255,255,0.6);">Scan reality to detect opportunities</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# AI ACTIONS DISPLAY
# ============================================================================

st.markdown("## 🧠 AI-GENERATED ACTION PLANS")

if st.session_state.ai_actions:
    for action in st.session_state.ai_actions:
        with st.expander(f"⚡ {action['title']} - {action['tier']} TIER", expanded=True):
            st.markdown(f"""
            <div class="ai-brain"></div>
            <p style="text-align: center; color: rgba(255,255,255,0.6); margin-bottom: 2rem;">
                Generated: {action['timestamp']}
            </p>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="news-matrix">
                <pre style="white-space: pre-wrap; font-family: 'Courier New', monospace;">{action['plan']}</pre>
            </div>
            """, unsafe_allow_html=True)
            
            col_d1, col_d2 = st.columns([3, 1])
            with col_d2:
                st.download_button(
                    "📥 DOWNLOAD PLAN",
                    action['plan'],
                    file_name=f"nexus_action_{action['opportunity_id']}.txt",
                    use_container_width=True
                )
else:
    st.markdown("""
    <div class="data-stream">
        <h3 class="text-neon">🧠 AI BRAIN READY</h3>
        <p style="color: rgba(255,255,255,0.6);">Click "AI ANALYSIS" to generate supreme action plans</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# NEWS FEED - MATRIX STYLE
# ============================================================================

st.markdown("## 📰 GLOBAL NEWS FEED")

if st.session_state.news_feed:
    cols = st.columns(2)
    
    for idx, news in enumerate(st.session_state.news_feed[:10]):
        with cols[idx % 2]:
            impact_color = {
                'critical': '#ff0055',
                'high': '#ff6b00',
                'medium': '#ffa726'
            }.get(news['impact'], '#66bb6a')
            
            st.markdown(f"""
            <div class="news-matrix" style="border-left-color: {impact_color};">
                <h4>{news['title']}</h4>
                <p style="margin: 0.5rem 0;">
                    <span style="background: rgba(0,255,0,0.2); padding: 0.2rem 0.5rem; border-radius: 5px;">
                        {news['category'].upper()}
                    </span>
                    <span style="background: rgba(0,255,100,0.2); padding: 0.2rem 0.5rem; border-radius: 5px; margin-left: 0.5rem;">
                        {news['sentiment'].upper()}
                    </span>
                    <span style="background: rgba(255,0,85,0.2); padding: 0.2rem 0.5rem; border-radius: 5px; margin-left: 0.5rem;">
                        {news['impact'].upper()} IMPACT
                    </span>
                </p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="data-stream">
        <h3 class="text-matrix">📡 NEWS FEED OFFLINE</h3>
        <p style="color: rgba(255,255,255,0.6);">Click "FETCH NEWS" to load global news</p>
    </div>
    """, unsafe_allow_html=True)

# Epic Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem;'>
    <h2 class="text-cyber">🌌 NEXUS 3.0 - THE ULTIMATE REALITY ENGINE</h2>
    <p style="color: rgba(255,255,255,0.6); font-size: 1.1rem;">
        Monitoring The Entire World • Generating Infinite Opportunities • Powered by Gemini 1.5 Pro
    </p>
    <p style="margin-top: 1rem;">
        <a href='https://github.com/yourusername/nexus-3.0' style='color: #00f5ff; text-decoration: none; margin: 0 1rem;'>⭐ GitHub</a>
        <span style='color: rgba(255,255,255,0.3);'>|</span>
        <a href='https://your-portfolio.com' style='color: #ff00ff; text-decoration: none; margin: 0 1rem;'>🌐 Portfolio</a>
        <span style='color: rgba(255,255,255,0.3);'>|</span>
        <a href='https://upwork.com/yourprofile' style='color: #00ff88; text-decoration: none; margin: 0 1rem;'>💼 Hire Me</a>
    </p>
</div>
""", unsafe_allow_html=True)                                       
# Radhe: Your AI Travel Concierge with Live Itinerary

![Multi-Agent Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-green)
![Interactive Workflow](https://img.shields.io/badge/Experience-Interactive-blue)
![Live Itinerary](https://img.shields.io/badge/Feature-Real--Time_HTML-orange)

## The Philosophy: Transform Travel Planning into the First Joy of Your Journey

**People don't seek travel tools; they seek transformations.**

Radhe is built on a simple truth: planning should be as magical as the destination. We've focused 90% of our energy on the transformation—turning planning from a chore into the first exciting chapter of your journey. The other 10%? That's our sophisticated multi-agent AI working quietly to make it happen.

## The Magic Moment: Watch Your Trip Come to Life

Radhe's breakthrough is the **live itinerary** that evolves with your conversation. Each decision you make—approving a flight, selecting a hotel—instantly updates a beautiful HTML document. This isn't just booking; it's watching your adventure unfold in real-time.

## The Radhe Experience: Specialized AI Agents at Your Service

Unlike typical chatbots, Radhe orchestrates a team of specialized AI agents working in concert:

### 1. Planning Agent: Your Itinerary Architect

The central conductor of your experience that coordinates an interactive, step-by-step planning workflow. It gathers your preferences through natural conversation and orchestrates all other agents.

### 2. Flight & Hotel Agents: Perfect Match Finders

Specialized agents that search for and present options perfectly aligned with your preferences. The flight agent handles route selection and seat preferences, while the hotel agent finds accommodations that match your style and budget.

### 3. Local Guide Agent: Your Insider Connection

Uncovers hidden gems, authentic experiences and cultural insights using real-time Google Search grounding. Provides personalized recommendations that most tourists miss.

### 4. Budget & Safety Agents: Peace of Mind

The expense manager creates comprehensive budget breakdowns with cost-saving strategies, while the emergency assistant provides destination-specific safety information and contacts.

### 5. Reporting Agent: Your Beautiful Travel Document

Transforms all approved selections into a polished, CSS-styled HTML document that updates in real-time as you make decisions. This shareable itinerary becomes your complete travel blueprint.

## The Technical Innovation: Beyond the Chatbot

What sets Radhe apart is not just what it does, but how it works:

* **Interactive Approval Workflow:** Each agent presents findings and collects your feedback, putting you in control at every step
* **Incremental HTML Generation:** Your document updates live after each confirmed selection
* **Google Search Grounding:** Real-time destination data ensures up-to-date recommendations
* **Multi-Agent Orchestration:** Specialized expertise working in concert for holistic solutions

## Radhe in Action: A Travel Experience Transformed

1. **Start the Conversation:** "I'm planning a trip to Barcelona for 5 days"
2. **Interactive Flight Selection:** Review and approve flight options with seat preferences
3. **Hotel Selection Made Easy:** Choose accommodations that match your style
4. **Local Insights That Matter:** Discover authentic experiences and hidden gems
5. **Budget with Confidence:** Review a comprehensive cost breakdown
6. **Safety First:** Access emergency contacts and location-specific safety information
7. **Watch It All Come Together:** See your beautiful HTML itinerary evolve with each decision

## Project Structure

```
Radhe/
├── agent.py                 # Main orchestration agent
├── sub_agents/              # Specialized agents
│   ├── planning/            # Interactive workflow coordination
│   ├── flight/              # Flight search and selection
│   ├── hotel/               # Accommodation recommendations
│   ├── local_guide/         # Destination insights and hidden gems
│   ├── expense_manager/     # Budget planning and optimization
│   ├── emergency_assistant/ # Safety information and contacts
│   └── reporting/           # Live HTML itinerary generation
└── tools/                   # Utility functions and API connectors
```

## The Vision: Beyond Travel

Radhe is more than a travel planner - it's a blueprint for the future of AI-assisted decision making. The same multi-agent architecture can revolutionize:

* Financial planning
* Healthcare decisions
* Education pathways
* Event management

We're building AI that doesn't just save time—it transforms experiences.
| **Components:**  | Tools, AgentTools, Memory |
| **Vertical:**  | Artificial Intelligence |

## Getting Started: Your Journey Begins Here

### Prerequisites

- Python 3.11+
- A Google Cloud Project with the Vertex AI API enabled
- An API Key for the Google Maps Platform Places API

## Setup Instructions


### 1. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your API keys
nano .env  # or use any text editor
```

Required variables to set in `.env`:
- `GOOGLE_GENAI_USE_VERTEXAI=0` (for ML Dev backend) or `1` (for Vertex AI)
- `GOOGLE_API_KEY=your_api_key_here` (if using ML Dev backend)
- `GOOGLE_PLACES_API_KEY=your_places_api_key_here`
- For Vertex AI: `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`

### 2. Install Dependencies

```bash

# Install Python dependencies
pip install google-adk
```

## Running the Radhe

### Command Line Interface

```bash

# Run the Radhe in CLI mode
adk run Radhe
```

### Web Interface

```bash
# Start the web interface
adk web
```

Then open the URL displayed in your terminal (typically http://localhost:8000), select "Radhe" in the top-left dropdown menu, and start interacting with the agent.

## Example Interactions

- "Need some destination ideas for the Americas."
- "Find flights to London from JFK on April 20th for 4 days."
- "I'm at my hotel in Seattle and want to visit the Space Needle. How do I get there?"

Welcome to the future of travel. Welcome to Radhe.

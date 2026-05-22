import streamlit as st
import pandas as pd
import json

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LightWork AI Data Platform Blueprint",
    page_icon="🏢",
    layout="wide"
)

# ============================================================
# COMMON STYLES
# ============================================================

st.markdown(
    """
    <style>
        .main-title {
            font-size: 36px;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 18px;
            color: #4b5563;
            margin-bottom: 25px;
        }
        .section-card {
            background-color: #f9fafb;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            margin-bottom: 15px;
        }
        .metric-card {
            background-color: #ffffff;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            text-align: center;
        }
        .flow-box {
            background-color: #eef2ff;
            padding: 14px;
            border-radius: 10px;
            border-left: 5px solid #6366f1;
            font-family: monospace;
            white-space: pre-wrap;
        }
        .small-note {
            color: #6b7280;
            font-size: 14px;
        }
        /* Make full tab row use available width */
        div[data-baseweb="tab-list"] {
            display: flex !important;
            width: 100% !important;
            gap: 6px !important;
            border-bottom: 1px solid #d1d5db !important;
        }

        /* Make each tab share equal width */
        button[data-baseweb="tab"] {
            flex: 1 1 0 !important;
            justify-content: center !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            color: #374151 !important;
            padding: 10px 6px !important;
            margin-right: 0 !important;
            border-radius: 10px 10px 0 0 !important;
            border: 1px solid #d1d5db !important;
            background-color: #ffffff !important;
            white-space: nowrap !important;
        }

        /* Active selected tab */
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #111827 !important;
            background-color: #eef2ff !important;
            border: 1px solid #6366f1 !important;
            border-bottom: 3px solid #6366f1 !important;
        }

        /* Hover effect */
        button[data-baseweb="tab"]:hover {
            background-color: #f3f4f6 !important;
            color: #111827 !important;
            border-color: #9ca3af !important;
        }

        /* Reduce space below tabs */
        div[data-baseweb="tab-panel"] {
            padding-top: 10px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HEADER
# ============================================================

st.markdown('<div class="main-title">LightWork AI Data Platform Blueprint</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Interactive walkthrough for PMS ingestion, real-time communication processing, agentic AI workflows, benchmarking, and scaling.</div>',
    unsafe_allow_html=True
)

# ============================================================
# TABS
# ============================================================
# ============================================================
# HELPER FUNCTIONS
# ============================================================

def render_tab_header(title: str, subtitle: str, css_class: str):
    st.markdown(
        f"""
        <div class="tab-hero {css_class}">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_flow(text: str):
    st.markdown(
        f"""
        <div class="flow-box">
{text}
        </div>
        """,
        unsafe_allow_html=True
    )
tabs = st.tabs([
    "📌 Overview",
    "🔄 PMS Data Ingestion",
    "⚡ Real-Time Processing",
    "🗄️ Schema Design",
    "🤖 AI + Benchmarking",
    "📈 Scaling Strategy",
    "🛠️ Technology Choices"
])

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="highlight-box">
        Pragya's LightWork AI Take-Home Task
    </div>
    """,
    unsafe_allow_html=True
)
# ============================================================
# TAB 1: OVERVIEW
# ============================================================

with tabs[0]:
    st.header("Overview")

    st.markdown(
        """
        This blueprint presents a practical data platform design for importing data from external hospitality and property PMS platforms, processing live communication data, and enabling safe, auditable agentic AI workflows. The design considers both open-source technologies and cloud-managed services, allowing the platform to remain flexible, scalable, and implementation-ready.
        """
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <h4>PMS Ingestion</h4>
                <p>Import tenant, property and tenancy data from legacy and modern PMS platforms.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Real-Time Data</h4>
                <p>Process messages, audio, and call transcripts using event-driven pipelines.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Agentic AI</h4>
                <p>Combine PMS facts with communication context for safe AI decisions.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Scalability</h4>
                <p>Scale APIs, workers, queues, databases, and AI services based on load.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        
# ============================================================
# TAB 2: Q1 PMS INGESTION
# ============================================================

with tabs[1]:
    st.header("Q1 — PMS Data Ingestion Design")

    st.markdown(
        """
        External PMS platforms may expose different integration methods: modern REST APIs, legacy APIs, CSV exports,
        SFTP drops, or webhooks. I would use a connector-based ingestion architecture to isolate source-specific complexity.
        """
    )

    st.subheader("Connector-Based Ingestion Flow")

    st.markdown(
        """
        <div class="flow-box">
External PMS Platform
Modern REST API / Legacy API / CSV / SFTP / Webhook
        ↓
Platform-Specific Connector
        ↓
Raw Payload Storage
        ↓
Validation + Schema Mapping
        ↓
Canonical Tenant / Property / Tenancy Model
        ↓
Operational DB + AI Context Store + Reporting Layer
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Recommended Design Decisions")

    ingestion_df = pd.DataFrame(
        [
            ["Integration pattern", "Connector-based architecture"],
            ["Primary language", "Python"],
            ["API framework", "FastAPI for webhooks and internal APIs"],
            ["Validation", "Pydantic, JSON Schema, Great Expectations, DBT"],
            ["Storage", "PostgreSQL for canonical data, AWS S3 for raw payloads"],
            ["Deployment", "Docker containers on Kubernetes"],
            ["Orchestration", "Airflow/Kubernetes CronJobs for scheduled sync"],
            ["Security", "Encryption, RBAC, secrets manager, PII masking"],
            ["Failure handling", "Retries, dead-letter queue, quarantine tables"],
        ],
        columns=["Area", "Recommendation"]
    )

    st.dataframe(ingestion_df, use_container_width=True)

    st.subheader("Medallion-Style Data Layers")

    medallion_df = pd.DataFrame(
        [
            ["Bronze", "Raw PMS payloads, CSV files, webhook events", "Debugging, replay, audit trail"],
            ["Silver", "Validated tenants, properties, tenancies, contacts", "Clean canonical business entities"],
            ["Gold", "Tenant 360, property timeline, AI-ready views", "Product, AI, analytics and reporting"],
        ],
        columns=["Layer", "Data Stored", "Purpose"]
    )

    st.dataframe(medallion_df, use_container_width=True)

    st.subheader("Example PMS Payload Normalisation")

    col_a, col_b = st.columns(2)

    with col_a:
        st.caption("External PMS Payload")
        raw_payload = {
            "tenantName": "John Smith",
            "mobile": "07123456789",
            "unit": "Flat 2",
            "postcode": "SW1A 1AA",
            "tenancyStatus": "Active"
        }
        st.json(raw_payload)

    with col_b:
        st.caption("Internal Canonical Format")
        canonical_payload = {
            "first_name": "John",
            "last_name": "Smith",
            "phone": "07123456789",
            "flat_number": "Flat 2",
            "postcode": "SW1A 1AA",
            "tenancy_status": "active"
        }
        st.json(canonical_payload)

# ============================================================
# TAB 3: Q2 REAL-TIME PIPELINE
# ============================================================

with tabs[2]:
    st.header("Q2 — Real-Time Messages, Audio and Transcript Processing")

    st.markdown(
        """
        For live communication data, I would enhance the platform with an event-driven architecture.
        The goal is to accept events quickly, store them safely, and process them asynchronously through workers.
        """
    )

    st.subheader("Real-Time Event Flow")

    st.markdown(
        """
        <div class="flow-box">
Email / WhatsApp / Phone / Web Chat
        ↓
Webhook API / Ingress Service
        ↓
Kafka / SQS
        ↓
Python Processing Workers
        ↓
PostgreSQL + AWS S3 + Vector DB
        ↓
AI Agent / Business Rules / Human Escalation
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Message Event Example")

    message_event = {
        "event_type": "message_received",
        "channel": "whatsapp",
        "sender_type": "tenant",
        "message_text": "My boiler is not working and I have no hot water.",
        "received_at": "2026-05-21T10:30:00Z",
        "source": "webhook"
    }

    st.json(message_event)

    st.subheader("Audio Event Example")

    audio_event = {
        "event_type": "call_completed",
        "channel": "phone",
        "audio_uri": "s3://lightwork-calls/call_123.wav",
        "call_started_at": "2026-05-21T10:00:00Z",
        "call_ended_at": "2026-05-21T10:08:00Z",
        "transcription_status": "pending"
    }

    st.json(audio_event)

    st.subheader("Processing Steps")

    realtime_steps = pd.DataFrame(
        # [
        #     [1, "Receive event", "Webhook API receives message/call/audio event"],
        #     [2, "Store raw event", "Persist raw payload for audit and replay"],
        #     [3, "Publish to queue", "Send event to Kafka/SQS"],
        #     [4, "Process asynchronously", "Workers classify, clean, transcribe and enrich"],
        #     [5, "Link to PMS data", "Match tenant, property and tenancy"],
        #     [6, "AI processing", "Retrieve context and decide action"],
        #     [7, "Audit action", "Store AI decision, response and escalation status"],
        # ],
        # columns=["Step", "Stage", "Description"]
        [
            ["Receive event", "Webhook API receives message/call/audio event"],
            ["Store raw event", "Persist raw payload for audit and replay"],
            ["Publish to queue", "Send event to Kafka/SQS"],
            ["Process asynchronously", "Workers classify, clean, transcribe and enrich"],
            ["Link to PMS data", "Match tenant, property and tenancy"],
            ["AI processing", "Retrieve context and decide action"],
            ["Audit action", "Store AI decision, response and escalation status"],
        ],
        columns=["Stage", "Description"]
    )

    st.dataframe(realtime_steps, use_container_width=True)

# ============================================================
# TAB 4: Q2 SCHEMA DESIGN
# ============================================================

with tabs[3]:
    render_tab_header(
        "Q2 · Schema Design",
        "A simple relational model for PMS entities, conversations, messages, calls, transcripts, AI actions, and retrieval chunks.",
        "hero-schema"
    )

    st.markdown(
        """
        The schema separates structured PMS data, communication history, audio/transcript records,
        and AI action audit logs.
        """
    )

    schema_tables = {
        "organisations": {
            "Purpose": "Stores customer/property management organisations.",
            "Key columns": "organisation_id, name, status, created_at",
            "Why it matters": "Supports multi-tenant isolation and customer-level governance.",
            "SQL": """
CREATE TABLE organisations (
    organisation_id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
"""
        },

        "source_systems": {
            "Purpose": "Tracks external PMS platforms connected to each organisation.",
            "Key columns": "source_system_id, organisation_id, provider_name, provider_type, status",
            "Why it matters": "Enables source lineage and connector-specific sync tracking.",
            "SQL": """
CREATE TABLE source_systems (
    source_system_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    provider_name TEXT NOT NULL,
    provider_type TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
"""
        },

        "properties": {
            "Purpose": "Stores property and address information.",
            "Key columns": "property_id, organisation_id, source_property_id, address, flat_number, postcode",
            "Why it matters": "Core entity for linking tenants, tenancies, messages and maintenance issues.",
            "SQL": """
CREATE TABLE properties (
    property_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    source_system_id UUID REFERENCES source_systems(source_system_id),
    source_property_id TEXT,
    address_line_1 TEXT,
    address_line_2 TEXT,
    flat_number TEXT,
    city TEXT,
    postcode TEXT,
    country TEXT DEFAULT 'UK',
    normalized_address_key TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE (organisation_id, source_system_id, source_property_id)
);
"""
        },

        "people": {
            "Purpose": "Stores tenant, landlord, guarantor, occupant, or contact details.",
            "Key columns": "person_id, first_name, last_name, email, phone, pii_hash",
            "Why it matters": "Handles personal data carefully while supporting identity resolution.",
            "SQL": """
CREATE TABLE people (
    person_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    source_system_id UUID REFERENCES source_systems(source_system_id),
    source_person_id TEXT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    pii_hash TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE (organisation_id, source_system_id, source_person_id)
);
"""
        },

        "tenancies": {
            "Purpose": "Stores tenancy relationship between people and properties.",
            "Key columns": "tenancy_id, property_id, tenancy_start_date, tenancy_end_date, tenancy_status",
            "Why it matters": "Allows the AI to understand current and historical occupancy.",
            "SQL": """
CREATE TABLE tenancies (
    tenancy_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    source_system_id UUID REFERENCES source_systems(source_system_id),
    source_tenancy_id TEXT,
    property_id UUID NOT NULL REFERENCES properties(property_id),
    tenancy_start_date DATE,
    tenancy_end_date DATE,
    tenancy_status TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE (organisation_id, source_system_id, source_tenancy_id)
);
"""
        },

        "tenancy_people": {
            "Purpose": "Links people to tenancies with relationship types.",
            "Key columns": "tenancy_id, person_id, relationship_type, is_primary_contact",
            "Why it matters": "Supports associated residents, guarantors and primary contacts.",
            "SQL": """
CREATE TABLE tenancy_people (
    tenancy_id UUID NOT NULL REFERENCES tenancies(tenancy_id),
    person_id UUID NOT NULL REFERENCES people(person_id),
    relationship_type TEXT NOT NULL,
    is_primary_contact BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (tenancy_id, person_id, relationship_type)
);
"""
        },

        "conversations": {
            "Purpose": "Groups messages/calls into a case or conversation thread.",
            "Key columns": "conversation_id, property_id, tenancy_id, primary_person_id, channel, status, topic",
            "Why it matters": "Provides conversation-level context for AI and humans.",
            "SQL": """
CREATE TABLE conversations (
    conversation_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    property_id UUID REFERENCES properties(property_id),
    tenancy_id UUID REFERENCES tenancies(tenancy_id),
    primary_person_id UUID REFERENCES people(person_id),
    channel TEXT NOT NULL,
    status TEXT NOT NULL,
    topic TEXT,
    priority TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);
"""
        },

        "messages": {
            "Purpose": "Stores inbound and outbound text-based communications.",
            "Key columns": "message_id, conversation_id, sender_person_id, channel, message_text, raw_payload",
            "Why it matters": "Forms the communication history used by AI and support teams.",
            "SQL": """
CREATE TABLE messages (
    message_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    conversation_id UUID NOT NULL REFERENCES conversations(conversation_id),
    sender_person_id UUID REFERENCES people(person_id),
    direction TEXT NOT NULL,
    channel TEXT NOT NULL,
    message_text TEXT,
    raw_payload JSONB,
    received_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT now()
);
"""
        },

        "calls": {
            "Purpose": "Stores phone/audio call metadata.",
            "Key columns": "call_id, conversation_id, caller_person_id, audio_object_uri, transcription_status",
            "Why it matters": "Connects audio files to conversations and transcription workflows.",
            "SQL": """
CREATE TABLE calls (
    call_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    conversation_id UUID REFERENCES conversations(conversation_id),
    caller_person_id UUID REFERENCES people(person_id),
    audio_object_uri TEXT,
    call_started_at TIMESTAMPTZ,
    call_ended_at TIMESTAMPTZ,
    transcription_status TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);
"""
        },

        "transcript_segments": {
            "Purpose": "Stores transcript text split by speaker and timestamp.",
            "Key columns": "transcript_segment_id, call_id, speaker_label, segment_text, start_seconds, end_seconds",
            "Why it matters": "Makes calls searchable and usable by AI retrieval.",
            "SQL": """
CREATE TABLE transcript_segments (
    transcript_segment_id UUID PRIMARY KEY,
    call_id UUID NOT NULL REFERENCES calls(call_id),
    speaker_label TEXT,
    segment_text TEXT NOT NULL,
    start_seconds NUMERIC,
    end_seconds NUMERIC,
    confidence_score NUMERIC,
    created_at TIMESTAMPTZ DEFAULT now()
);
"""
        },

        "ai_actions": {
            "Purpose": "Stores AI decisions, responses, and audit logs.",
            "Key columns": "ai_action_id, conversation_id, action_type, model_name, prompt_version, confidence_score",
            "Why it matters": "Supports explainability, human review, benchmarking and compliance.",
            "SQL": """
CREATE TABLE ai_actions (
    ai_action_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    conversation_id UUID REFERENCES conversations(conversation_id),
    message_id UUID REFERENCES messages(message_id),
    action_type TEXT NOT NULL,
    model_name TEXT,
    prompt_version TEXT,
    input_context_summary TEXT,
    output_text TEXT,
    confidence_score NUMERIC,
    requires_human_review BOOLEAN DEFAULT false,
    final_status TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);
"""
        },

        "knowledge_chunks": {
            "Purpose": "Stores AI retrieval chunks from messages, transcripts, policies and PMS notes.",
            "Key columns": "chunk_id, source_type, source_id, chunk_text, embedding_model, metadata",
            "Why it matters": "Supports semantic search and RAG workflows.",
            "SQL": """
CREATE TABLE knowledge_chunks (
    chunk_id UUID PRIMARY KEY,
    organisation_id UUID NOT NULL REFERENCES organisations(organisation_id),
    source_type TEXT NOT NULL,
    source_id UUID NOT NULL,
    chunk_text TEXT NOT NULL,
    embedding_model TEXT,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Optional if using PostgreSQL with pgvector
ALTER TABLE knowledge_chunks
ADD COLUMN embedding vector(1536);
"""
        },
    }

    selected_table = st.selectbox(
        "Select a table to inspect",
        list(schema_tables.keys())
    )

    table_info = schema_tables[selected_table]

    st.markdown(f"### {selected_table}")

    st.markdown(
        f"""
        <div class="section-card">
            <p><b>Purpose:</b> {table_info["Purpose"]}</p>
            <p><b>Key columns:</b> {table_info["Key columns"]}</p>
            <p><b>Why it matters:</b> {table_info["Why it matters"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("SQL Definition")

    st.code(table_info["SQL"], language="sql")


# ============================================================
# TAB 5: Q3 AGENTIC AI + BENCHMARKING
# ============================================================

with tabs[4]:
    st.header("Q3 — Agentic AI Usage and Benchmarking")

    st.markdown(
        """
        The agentic AI system should combine structured PMS data with unstructured communication context.
        It should retrieve only relevant data, validate actions through business rules, and escalate uncertain or high-risk cases.
        """
    )

    st.subheader("Agentic AI Workflow")

    st.markdown(
        """
        <div class="flow-box">
Incoming Message / Transcript
        ↓
Intent Classification
        ↓
Tenant + Property Matching
        ↓
Retrieve Structured PMS Facts from PostgreSQL
        ↓
Retrieve Conversation / Policy Context from Vector DB
        ↓
Agent Decision
        ↓
Business Rule Validation
        ↓
Auto Response / Task Creation / Human Escalation
        ↓
Audit Log
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Example Scenario")

    scenario_col1, scenario_col2 = st.columns(2)

    with scenario_col1:
        st.markdown("**Tenant Message**")
        st.info("My boiler has stopped working and I have no hot water.")

    with scenario_col2:
        st.markdown("**Expected AI Behaviour**")
        st.write(
            """
            - Classify intent as maintenance  
            - Detect urgency  
            - Match tenant to property  
            - Retrieve tenancy/property context  
            - Create maintenance task or escalate  
            - Draft a safe response  
            - Log the AI decision  
            """
        )

    st.subheader("Benchmarking Metrics")

    benchmark_df = pd.DataFrame(
        [
            ["Intent classification", "Accuracy, precision, recall, F1"],
            ["Tenant/property matching", "Exact match accuracy"],
            ["RAG retrieval", "Recall@K, MRR, groundedness, context precision"],
            ["AI actions", "Human override rate, false automation rate, false escalation rate"],
            ["Live processing", "P95 latency, queue lag, processing time"],
            ["Business outcome", "Resolution time, tenant satisfaction, automation rate"],
        ],
        columns=["Area", "Metrics"]
    )

    st.dataframe(benchmark_df, use_container_width=True)

    st.subheader("AI Safety Controls")

    controls_df = pd.DataFrame(
        [
            ["Human-in-the-loop", "Escalate low-confidence or sensitive cases"],
            ["Prompt/version tracking", "Track which prompt/model produced each output"],
            ["Business rule validation", "Validate AI action before execution"],
            ["PII minimisation", "Retrieve only necessary tenant/property data"],
            ["Audit logging", "Store input context, action, confidence and final status"],
            ["Evaluation dataset", "Use labelled historical cases for offline benchmarking"],
        ],
        columns=["Control", "Purpose"]
    )

    st.dataframe(controls_df, use_container_width=True)

# ============================================================
# TAB 6: Q4 SCALING PLAN
# ============================================================

with tabs[5]:
    st.header("Q4 — Scaling Plan")

    st.markdown(
        """
        I would scale the platform based on observed bottlenecks and service-level objectives, rather than over-engineering upfront.
        """
    )

    scaling_df = pd.DataFrame(
        [
            ["PMS sync slow", "Sync freshness SLA missed", "Add connector workers, improve incremental sync"],
            ["Queue lag increasing", "Messages waiting too long", "Scale consumers with KEDA/HPA"],
            ["Database slow", "CPU > 70–80%, slow queries", "Indexes, read replicas, partitioning, connection pooling"],
            ["AI latency high", "P95 response too slow", "Caching, smaller models for classification, async processing"],
            ["Vector search slow", "Retrieval latency high", "Move from pgvector to dedicated vector DB"],
            ["Audio backlog", "Transcription queue growing", "Separate transcription worker pool"],
            ["API pressure", "High request latency/error rate", "Autoscale API pods, add rate limiting"],
        ],
        columns=["Bottleneck", "Signal", "Scaling Action"]
    )

    st.dataframe(scaling_df, use_container_width=True)

    st.subheader("Scaling Triggers")

    st.markdown(
        """
        <div class="section-card">
        <ul>
            <li>P95 message processing latency exceeds the target SLA.</li>
            <li>Queue lag grows continuously and consumers cannot catch up.</li>
            <li>PMS data freshness falls behind customer expectations.</li>
            <li>Database CPU remains above 70–80% for a sustained period.</li>
            <li>Transcription backlog delays real-time or near-real-time workflows.</li>
            <li>AI response latency affects user experience.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Kubernetes Scaling Approach")

    st.markdown(
        """
        <div class="flow-box">
Kubernetes Cluster
    ├── API Pods: scale by CPU/request load
    ├── PMS Connector Workers: scale by sync backlog
    ├── Message Consumers: scale by queue lag
    ├── Transcription Workers: scale by audio backlog
    ├── AI Workers: scale by AI task queue depth
    └── Monitoring: AWS CloudWatch, Grafana
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# TAB 7: TECHNOLOGY CHOICES
# ============================================================

with tabs[6]:
    st.header("Technology Choices and Trade-Offs")

    st.markdown(
        """
        The first version should be practical and product-focused. I would use Python services, PostgreSQL,
        AWS S3, an event queue, and Kubernetes. Spark or Databricks can be introduced later if the data volume requires distributed processing.
        """
    )

    tech_df = pd.DataFrame(
        [
            ["Main implementation", "Python", "Good for APIs, connectors, workers, AI/RAG orchestration"],
            ["API layer", "FastAPI", "Lightweight, async-friendly, strong Python ecosystem"],
            ["Operational database", "PostgreSQL", "Good for relational PMS/product data"],
            ["Raw storage", "S3/object storage", "Good for raw payloads, audio, exports, transcripts"],
            ["Event processing", "Kafka / SQS", "Supports asynchronous and real-time processing"],
            ["Vector search", "pgvector initially", "Simple start; can move to Pinecone/Qdrant/Weaviate later"],
            ["Cache", "Redis", "Useful for recent context and fast lookup"],
            ["Deployment", "Docker + Kubernetes", "Scalable deployment and worker orchestration"],
            ["Batch orchestration", "Airflow/CronJobs", "Useful for scheduled PMS syncs"],
            ["Large-scale analytics", "Databricks/Spark later", "Only if large batch/backfill/ML workloads require it"],
        ],
        columns=["Area", "Recommended Choice", "Reason"]
    )

    st.dataframe(tech_df, use_container_width=True)

    # st.subheader("Databricks / Spark Position")

    # st.info(
    #     """
    #     I would not force Databricks or Spark from day one. I would use a Medallion-style architecture logically,
    #     and introduce Spark/Databricks later if data volume, historical backfills, transcript analytics,
    #     or ML feature engineering require distributed processing.
    #     """
    # )

    st.subheader("Final Recommendation")

    st.markdown(
        """
        <div class="flow-box">
Recommended first version:
Python + FastAPI + PostgreSQL + AWS S3 + Queue/Event Bus + Vector DB + Docker + Kubernetes

Future scale option:
Spark / Databricks / Lakehouse for large-scale batch analytics, feature engineering and historical processing
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
# st.markdown(
#     """
#     <span class="small-note">
#     Prepared as an interactive companion to the written LightWork AI Data Engineer take-home assessment.
#     </span>
#     """,
#     unsafe_allow_html=True
# )
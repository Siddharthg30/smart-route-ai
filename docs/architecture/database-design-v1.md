# SmartRoute AI
# Database Design v1

Version: 1.0

Status: Draft

Author: Siddharth Gupta

---

# 1. Objective

This document defines the initial database design for the SmartRoute AI backend.

The goal is to create a scalable database architecture capable of supporting:

- AI-based traffic signal optimization
- Edge AI + Server AI
- Time-based fallback
- Manual override
- Traffic analytics
- Multi-city deployment
- Future microservice architecture

---

# 2. Database Technology

Database: PostgreSQL

Reason:

- ACID compliant
- Excellent relational support
- JSONB support
- GIS support (PostGIS)
- Mature ecosystem
- Enterprise ready

---

# 3. Primary Key Strategy

Every table will use UUID as the primary key.

Example

550e8400-e29b-41d4-a716-446655440000

Reason:

- Globally unique
- Secure
- Microservice friendly
- Distributed system friendly

---

# 4. Audit Fields

Every table will contain:

- id
- created_at
- updated_at
- deleted_at

Future:

- created_by
- updated_by

---

# 5. Soft Delete Strategy

Instead of deleting rows permanently:

DELETE ❌

We use:

deleted_at = timestamp

Benefits:

- Data recovery
- Audit history
- Compliance
- Analytics

---

# 6. Main Entities

The system consists of the following entities.

Intersection

↓

Signal

↓

Camera

↓

Edge Device

↓

AI Decision

↓

Manual Override

↓

Vehicle Count

---

# 7. Entity Relationship

Intersection

├── Signals

├── Cameras

├── Edge Device

├── AI Decisions

└── Manual Overrides

---

# 8. Intersection

Purpose

Represents a physical road junction.

Fields

- id
- name
- city
- latitude
- longitude
- status
- operating_mode
- created_at
- updated_at
- deleted_at

Relationships

One Intersection

↓

Many Signals

↓

Many Cameras

↓

Many AI Decisions

↓

Many Manual Overrides

---

# 9. Signal

Purpose

Represents one traffic signal.

Fields

- id
- intersection_id
- direction
- current_signal
- remaining_time
- created_at
- updated_at

Relationship

Many Signals

↓

Belong to one Intersection

---

# 10. Camera

Purpose

Traffic monitoring camera.

Fields

- id
- intersection_id
- camera_name
- stream_url
- fps
- status
- last_heartbeat

Relationship

Many Cameras

↓

Belong to one Intersection

---

# 11. Edge Device

Purpose

Represents the physical AI device installed at an intersection.

Fields

- id
- intersection_id
- device_name
- status
- model_version
- last_heartbeat

Relationship

One Edge Device

↓

Belongs to one Intersection

---

# 12. AI Decision

Purpose

Stores every AI prediction.

No prediction is overwritten.

Fields

- id
- intersection_id
- vehicle_count
- traffic_density
- confidence
- recommended_green_time
- decision_source
- created_at

Relationship

Many Decisions

↓

Belong to one Intersection

---

# 13. Manual Override

Purpose

Stores manual intervention performed by traffic police.

Fields

- id
- intersection_id
- operator
- reason
- start_time
- end_time

Relationship

Many Overrides

↓

Belong to one Intersection

---

# 14. Enumerations

IntersectionStatus

- ACTIVE
- INACTIVE
- MAINTENANCE

OperatingMode

- EDGE_AI
- SERVER_AI
- TIME_BASED
- MANUAL

SignalState

- RED
- YELLOW
- GREEN

CameraStatus

- ONLINE
- OFFLINE

DeviceStatus

- ONLINE
- OFFLINE

DecisionSource

- EDGE_AI
- SERVER_AI
- TIME_BASED

---

# 15. Naming Convention

Tables

snake_case

Example

intersection

signal

camera

Columns

snake_case

Primary Key

id

Foreign Key

intersection_id

Timestamps

created_at

updated_at

deleted_at

---

# 16. Index Strategy (Initial)

Primary Keys

UUID

Indexes

intersection.name

intersection.city

camera.status

edge_device.status

ai_decision.created_at

---

# 17. Future Tables

The following tables are intentionally postponed.

- users
- roles
- permissions
- notification
- mqtt_messages
- event_logs
- emergency_vehicle
- traffic_history
- model_registry
- analytics

---

# 18. Future Improvements

- PostGIS
- TimescaleDB
- Table partitioning
- Read replicas
- Event sourcing
- Distributed tracing
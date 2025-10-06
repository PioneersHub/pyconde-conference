---
title: Task Completion Policy 
icon: fontawesome/solid/list-check
---
# Task Completion Policy

## Overview

Our conference operates through a collaborative model where **Committees** (volunteers) and the **Office** work together to ensure all necessary tasks are completed. While our committees are staffed by dedicated volunteers, certain tasks—especially post-conference activities—are critical to our operations and must be completed regardless of volunteer availability.

## How It Works

### Task Assignment
- Tasks are initially assigned to the appropriate **Committee**
- Committees consist of volunteers who generously donate their time and expertise
- Clear expectations and deadlines are communicated when tasks are assigned

### Follow-up Process
If a task isn't completed by the deadline, the **Office** will:
1. Send a **first reminder** to the committee
2. If needed, send a **second and final reminder**
3. After two reminders with no volunteer pickup, the task enters our decision process

### Decision Framework
When no committee volunteer takes on a task after two reminders, the Office evaluates:

#### Essential Tasks
Tasks critical to conference operations or legal/financial obligations are **automatically moved to the Office** for completion.

#### Non-Essential Tasks
For other tasks, we consider:
- **Available capacity**: Does the Office have bandwidth?
- **Budget**: Are there funds available if external help is needed?

**If yes to both**: Task moves to Office for completion  
**If no**: Task is dropped from the current cycle

## Why This Policy Matters

This policy ensures:
- **Reliability**: Critical tasks always get completed
- **Respect for volunteers**: No endless pressure on busy volunteers
- **Resource management**: Office capacity is used strategically
- **Transparency**: Everyone knows what to expect

## Communication
- All task assignments include clear deadlines and context
- Reminders are sent in a supportive, non-pressuring tone
- Decisions about task transfers are communicated to relevant committees
- We always appreciate volunteer efforts, regardless of availability

### Graph of the process

``` mermaid

flowchart TD
    subgraph Office ["🏢 Office"]
        D[Send Reminder]
        E{Reminder Count = 2?}
        G{Essential Task?}
        H[Complete Task]
        I{Capacity?}
    end
    
    subgraph Committee ["👥 Committee"]
        A[Task Assigned]
        F{Volunteer Takes Task?}
    end
    
    A --> B{Task Done?}
    B -->|Yes| C[✅ Complete]
    B -->|No| D
    
    D --> E
    E -->|No| F
    F -->|Yes| C
    F -->|No| D
    
    E -->|Yes| G
    G -->|Yes| H
    G -->|No| I
    
    I -->|Yes| H
    I -->|No| J[❌ Drop Task]

    
    H --> C
    
    style A fill:#e1f5fe
    style B fill:#f0f0f0
    style C fill:#c8e6c9
    style D fill:#fff3e0
    style H fill:#fff3e0
    style J fill:#ffcdd2
```


*This policy helps us maintain our conference quality while respecting the voluntary nature of committee participation.*
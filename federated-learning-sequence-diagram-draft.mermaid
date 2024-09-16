sequenceDiagram
    participant Server as Flower Server
    participant Strategy as FedAvg Strategy
    participant Client1 as Flower Client 1
    participant Client2 as Flower Client 2
    participant Model as ALBERT Model
    participant Dataset as Dataset Module

    Server->>Strategy: Initialize
    Server->>Client1: Select for round
    Server->>Client2: Select for round
    Client1->>Dataset: Load local data
    Client2->>Dataset: Load local data
    Server->>Client1: Send global model
    Server->>Client2: Send global model
    Client1->>Model: Update local model
    Client2->>Model: Update local model
    Client1->>Model: Train on local data
    Client2->>Model: Train on local data
    Client1->>Server: Send updated model
    Client2->>Server: Send updated model
    Server->>Strategy: Aggregate models
    Strategy->>Server: Return aggregated model
    Server->>Client1: Evaluate global model
    Server->>Client2: Evaluate global model
    Client1->>Server: Send evaluation metrics
    Client2->>Server: Send evaluation metrics
    Server->>Server: Log results

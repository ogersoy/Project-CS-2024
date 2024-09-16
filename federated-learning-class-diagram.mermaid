classDiagram
    class FlowerServer {
        -strategy: FedAvgStrategy
        -model: ALBERTModel
        +start_server()
        +fit()
        +evaluate()
    }
    class FedAvgStrategy {
        -fraction_fit: float
        -fraction_evaluate: float
        -min_fit_clients: int
        -min_evaluate_clients: int
        -min_available_clients: int
        +configure_fit()
        +aggregate_fit()
        +configure_evaluate()
        +aggregate_evaluate()
        +update_global_model()
    }
    class FlowerClient {
        -model: ALBERTModel
        -dataset: Dataset
        +get_parameters()
        +fit()
        +evaluate()
    }
    class ALBERTModel {
        -config: ALBERTConfig
        -parameters: dict
        +forward()
        +backward()
        +update_parameters()
    }
    class Dataset {
        -data: list
        -partition: dict
        +load_data()
        +get_partition()
        +preprocess()
    }
    class Evaluator {
        +calculate_metrics()
        +generate_report()
    }
    class Logger {
        +log_training_progress()
        +log_evaluation_results()
    }

    FlowerServer "1" -- "1" FedAvgStrategy : uses
    FlowerServer "1" -- "1..*" FlowerClient : coordinates
    FlowerServer "1" -- "1" ALBERTModel : manages
    FlowerClient "1" -- "1" ALBERTModel : trains
    FlowerClient "1" -- "1" Dataset : uses
    FlowerServer "1" -- "1" Evaluator : uses
    FlowerServer "1" -- "1" Logger : uses
    FedAvgStrategy -- Evaluator : uses

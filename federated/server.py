
# import flwr as fl
# from typing import List, Tuple

# # Custom strategy with manual accuracy aggregation
# class SaveMetricsStrategy(fl.server.strategy.FedAvg):
#     def __init__(self):
#         super().__init__()
#         self.round_metrics = []

#     def aggregate_evaluate(
#         self,
#         rnd: int,
#         results: List[Tuple],
#         failures: List
#     ) -> Tuple[float, dict]:
#         # Aggregate loss using default
#         aggregated_loss, _ = super().aggregate_evaluate(rnd, results, failures)

#         # Manually compute average accuracy from all clients
#         accuracies = []
#         # for _, _, metrics in results:
#         for _, eval_res in results:
#             if "accuracy" in eval_res.metrics:
#                 accuracies.append(eval_res.metrics["accuracy"])

#         if accuracies:
#             avg_acc = sum(accuracies) / len(accuracies)
#             print(f"Round {rnd} aggregated accuracy: {avg_acc:.4f}")
#             self.round_metrics.append((rnd, avg_acc))
#             return aggregated_loss, {"accuracy": avg_acc}
#         else:
#             print(f"Round {rnd} completed, but no accuracy returned.")
#             self.round_metrics.append((rnd, None))
#             return aggregated_loss, {}

# # Launch the Flower server
# def main():
#     strategy = SaveMetricsStrategy()
#     fl.server.start_server(
#         server_address="localhost:8080",
#         config=fl.server.ServerConfig(num_rounds=10),
#         strategy=strategy,
#     )

# if __name__ == "__main__":
#     main()


#rte
import flwr as fl
from typing import List, Tuple
import json  # ✅ Added

# Custom strategy with manual accuracy aggregation
class SaveMetricsStrategy(fl.server.strategy.FedAvg):
    def __init__(self):
        super().__init__()
        self.round_metrics = []

    def aggregate_evaluate(
        self,
        rnd: int,
        results: List[Tuple],
        failures: List
    ) -> Tuple[float, dict]:
        # Aggregate loss using default
        aggregated_loss, _ = super().aggregate_evaluate(rnd, results, failures)

        # Manually compute average accuracy from all clients
        accuracies = []
        for _, eval_res in results:
            if "accuracy" in eval_res.metrics:
                accuracies.append(eval_res.metrics["accuracy"])

        if accuracies:
            avg_acc = sum(accuracies) / len(accuracies)
            print(f"Round {rnd} aggregated accuracy: {avg_acc:.4f}")
            self.round_metrics.append((rnd, avg_acc))
            return aggregated_loss, {"accuracy": avg_acc}
        else:
            print(f"Round {rnd} completed, but no accuracy returned.")
            self.round_metrics.append((rnd, None))
            return aggregated_loss, {}

# Launch the Flower server
def main():
    strategy = SaveMetricsStrategy()

    # ✅ Capture history
    hist = fl.server.start_server(
        server_address="localhost:8080",
        config=fl.server.ServerConfig(num_rounds=10),
        strategy=strategy,
    )

    # ✅ Save metrics after training
    with open("metrics.json", "w") as f:
        json.dump({
            "accuracy": strategy.round_metrics,
            "loss": hist.losses_distributed  # This is a list of (round, loss)
        }, f)

if __name__ == "__main__":
    main()

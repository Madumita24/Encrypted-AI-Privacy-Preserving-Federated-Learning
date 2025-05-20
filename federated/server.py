
# # import flwr as fl
# # import tensorflow as tf
# # from typing import Dict

# # # Define strategy for federated averaging
# # class SaveMetricsStrategy(fl.server.strategy.FedAvg):
# #     def __init__(self):
# #         super().__init__()
# #         self.round_metrics = []

# #     def aggregate_evaluate(
# #         self,
# #         rnd: int,
# #         results,
# #         failures
# #     ) -> float:
# #         aggregated_loss, aggregated_metrics = super().aggregate_evaluate(rnd, results, failures)
# #         if aggregated_metrics is not None:
# #             if "accuracy" in aggregated_metrics:
# #                 print(f"Round {rnd} aggregated accuracy: {aggregated_metrics['accuracy']:.4f}")
# #             else:
# #                 print(f"Round {rnd} completed, but no accuracy metric returned.")

# #             self.round_metrics.append((rnd, aggregated_metrics["accuracy"]))
# #         return aggregated_loss, aggregated_metrics

# # # Launch Flower server
# # def main():
# #     strategy = SaveMetricsStrategy()
# #     fl.server.start_server(
# #         server_address="localhost:8080",
# #         config=fl.server.ServerConfig(num_rounds=10),
# #         strategy=strategy,
# #     )

# # if __name__ == "__main__":
# #     main()


# import flwr as fl
# import tensorflow as tf
# from typing import Dict

# # Define strategy for federated averaging
# class SaveMetricsStrategy(fl.server.strategy.FedAvg):
#     def __init__(self):
#         super().__init__()
#         self.round_metrics = []

#     def aggregate_evaluate(
#         self,
#         rnd: int,
#         results,
#         failures
#     ) -> float:
#         aggregated_loss, aggregated_metrics = super().aggregate_evaluate(rnd, results, failures)
#         if aggregated_metrics is not None:
#             if "accuracy" in aggregated_metrics:
#                 print(f"Round {rnd} aggregated accuracy: {aggregated_metrics['accuracy']:.4f}")
#                 self.round_metrics.append((rnd, aggregated_metrics["accuracy"]))
#             else:
#                 print(f"Round {rnd} completed, but no accuracy metric returned.")
#                 self.round_metrics.append((rnd, None))  # Record None if accuracy is missing
#         return aggregated_loss, aggregated_metrics

# # Launch Flower server
# def main():
#     strategy = SaveMetricsStrategy()
#     fl.server.start_server(
#         server_address="localhost:8080",
#         config=fl.server.ServerConfig(num_rounds=10),
#         strategy=strategy,
#     )

# if __name__ == "__main__":
#     main()



import flwr as fl
from typing import List, Tuple

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
        # for _, _, metrics in results:
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
    fl.server.start_server(
        server_address="localhost:8080",
        config=fl.server.ServerConfig(num_rounds=10),
        strategy=strategy,
    )

if __name__ == "__main__":
    main()

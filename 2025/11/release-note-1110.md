
# Title: November 06, 2025 
Link: https://docs.cloud.google.com/release-notes#November_06_2025<br>
# BigQuery
## Announcement
原文: The research paper ARIMA_PLUS: Large-scale, Accurate, Automatic and Interpretable In-Database Time Series Forecasting and Anomaly Detection in Google BigQuery is now publicly available. This paper describes the algorithms behind the `ARIMA_PLUS` and `ARIMA_PLUS_XREG` models for time series forecasting and anomaly detection, and demonstrates the high performance, scalability, explainability, and customizability of the models.

説明: Google BigQueryのデータベース内時系列予測および異常検知モデルである`ARIMA_PLUS`および`ARIMA_PLUS_XREG`に関する研究論文が公開されました。この論文は、これらのモデルの背後にあるアルゴリズムを詳細に記述し、モデルの高性能、スケーラビリティ、説明可能性、およびカスタマイズ性を示しています。これは既存のBigQuery MLの機能に関する学術的な情報提供であり、新たな機能のリリースや変更ではありません。

影響有無: **影響なし**
このリリースは、既存のBigQuery MLで提供されている`ARIMA_PLUS`および`ARIMA_PLUS_XREG`モデルの内部アルゴリズムに関する研究論文が公開されたという「情報提供」です。既存のサービス稼働、設定、API、料金体系、パフォーマンスなどに直接的な変更をもたらすものではありません。したがって、お客様の既存のBigQueryワークロードやサービス運用に直接的な影響はありません。

対処方法: 特に対応は不要です。
BigQuery MLを利用して時系列分析や予測を行っている、あるいは今後行いたいユーザーにとっては、これらのモデルの理論的背景や性能について深く理解するための貴重な情報源となります。関心があれば、公開された論文を参照することが推奨されます。

用語説明:
*   **ARIMA_PLUS / ARIMA_PLUS_XREG**: Google BigQuery MLで利用できる時系列予測および異常検知のための機械学習モデルです。ARIMA（自己回帰移動平均）モデルをベースにGoogleが拡張したもので、`ARIMA_PLUS_XREG`は外部変数（eXogenous REGressors）を考慮できる点が特徴です。
*   **時系列予測 (Time Series Forecasting)**: 過去の一定間隔で収集されたデータ（時系列データ）のパターンを分析し、未来の値を予測する手法です。
*   **異常検知 (Anomaly Detection)**: 通常のパターンから著しく逸脱するデータポイントやイベント（異常値、外れ値）を識別するプロセスです。
*   **BigQuery ML**: Google BigQueryの機能の一つで、SQLクエリを使用してBigQuery内で直接機械学習モデルを構築、トレーニング、評価、デプロイできるサービスです。データ移動なしに機械学習を実行できるため、効率的なデータ分析が可能です。
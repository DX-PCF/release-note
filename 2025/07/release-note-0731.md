
# Title: July 28, 2025 
Link: https://cloud.google.com/release-notes#July_28_2025<br>
# Apigee X
## Announcement
原文: On July 28, 2025, we released an updated version of Apigee (1-15-0-apigee-7).
 > **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.
説明：Apigeeの新しいバージョン1-15-0-apigee-7がリリースされました。本日からロールアウトが開始されており、全てのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまでは、新機能や修正が利用できない場合があります。
影響有無：なし。Apigeeはマネージドサービスであり、バージョンアップは自動的に適用されるため、お客様側での明示的な操作は不要です。
対処方法：特になし。新しい機能や修正が利用可能になるまで、ロールアウトの完了を待機してください。

## Fixed
原文: **422195061** | **Enhanced cache lookup performance.**
説明：キャッシュ参照のパフォーマンスが向上しました。
影響有無：なし。パフォーマンス改善であり、既存の動作に悪影響はありません。
対処方法：特になし。

## Fixed
原文: **269573358** | **Resolved issue with OASValidation policy schema references for parameters without body validation** The OASValidation policy correctly resolves and validates schemas passed by reference (`$ref`) for header, path, and query parameters, even when the <ValidateMessageBody> flag is set to `false`.
説明：`OASValidation`ポリシーにおいて、リクエストボディの検証（`ValidateMessageBody`フラグが`false`の場合）が行われない設定でも、ヘッダー、パス、クエリパラメータのスキーマ参照（`$ref`）が正しく解決され、検証されるようになりました。以前の不具合が修正されています。
影響有無：なし。バグ修正であり、ポリシーが期待通りに動作するようになるため、既存の動作に悪影響はありません。
対処方法：特になし。
用語説明：
*   `OASValidation policy`: OpenAPI Specification (OAS) に基づいてAPIリクエストやレスポンスを検証するApigeeのポリシーです。
*   `$ref`: OpenAPI Specification内で定義されたスキーマやコンポーネントを再利用するための参照メカニズムです。

## Fixed
原文: **421141062** | **Increased OAS validation limit to 20MB in JSON payloads to prevent validation failures.**
説明：JSONペイロードにおけるOAS検証のサイズ上限が20MBに引き上げられました。これにより、大規模なJSONペイロードでの検証失敗が減少します。
影響有無：なし。上限緩和であり、既存の動作に悪影響はありません。
対処方法：特になし。

## Fixed
原文: **417200603** | **Improved API connection stability to prevent premature timeouts for long-running requests.**
説明：API接続の安定性が向上し、長時間実行されるリクエストにおいて発生していた早期タイムアウトが防止されるようになりました。
影響有無：なし。安定性向上であり、既存の動作に悪影響はありません。
対処方法：特になし。

## Fixed
原文: **423597917** | **`POST` operations for AppGroupApp keys updated** `POST` operations for AppGroup app keys now insert scopes and attributes instead of appending these values. This behavior is consistent with `POST` operations for companies in Apigee Edge for Public Cloud.
説明：`AppGroupApp`キーに対する`POST`操作において、スコープと属性が「追加 (append)」ではなく「挿入 (insert)」されるように動作が変更されました。この新しい挙動は、Apigee Edge for Public Cloudの会社（companies）に対する`POST`操作の挙動と一貫性を持つようになります。
影響有無：あり。`AppGroupApp`キーの`POST`操作を利用している場合、スコープや属性が単純に追記されることを期待していたシステムでは、挙動が変わる可能性があります。挿入（insert）の具体的な挙動（例：既存の値を上書きするか、ユニークなものとして追加するか）によっては、既存のロジックに影響が出る可能性があります。
対処方法：`AppGroupApp`キーに対する`POST`操作を利用している場合、この変更が既存のワークフローに与える影響を確認し、必要に応じてテストを実施してください。特に、スコープや属性の管理方法に意図しない変更がないか検証が必要です。
用語説明：
*   `AppGroupApp keys`: Apigeeの機能で、開発者アプリをグループ化し、APIアクセスを管理するためのキーです。
*   `scopes`: APIアクセス権限を定義する識別子です。
*   `attributes`: アプリケーションやAPIプロダクトに関連付けられるカスタムデータです。

## Fixed
原文: **390234048** | **Resolved issue resulting in missing fields in API responses for Monetization rate plans** The `createdAt` and `lastModifiedAt` fields are now present in responses from the `organizations.apiproducts.rateplans` API.
説明：収益化レートプランのAPIレスポンスにおいて、`createdAt`と`lastModifiedAt`フィールドが欠落する問題が修正されました。これにより、これらのフィールドがAPIレスポンスに正しく含まれるようになります。
影響有無：なし。バグ修正であり、情報が正しく返されるようになるため、既存のシステムに悪影響はありません。これらのフィールドに依存するロジックがある場合、以前は値が取得できませんでしたが、今後は取得できるようになります。
対処方法：特になし。
用語説明：
*   `Monetization rate plans`: Apigeeの収益化機能の一部で、API利用に対する料金体系を定義するプランです。

## Fixed
原文: **422757662** | **Reverted problematic commit regarding X-b3 trace headers send when using distributed tracing.**
説明：分散トレースを使用する際に`X-b3`トレースヘッダーの送信に関する問題を引き起こしていたコミットが元に戻されました。
影響有無：なし。以前の不具合が解消され、正常な動作に戻るため、既存の動作に悪影響はありません。
対処方法：特になし。
用語説明：
*   `Distributed tracing`: 複数のサービスにまたがるリクエストのフローを追跡し、パフォーマンスの問題特定などに役立てる技術です。`X-b3`ヘッダーは、OpenTracingやZipkinなどで使用されるトレーシングコンテキスト伝播のためのHTTPヘッダーの一種です。

## Fixed
原文: **N/A** | **Updates to security infrastructure and libraries.**
説明：セキュリティインフラストラクチャとライブラリが更新されました。
影響有無：なし。セキュリティ強化であり、既存の機能動作に直接的な影響はありません。
対処方法：特になし。

# BigQuery
## Libraries
### Node.js
原文: - Remove `is` package as dependency (#1500) (926c9f8)
説明：Node.js用BigQueryクライアントライブラリ（`@google-cloud/bigquery`）バージョン8.1.1において、`is`パッケージへの依存関係が削除されました。
影響有無：なし。ライブラリの内部的な依存関係の変更であり、ユーザーコードに直接的な影響はありません。セキュリティ改善やバンドルサイズの削減に寄与する可能性があります。
対処方法：利用しているNode.jsクライアントライブラリのバージョンを最新に更新することを検討してください。

### Python
原文: - Specify the inherited-members directive for job classes (#2244) (d207f65)
説明：Python用BigQueryクライアントライブラリ（`google-cloud-bigquery`）バージョン3.35.1において、ジョブクラスに対する`inherited-members`ディレクティブが指定されました。これは主にドキュメント生成に関する変更と推測されます。
影響有無：なし。ライブラリのドキュメント生成に関連する変更であり、ユーザーコードに直接的な影響はありません。
対処方法：利用しているPythonクライアントライブラリのバージョンを最新に更新することを検討してください。

# Cloud Composer
## Fixed
原文: Fixed an issue that caused unexpected restarts of Airflow component workloads in the environment's cluster.
説明：Cloud Composer環境のクラスタ内で、Airflowコンポーネントのワークロードが予期せず再起動する問題が修正されました。
影響有無：なし。Airflowコンポーネントの安定性向上につながる修正であり、既存の運用に悪影響はありません。
対処方法：環境のバージョンがこの修正を含むように更新されるのを待つか、環境のアップデートを検討してください。
用語説明：
*   `Airflow component workloads`: Apache Airflow環境を構成する様々なサービス（Scheduler, Webserver, Workerなど）が動作するワークロードです。

## Fixed
原文: *(Cloud Composer 3)* The `DAGS_FOLDER` reserved environment variable now correctly points to the local directory where DAG files are stored.
説明：(Cloud Composer 3のみ) `DAGS_FOLDER`という予約済みの環境変数が、DAGファイルが保存されているローカルディレクトリを正しく指すようになりました。
影響有無：なし。現在ご利用中の環境はCloud Composer 2であるため、この変更は適用されません。
対処方法：なし。
用語説明：
*   `DAGS_FOLDER`: Apache AirflowでDAG（Directed Acyclic Graph）ファイルが配置されるディレクトリを示す環境変数です。

## Changed
原文: New Airflow builds are available in Cloud Composer 3:
- composer-3-airflow-2.10.5-build.10 (default)
- composer-3-airflow-2.9.3-build.30
説明：Cloud Composer 3向けに新しいAirflowビルドが利用可能になりました。具体的には、`composer-3-airflow-2.10.5-build.10`（デフォルト）と`composer-3-airflow-2.9.3-build.30`です。
影響有無：なし。現在ご利用中の環境はCloud Composer 2であるため、この変更は適用されません。
対処方法：なし。

## Changed
原文: New images are available in Cloud Composer 2:
- composer-2.13.8-airflow-2.10.5 (default)
- composer-2.13.8-airflow-2.9.3
説明：Cloud Composer 2向けに新しいイメージが利用可能になりました。具体的には、`composer-2.13.8-airflow-2.10.5`（デフォルト）と`composer-2.13.8-airflow-2.9.3`です。
影響有無：あり。現在ご利用中の環境はComposer version 2.7.1、Airflow version 2.7.3です。新しいイメージではAirflowのバージョンが2.9.3または2.10.5に更新されており、メジャー・マイナーバージョンアップに伴うDAGの互換性、Operatorの変更、APIの変更などが発生する可能性があります。
対処方法：
*   現在の環境（Composer 2.7.1, Airflow 2.7.3）から新しいイメージ（Airflow 2.9.3または2.10.5）へアップグレードする計画を立案してください。
*   アップグレード前に、新しいAirflowバージョンにおけるDAGの互換性（特にカスタムOperatorや利用中のライブラリ）を確認し、Airflowのリリースノートを精査してください。
*   可能であれば、ステージング環境などで新しいイメージにアップグレードし、既存のDAGが問題なく動作することを確認してから本番環境へ適用してください。
*   Cloud Composer環境の更新手順に従い、計画的にアップグレードを実施してください。
用語説明：
*   `Cloud Composer image`: Cloud Composer環境の基盤となるDockerイメージです。これには特定のバージョンのApache Airflow、Pythonライブラリなどが含まれます。

## Deprecated
原文: Cloud Composer version 2.8.6 has reached its end of support period.
説明：Cloud Composerバージョン2.8.6がサポート終了期間に達しました。
影響有無：なし。現在ご利用中の環境はCloud Composer 2.7.1であるため、この告知による直接的な影響はありません。
対処方法：なし。

# Google Kubernetes Engine
## Announcement
原文: Starting in May, 2025, Google is performing maintenance on the internal control plane datastore for all GKE clusters to improve scalability and reliability. We expect to complete these improvements across GKE by October, 2025.
This maintenance is happening gradually across all GKE clusters, and will occur in your clusters only during configured maintenance windows. The maintenance process is expected to take approximately 15 minutes to complete during your cluster's maintenance window.
**Expected impact**
During the internal control plane datastore maintenance, the **Kubernetes API server will be unavailable for 15 minutes**, regardless of whether you use a regional cluster or a zonal cluster. During this 15-minute period, you won't be able to interact with the Kubernetes API server for your cluster.
Consider the following potential disruptions to your normal workflows during the maintenance window for your cluster:
- **Kubernetes API unavailability**: you can't use the `kubectl` tool or any other Kubernetes API client to issue commands to the control plane, regardless of whether the cluster is regional or zonal. Attempts to deploy, modify, or query resources by using the Kubernetes API will fail during this period.
- **Halted deployments:** automated deployment pipelines (CI/CD) that interact with the Kubernetes API will fail to complete tasks such as deploying or updating applications in the cluster.
- **Google Cloud console limitations**: operations for the cluster in the Google Cloud console that communicate with the Kubernetes API might fail during the maintenance period.
- **Delayed control plane automation**: features that are managed by the control plane, such as the cluster autoscaler, Horizontal or Vertical Pod Autoscaling adjustments, or some node auto-repair operations might be paused until the API server is online.
The following resources have no expected impact during the maintenance period:
- **Running applications**: any running applications and services on your nodes should continue to function without interruptions.
- **Node pool operations**: existing nodes should remain connected and operational.
- **Network traffic**: traffic in the data plane, such as traffic to and from your running workloads, shouldn't be affected.
**What you need to do**
No action is required from you for the maintenance to occur. To plan for this maintenance, we recommend that you do the following:
- **Review maintenance windows**: review your cluster's maintenance window and exclusions settings and schedule maintenance windows during periods that minimize disruptions to your normal workflows.
- **Plan for Kubernetes API unavailability**: if you run critical operations in your cluster that require access to the Kubernetes API, avoid scheduling these operations during maintenance windows.
説明：2025年5月から10月にかけて、GKEクラスタの内部コントロールプレーンデータストアのメンテナンスが
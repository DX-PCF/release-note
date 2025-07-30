
# Title: July 28, 2025 
Link: https://cloud.google.com/release-notes#July_28_2025<br>
以下に、Google Cloud リリースノートの製品・アナウンス単位での影響調査結果を記載します。

# Apigee X
## Announcement
原文: On July 28, 2025, we released an updated version of Apigee (1-15-0-apigee-7).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.
説明: Apigeeの新しいバージョン (1-15-0-apigee-7) がリリースされました。このリリースはロールアウト中であり、全てのGoogle Cloudゾーンに適用されるまで数営業日かかる可能性があります。
影響有無: 影響なし。
理由: このリリースは自動的に適用されるため、ユーザー側での手動対応は不要です。新機能や修正が環境に適用されるまで数日かかる可能性がある点のみ留意が必要です。
対処方法: なし。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **422195061** | **Enhanced cache lookup performance.** |
説明: キャッシュの参照パフォーマンスが向上しました。
影響有無: ポジティブな影響。
理由: Apigee Xでキャッシュ機能を利用している場合、APIレスポンスのレイテンシが改善される可能性があります。
対処方法: なし。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **269573358** | **Resolved issue with OASValidation policy schema references for parameters without body validation** The OASValidation policy correctly resolves and validates schemas passed by reference (`$ref`) for header, path, and query parameters, even when the <ValidateMessageBody> flag is set to `false`. |
説明: `OASValidation` ポリシーにおいて、メッセージボディの検証が無効（`<ValidateMessageBody>` フラグが `false`）な場合でも、ヘッダー、パス、クエリパラメータのスキーマ参照 (`$ref`) が正しく解決され、検証されるようになりました。
影響有無: ポジティブな影響。
理由: `OASValidation` ポリシーでこの問題に遭遇していた場合、ポリシーが期待通りに動作するようになります。これにより、APIの入力検証の堅牢性が向上します。
対処方法: なし。
用語説明:
*   **OASValidation policy**: OpenAPI Specification (OAS) に基づいてAPIリクエストやレスポンスを検証するApigeeのポリシーです。
*   **$ref**: JSON Schemaなどで、他のスキーマ定義を参照するために使用されるキーワードです。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **421141062** | **Increased OAS validation limit to 20MB in JSON payloads to prevent validation failures.** |
説明: JSONペイロードのOAS検証におけるサイズ制限が20MBに引き上げられました。これにより、大きなJSONペイロードの検証が失敗するのを防ぎます。
影響有無: ポジティブな影響。
理由: 大きなJSONペイロードを扱うAPIでOASValidationポリシーを使用している場合、検証失敗のリスクが減少します。
対処方法: なし。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **417200603** | **Improved API connection stability to prevent premature timeouts for long-running requests.** |
説明: 長時間実行されるリクエストにおけるAPI接続の安定性が向上し、早期タイムアウトが防止されるようになりました。
影響有無: ポジティブな影響。
理由: バックエンドサービスへの接続が長時間必要となるAPIリクエストを使用している場合、タイムアウトエラーの発生頻度が減少することが期待されます。
対処方法: なし。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **423597917** | **`POST` operations for AppGroupApp keys updated** `POST` operations for AppGroup app keys now insert scopes and attributes instead of appending these values. This behavior is consistent with `POST` operations for companies in Apigee Edge for Public Cloud. |
説明: `AppGroupApp` キーに対する `POST` 操作の挙動が変更され、スコープと属性の値が「追加 (append)」ではなく「挿入 (insert)」されるようになりました。これは、Apigee Edge for Public Cloudにおける会社 (companies) の `POST` 操作と同じ挙動です。
影響有無: 影響ありの可能性あり。
理由: `AppGroupApp` キーの `POST` 操作を利用しており、そのAPIクライアントがこれまでの「追加」の動作に依存していた場合、予期せぬ結果を引き起こす可能性があります。例えば、既存のスコープや属性が上書きされる、または順序が変更されるといった影響が考えられます。
対処方法: `AppGroupApp` キーの `POST` 操作を使用している場合は、この変更による影響を確認するため、テスト環境で動作検証を実施してください。必要に応じて、APIクライアント側のロジックを修正する必要があります。
用語説明:
*   **AppGroupApp key**: Apigeeでアプリケーションを識別するために使用されるキーです。これには、アプリケーションがアクセスできるAPIプロダクトのスコープやカスタム属性が関連付けられます。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **390234048** | **Resolved issue resulting in missing fields in API responses for Monetization rate plans** The `createdAt` and `lastModifiedAt` fields are now present in responses from the `organizations.apiproducts.rateplans` API. |
説明: マネタイゼーションのレートプランAPI (`organizations.apiproducts.rateplans`) からの応答に、`createdAt`（作成日時）と `lastModifiedAt`（最終更新日時）フィールドが欠落する問題が修正されました。
影響有無: ポジティブな影響。
理由: マネタイゼーション機能を利用しており、レートプランの作成日時や最終更新日時を参照する必要がある場合に、これらの情報がAPI応答に含まれるようになります。
対処方法: なし。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **422757662** | **Reverted problematic commit regarding X-b3 trace headers send when using distributed tracing.** |
説明: 分散トレーシングを使用している場合に、`X-b3` トレースヘッダーの送信に関する問題のあるコミットが元に戻されました。
影響有無: ポジティブな影響。
理由: 分散トレーシング機能の安定性が向上し、`X-b3` ヘッダーを用いたトレースがより正確に行われるようになります。
対処方法: なし。
用語説明:
*   **X-b3 trace headers**: 分散トレーシングシステム（例: Zipkin、OpenTelemetry）で、サービス間のリクエストの流れを追跡するために使用されるHTTPヘッダーのセットです。トレースID、スパンIDなどが含まれます。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **N/A** | **Updates to security infrastructure and libraries.** |
説明: セキュリティインフラストラクチャとライブラリが更新されました。
影響有無: ポジティブな影響。
理由: 基盤となるセキュリティが強化され、全体的なセキュリティ体制が向上します。
対処方法: なし。

# BigQuery
## Libraries
### Node.js
原文: ## Node.js
## Changes for @google-cloud/bigquery
[@google-cloud/bigquery](https://github.com/googleapis/nodejs-bigquery)
[8.1.1](https://github.com/googleapis/nodejs-bigquery/compare/v8.1.0...v8.1.1)
- Remove `is` package as dependency (#1500) (926c9f8)
説明: Node.js用のBigQueryクライアントライブラリ `@google-cloud/bigquery` のバージョン8.1.1がリリースされ、`is` パッケージへの依存関係が削除されました。
影響有無: 影響なし。
理由: 依存関係の削除は通常、ライブラリのフットプリント削減やセキュリティ向上に寄与しますが、既存の機能動作への影響はありません。
対処方法: Node.jsで `@google-cloud/bigquery` ライブラリを使用している場合、可能であれば最新バージョンへの更新を検討しても良いでしょう。

### Python
原文: ## Python
## Changes for google-cloud-bigquery
[google-cloud-bigquery](https://github.com/googleapis/python-bigquery)
[3.35.1](https://github.com/googleapis/python-bigquery/compare/v3.35.0...v3.35.1)
- Specify the inherited-members directive for job classes (#2244) (d207f65)
説明: Python用のBigQueryクライアントライブラリ `google-cloud-bigquery` のバージョン3.35.1がリリースされ、ジョブクラスに対して `inherited-members` ディレクティブが指定されました。
影響有無: 影響なし。
理由: この変更はドキュメント生成に関するものであり、ライブラリの機能的な動作に影響を与えるものではありません。
対処方法: Pythonで `google-cloud-bigquery` ライブラリを使用している場合、可能であれば最新バージョンへの更新を検討しても良いでしょう。

# Cloud Composer
**(現在の環境: Composer version 2.7.1, Airflow version 2.7.3)**

## Fixed
原文: Fixed an issue that caused unexpected restarts of Airflow component workloads in the environment's cluster.
説明: 環境のクラスタ内でAirflowコンポーネントのワークロードが予期せず再起動する問題が修正されました。
影響有無: ポジティブな影響の可能性あり。
理由: 現在のComposer環境でこの問題が発生している場合、安定性が向上することが期待されます。この修正がComposer 2.7.1にバックポートされるか、またはバージョンアップによって解消されます。
対処方法: 現在のComposer環境でAirflowコンポーネントの予期せぬ再起動に遭遇している場合、Cloud Composerのバージョンアップを検討してください。

## Fixed
原文: *(Cloud Composer 3)* The `DAGS_FOLDER` reserved environment variable now correctly points to the local directory where DAG files are stored.
説明: Cloud Composer 3において、予約済みの環境変数 `DAGS_FOLDER` が、DAGファイルが保存されているローカルディレクトリを正しく指すようになりました。
影響有無: 影響なし。
理由: この修正はCloud Composer 3に限定されており、利用中の環境はCloud Composer 2のため対象外です。
対処方法: なし。

## Changed
原文: New Airflow builds are available in Cloud Composer 3:
[Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-2.10.5-build.10 (default)
- composer-3-airflow-2.9.3-build.30
説明: Cloud Composer 3向けに、新しいAirflowビルド（2.10.5および2.9.3）が利用可能になりました。
影響有無: 影響なし。
理由: この変更はCloud Composer 3に限定されており、利用中の環境はCloud Composer 2のため対象外です。
対処方法: なし。

## Changed
原文: New images are available in Cloud Composer 2:
[images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
- composer-2.13.8-airflow-2.10.5 (default)
- composer-2.13.8-airflow-2.9.3
説明: Cloud Composer 2向けに、新しいイメージ（`composer-2.13.8-airflow-2.10.5` および `composer-2.13.8-airflow-2.9.3`）が利用可能になりました。
影響有無: 影響あり。
理由: 現在 `composer-2.7.1-airflow-2.7.3` を使用しているため、利用可能なより新しいComposerおよびAirflowバージョンが提供されたことになります。これらの新しいイメージにアップグレードすることで、最新の機能や修正が利用できるようになります。
対処方法: 新しいComposerイメージへのアップグレードを計画してください。アップグレード前に、新しいAirflowバージョン（2.9.3または2.10.5）でのDAGの互換性、使用しているPythonライブラリの動作、依存パッケージの互換性などを十分に検証することが強く推奨されます。

## Deprecated
原文: Cloud Composer version 2.8.6 has reached its end of support period.
[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support)
説明: Cloud Composerバージョン2.8.6がサポート終了期間に達しました。
影響有無: 間接的な影響あり。
理由: 現在利用中のCloud Composer 2.7.1は、2.8.6よりもさらに古いバージョンであり、将来的にサポート終了となる可能性が高いことを示唆しています。
対処方法: Cloud Composerのバージョンアップ計画を早急に検討し、サポートされている最新バージョンへの移行を進めることを推奨します。

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
説明: 2025年5月から10月にかけて、GKEクラスタの内部コントロールプレーンデータストアのメンテナンスが実施されます。これはスケーラビリティと信頼性を向上させるためのもので、設定されたメンテナンスウィンドウ中に約15分間、Kubernetes APIサーバーが利用できなくなります。この期間中は、`kubectl` コマンド、CI/CDパイプライン、GCPコンソールからのクラスタ操作、オートスケーラーなどが影響を受けますが、稼働中のアプリケーションやノードプール、データプレーンのネットワークトラフィックには影響ありません。
影響有無: 影響あり。
理由: メンテナンスウィンドウ中にKubernetes APIサーバーが約15分間利用不可となるため、この期間にAPIへのアクセスが必要な運用（デプロイ、リソースの更新、監視など）は失敗します。
対処方法:
1.  **メンテナンスウィンドウの確認**: GKEクラスタのメンテナンスウィンドウと除外設定を見直し、業務への影響が最小限となる時間帯に設定してください。
2.  **APIアクセス計画**: Kubernetes APIへのアクセスが必要なクリティカルな操作は、メンテナンスウィンドウ中に実行されないよう計画してください。
用語説明:
*   **コントロールプレーン**: Kubernetesクラスタを管理するコンポーネント群（APIサーバー、スケジューラー、コントローラーマネージャーなど）を指します。
*   **データプレーン**: ワークロードが実際に動作するノードと、その間のネットワーク通信を指します。

## Fixed
原文: A fix is available for an issue in which the Compute Engine Persistent Disk CSI driver failed with an `invalid cpuString` error on GKE nodes that used custom machine types. This issue prevented successful attachment and mounting of Persistent Disk volumes on affected nodes. The fix is available in the following GKE versions:
- 1.31.10-gke.1021000 and later
- 1.32.4-gke.1698000 and later
- 1.33.1-gke.1386000 and later
説明: カスタムマシンタイプを使用するGKEノードにおいて、Compute Engine Persistent Disk CSIドライバが `invalid cpuString` エラーで失敗し、Persistent Diskボリュームのアタッチやマウントができない問題が修正されました。この修正は、上記のGKEバージョンで利用可能です。
影響有無: 条件付きで影響あり。
理由: もし、貴社のGKEクラスタが上記の修正対象バージョンよりも古いバージョンで、かつカスタムマシンタイプを使用しており、Persistent Disk CSIドライバでこの問題に遭遇していた場合、この修正により問題が解決されます。問題に遭遇していない場合や、既に修正バージョンを利用している場合は影響ありません。
対処方法:
1.  現在のGKEクラスタのバージョンと、カスタムマシンタイプを使用しているかを確認してください。
2.  もしこの問題に遭遇している、または将来的な予防策として、記載されているGKEバージョン（1.31.10-gke.1021000以降、1.32.4-gke.1698000以降、1.33.1-gke.1386000以降）にクラスタをアップグレードすることを検討してください。
用語説明:
*   **Compute Engine Persistent Disk CSI driver**: GKEクラスタがCompute Engine Persistent Diskをストレージとして利用するための標準的なインターフェースを提供するドライバです。CSI (Container Storage Interface) は、Kubernetesが様々なストレージシステムと連携するための業界標準です。

# SAP on Google Cloud
## Announcement
原文: **New SAP NetWeaver certification: C4D bare metal machine types**
For use with SAP NetWeaver, SAP has certified the following Compute Engine bare metal machine types: `c4d-standard-384-metal` and `c4d-highmem-384-metal`.
For more information, see the following:
- Certifications for SAP applications on Google Cloud
- C4D machine series
説明: SAP NetWeaver向けに、Compute Engineのベアメタルマシンタイプ `c4d-standard-384-metal` および `c4d-highmem-384-metal` がSAPによって認定されました。
影響有無: 影響なし。
理由: これは新しいリソースタイプが追加されたというアナウンスであり、既存のSAP on Google Cloud環境に直接的な影響を与えるものではありません。将来的にこれらのマシンタイプを検討する際の選択肢が増えます。
対処方法: なし。

# Security Command Center
## Changed
原文: **Model Armor filter updates**
- The prompt injection and jailbreak detection filter now supports 10,000 tokens.
- For the Sensitive Data Protection filter, `SKIP_DETECTION` is returned if the prompt or response exceeds the token limit.
- For all other filters, if the prompt or response exceeds the token limit, `MATCH_FOUND` is returned if malicious content is found, and `SKIP_DETECTION` is returned if no malicious content is found.
説明: Model Armorのフィルター機能が更新されました。
*   プロンプトインジェクションおよびジェイルブレイク検出フィルターが10,000トークンまでサポートされるようになりました。
*   機密データ保護フィルターでは、プロンプトまたはレスポンスがトークン制限を超過した場合に `SKIP_DETECTION` が返されます。
*   その他のフィルターでは、トークン制限を超過した場合でも、悪意のあるコンテンツが見つかれば `MATCH_FOUND`、見つからなければ `SKIP_DETECTION` が返されます。
影響有無: 影響ありの可能性あり。
理由: Model Armorを利用している場合、トークン制限を超過した場合のフィルターの挙動が変更されています。特に、機密データ保護フィルターで `SKIP_DETECTION` が返される条件が明確化されたため、検出ロジックやアラート処理に影響を与える可能性があります。これにより、特定のシナリオで検出漏れや過検知が発生しないか再評価が必要になる場合があります。
対処方法: Model Armorを利用している場合は、このフィルター更新による既存のセキュリティ運用への影響を評価してください。特に、トークン制限を超える可能性のあるプロンプトやレスポンスを処理している場合、その挙動を確認し、必要に応じてセキュリティポリシーやアラートの設定を見直してください。
用語説明:
*   **Model Armor**: 生成AIモデル（LLMなど）に対する脅威（プロンプトインジェクション、ジェイルブレイクなど）から保護するためのSecurity Command Centerの機能です。
*   **プロンプトインジェクション (Prompt Injection)**: 悪意のある入力を
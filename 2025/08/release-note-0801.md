
# Title: July 28, 2025 
Link: https://cloud.google.com/release-notes#July_28_2025<br>
# Apigee X
## Announcement
原文: On July 28, 2025, we released an updated version of Apigee (1-15-0-apigee-7).
 > **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.
説明: Apigeeの新しいバージョン(1-15-0-apigee-7)がリリースされました。このリリースは段階的に展開されるため、全てのGoogle Cloudゾーンで利用可能になるまで数営業日かかる可能性があります。お使いのインスタンスに新機能や修正が適用されるのは、展開が完了した後になります。
影響有無: 影響なし。このアナウンスは、新しいバージョンがリリースされたという情報提供であり、既存環境への直接的な機能変更や不具合を発生させるものではありません。新機能や修正がすぐに適用されない可能性があるという注意喚起です。
対処方法: 特になし。必要に応じて、新機能や修正が適用されたことを確認してください。

## Fixed
### Bug ID: 422195061
原文: **Enhanced cache lookup performance.**
説明: キャッシュルックアップのパフォーマンスが向上しました。
影響有無: 影響なし（ポジティブな影響）。キャッシュの検索性能が向上するため、APIプロキシの応答速度が改善される可能性があります。
対処方法: 特になし。

### Bug ID: 269573358
原文: **Resolved issue with OASValidation policy schema references for parameters without body validation** The OASValidation policy correctly resolves and validates schemas passed by reference (`$ref`) for header, path, and query parameters, even when the <ValidateMessageBody> flag is set to `false`.
説明: OASValidationポリシーにおいて、メッセージボディの検証（`ValidateMessageBody`フラグが`false`）を行わない設定でも、ヘッダー、パス、クエリパラメータに対するスキーマ参照（`$ref`）が正しく解決され、検証されるようになりました。
影響有無: 影響なし（ポジティブな影響）。OASValidationポリシーの機能が正しく動作するようになり、より堅牢なAPI検証が可能になります。この問題に起因する検証エラーや見落としがあった場合に改善されます。
対処方法: 特になし。

### Bug ID: 421141062
原文: **Increased OAS validation limit to 20MB in JSON payloads to prevent validation failures.**
説明: JSONペイロードにおけるOAS検証のサイズ制限が20MBに増加し、大きなペイロードでの検証失敗を防ぎます。
影響有無: 影響なし（ポジティブな影響）。これまで20MB以上のJSONペイロードでOASValidationポリシーを使用していた際に検証失敗していた場合、この変更により問題が解消される可能性があります。
対処方法: 特になし。

### Bug ID: 417200603
原文: **Improved API connection stability to prevent premature timeouts for long-running requests.**
説明: API接続の安定性が向上し、長時間実行されるリクエストでの早期タイムアウトが防止されるようになりました。
影響有無: 影響なし（ポジティブな影響）。特に長時間の処理を伴うAPIリクエストの信頼性が向上します。
対処方法: 特になし。

### Bug ID: 423597917
原文: **`POST` operations for AppGroupApp keys updated** `POST` operations for AppGroup app keys now insert scopes and attributes instead of appending these values. This behavior is consistent with `POST` operations for companies in Apigee Edge for Public Cloud.
説明: AppGroupAppキーに対する`POST`操作の挙動が変更されました。これまでスコープや属性を「追加 (appending)」していましたが、今後は「挿入 (inserting)」するようになります。これは、Apigee Edge for Public Cloudにおける企業（companies）に対する`POST`操作の一貫した動作です。
影響有無: **影響あり（要確認）**。AppGroupAppキーに対して`POST`操作を使用しており、その操作がスコープや属性を既存の値に追加する（複数値を持つことを期待する）ロジックに依存していた場合、動作が変わる可能性があります。新しい動作では、既存の値を上書きする可能性や、重複を許容しない動作になる可能性があります。
対処方法: AppGroupAppキーに対して`POST`操作を利用している場合、この変更が既存のワークフローや期待するデータ状態に影響を与えないか、テスト環境で動作検証を実施してください。特に、スコープや属性の管理方法を見直しが必要になる場合があります。

### Bug ID: 390234048
原文: **Resolved issue resulting in missing fields in API responses for Monetization rate plans** The `createdAt` and `lastModifiedAt` fields are now present in responses from the `organizations.apiproducts.rateplans` API.
説明: Monetizationの料金プランに関するAPI応答（`organizations.apiproducts.rateplans`）で、`createdAt`と`lastModifiedAt`フィールドが欠落していた問題が修正されました。これらのフィールドが応答に含まれるようになります。
影響有無: 影響なし（ポジティブな影響）。Monetization機能を利用しており、該当APIの応答でこれらのタイムスタンプ情報を利用していた、または利用したかった場合に改善されます。
対処方法: 特になし。

### Bug ID: 422757662
原文: **Reverted problematic commit regarding X-b3 trace headers send when using distributed tracing.**
説明: 分散トレーシング使用時に`X-b3`トレースヘッダーの送信に関する問題を引き起こしていたコミットが元に戻されました。
影響有無: 影響なし（ポジティブな影響）。`X-b3`ヘッダーを利用した分散トレーシングに問題が発生していた場合、この修正によりトレーシングの信頼性が向上します。
対処方法: 特になし。

### Bug ID: N/A
原文: **Updates to security infrastructure and libraries.**
説明: セキュリティインフラストラクチャとライブラリが更新されました。
影響有無: 影響なし（ポジティブな影響）。セキュリティが強化され、潜在的な脆弱性への対策が施されます。
対処方法: 特になし。

# BigQuery
## Libraries
### Node.js
原文:
## Changes for @google-cloud/bigquery
[@google-cloud/bigquery](https://github.com/googleapis/nodejs-bigquery)
[8.1.1](https://github.com/googleapis/nodejs-bigquery/compare/v8.1.0...v8.1.1)
- Remove `is` package as dependency (#1500) (926c9f8)
説明: Node.js用BigQueryクライアントライブラリのバージョン8.1.1がリリースされました。このバージョンでは、内部依存パッケージである`is`パッケージが削除されました。
影響有無: 影響なし。これはライブラリの内部的な依存関係の最適化であり、BigQuery APIの動作やクライアントライブラリの公開APIに変更はありません。
対処方法: Node.jsクライアントライブラリを利用している場合、依存関係の改善とセキュリティの観点から、最新バージョンへのアップデートを検討しても良いですが必須ではありません。

### Python
原文:
## Changes for google-cloud-bigquery
[google-cloud-bigquery](https://github.com/googleapis/python-bigquery)
[3.35.1](https://github.com/googleapis/python-bigquery/compare/v3.35.0...v3.35.1)
- Specify the inherited-members directive for job classes (#2244) (d207f65)
説明: Python用BigQueryクライアントライブラリのバージョン3.35.1がリリースされました。このバージョンでは、ジョブクラスに関するドキュメント生成時の`inherited-members`ディレクティブが指定されました。
影響有無: 影響なし。これは主にライブラリのドキュメント生成に関する内部的な変更であり、BigQuery APIの動作やクライアントライブラリの公開APIに変更はありません。
対処方法: Pythonクライアントライブラリを利用している場合、最新バージョンへのアップデートは必須ではありません。

# Cloud Composer
## Fixed
原文: Fixed an issue that caused unexpected restarts of Airflow component workloads in the environment's cluster.
説明: Cloud Composer環境のクラスタ内で、Airflowコンポーネントのワークロードが予期せず再起動する問題が修正されました。
影響有無: 影響なし（ポジティブな影響）。環境の安定性が向上します。
対処方法: 特になし。

## Fixed
原文: *(Cloud Composer 3)* The `DAGS_FOLDER` reserved environment variable now correctly points to the local directory where DAG files are stored.
説明: (Cloud Composer 3向け) 予約済みの環境変数`DAGS_FOLDER`が、DAGファイルが保存されるローカルディレクトリを正しく指すようになりました。
影響有無: 影響なし。現在の環境はCloud Composer 2（Composer version 2.7.1）のため、この変更は適用されません。
対処方法: 特になし。

## Changed
原文:
 New Airflow builds
are available in Cloud Composer 3:
[Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-2.10.5-build.10 (default)
- composer-3-airflow-2.9.3-build.30
説明: Cloud Composer 3向けに新しいAirflowビルドイメージが提供されました。
影響有無: 影響なし。現在の環境はCloud Composer 2（Composer version 2.7.1）のため、この変更は適用されません。
対処方法: 特になし。

## Changed
原文:
 New images
are available in Cloud Composer 2:
[images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
- composer-2.13.8-airflow-2.10.5 (default)
- composer-2.13.8-airflow-2.9.3
説明: Cloud Composer 2向けに新しいイメージが提供されました。デフォルトは`composer-2.13.8-airflow-2.10.5`です。
影響有無: **影響あり**。現在利用中のComposer環境は`Composer version 2.7.1`、`Airflow version 2.7.3`であり、提供されている新しいイメージ（`2.13.8`）よりもかなり古いバージョンです。新しいイメージへのアップグレードを検討する必要があります。
対処方法:
1.  **アップグレード計画の策定**: 現在の`Composer 2.7.1 / Airflow 2.7.3`から、新しい`Composer 2.13.8 / Airflow 2.10.5`または`2.9.3`へのアップグレード計画を立ててください。
2.  **DAGの互換性確認**: Airflowのメジャーバージョンアップ（2.7.3から2.9.3または2.10.5）を伴うため、既存のDAGが新しいAirflowバージョンで正しく動作するか、テスト環境で十分に検証してください。
3.  **依存ライブラリの確認**: DAGsが依存するPythonライブラリが、新しいAirflowバージョンおよびComposerイメージで互換性があるか確認してください。
4.  **環境のアップグレード**: 計画に基づき、Cloud Composer環境を新しいイメージにアップグレードしてください。

## Deprecated
原文: Cloud Composer version 2.8.6 has reached its end of support period.
説明: Cloud Composerバージョン2.8.6がサポート終了期間に達しました。
影響有無: **影響あり**。現在利用中のComposer環境は`Composer version 2.7.1`であり、サポートが終了したバージョン（2.8.6）よりもさらに古いバージョンです。これは、現在の環境がすでにサポート対象外である、あるいは間もなくサポート対象外となる可能性が高いことを示唆しています。サポート対象外の環境を使い続けることは、セキュリティリスクや、問題発生時のサポートが受けられないなどの運用リスクを伴います。
対処方法: 早急に、最新のCloud Composer 2イメージ（`composer-2.13.8-airflow-2.10.5`など）へのアップグレード計画を策定し、実行してください。アップグレードに際しては、前述の「Changed」セクションで示した対処方法と同様に、DAGの互換性確認とテストを十分に行ってください。

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
説明: 2025年5月から10月にかけて、GKEクラスターの内部コントロールプレーンデータストアのメンテナンスが実施されます。これにより、スケーラビリティと信頼性が向上します。このメンテナンスは、設定されたメンテナンスウィンドウ中に約15分間行われ、その間、Kubernetes APIサーバーが利用できなくなります。
**影響を受ける可能性のある操作**:
*   `kubectl`コマンドや他のKubernetes APIクライアントからの操作
*   CI/CDパイプラインによるデプロイやアプリケーション更新
*   Google Cloud ConsoleからのGKEクラスター操作
*   Cluster Autoscaler、HPA/VPA、ノード自動修復などのコントロールプレーンが管理する自動化機能
**影響を受けない操作**:
*   実行中のアプリケーションの動作
*   ノードプールの操作
*   データプレーン（ワークロード間のトラフィック）
影響有無: **影響あり**。2025年5月以降、設定したメンテナンスウィンドウ中に最大15分間、Kubernetes APIサーバーが利用不可になるため、APIアクセスを必要とする運用ツールやアプリケーションが一時的に機能停止する可能性があります。
対処方法:
1.  **メンテナンスウィンドウの確認と設定**: 各GKEクラスターのメンテナンスウィンドウと除外設定を確認し、APIの停止が許容できる時間帯（例：業務時間外、システム負荷が低い時間帯）に設定してください。
2.  **API停止を考慮したワークフローの設計**:
    *   重要なデプロイや設定変更など、Kubernetes APIへのアクセスが必須となる作業は、メンテナンスウィンドウ中には実行しないように計画してください。
    *   CI/CDパイプラインや運用スクリプトでAPIアクセスを行う場合、APIが一時的に利用不可になることを想定し、リトライロジックの実装やメンテナンス期間中の実行抑制を検討してください。
3.  **関係者への周知**: このメンテナンスのスケジュールと影響について、開発チームや運用チームなど関係者に周知してください。

## Fixed
原文: A fix is available for an issue in which the Compute Engine Persistent Disk CSI driver failed with an `invalid cpuString` error on GKE nodes that used custom machine types. This issue prevented successful attachment and mounting of Persistent Disk volumes on affected nodes. The fix is available in the following GKE versions:
- 1.31.10-gke.1021000 and later
- 1.32.4-gke.1698000 and later
- 1.33.1-gke.1386000 and later
説明: カスタムマシンタイプを使用するGKEノードで、Compute Engine Persistent Disk CSIドライバーが`invalid cpuString`エラーで失敗し、Persistent Diskボリュームの添付やマウントができない問題が修正されました。この修正は、特定のGKEバージョン以降で利用可能です。
影響有無: 影響なし（ポジティブな影響）。カスタムマシンタイプを使用するGKEノードでこの問題に遭遇していた場合、上記のバージョンにアップグレードすることで問題が解決されます。現在この問題が発生していない場合は影響ありません。
対処方法: カスタムマシンタイプを使用しているGKEノードでPersistent Disk CSIドライバー関連のエラーが発生している場合、上記のGKEバージョンにアップグレードを検討してください。

# SAP on Google Cloud
## Announcement
原文: **New SAP NetWeaver certification: C4D bare metal machine types**
For use with SAP NetWeaver, SAP has certified the following Compute Engine bare metal machine types: `c4d-standard-384-metal` and `c4d-highmem-384-metal`.
For more information, see the following:
- Certifications for SAP applications on Google Cloud
- C4D machine series
説明: SAP NetWeaver向けに、Compute EngineのC4Dベアメタルマシンタイプ（`c4d-standard-384-metal`と`c4d-highmem-384-metal`）がSAPによって認定されました。
影響有無: 影響なし。SAP NetWeaverを利用している、または導入を検討しており、かつベアメタルマシンタイプを評価している場合に、選択肢が増えるという情報提供です。
対処方法: 特になし。

# Security Command Center
## Changed
原文: **Model Armor filter updates**
- The prompt injection and jailbreak detection filter now supports 10,000 tokens.
- For the Sensitive Data Protection filter, `SKIP_DETECTION` is returned if the prompt or response exceeds the token limit.
- For all other filters, if the prompt or response exceeds the token limit, `MATCH_FOUND` is returned if malicious content is found, and `SKIP_DETECTION` is returned if no malicious content is found.
説明: Model Armorのフィルターが更新されました。
*   プロンプトインジェクションおよびジェイルブレイク検出フィルターが10,000トークンまでサポートするようになりました。
*   機密データ保護フィルターでは、プロンプトまたは応答がトークン制限を超過した場合、`SKIP_DETECTION`が返されます。
*   その他のフィルターでは、プロンプトまたは応答がトークン制限を超過した場合でも、悪意のあるコンテンツが検出されれば`MATCH_FOUND`が返され、検出されなければ`SKIP_DETECTION`が返されます。
影響有無: 影響なし。Model Armorを利用している場合、フィルターの挙動が改善され、特に長いプロンプトや応答に対する検出能力が向上します。機密データ保護フィルターの挙動が明確化されます。
対処方法: 特になし。Model Armorの検出結果を処理するロジックを実装している場合は、`SKIP_DETECTION`の返却条件が明確になったため、必要に応じてハンドリングを見直すことを検討しても良いでしょう。

---
**用語説明**

*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォーム。APIの設計、セキュリティ、デプロイ、監視、分析など、APIライフサイクル全体を管理します。
*   **OASValidation Policy**: Apigeeのポリシーの一つで、OpenAPI Specification (OAS) に基づいてAPIリクエストやレスポンスの構造と内容を検証します。
*   **`$ref`**: OpenAPI Specificationなどで使われる参照構文。別のスキーマ定義やコンポーネントを参照するために使用されます。
*   **AppGroupApp keys**: Apigeeでアプリケーションを管理する際に使用されるキーで、アプリケーションにアクセス制御（スコープや属性）を適用するために使われます。
*   **Monetization rate plans**: Apigee Monetization機能で、APIの利用に対して課金モデル（料金プラン）を定義・管理する機能です。
*   **X-b3 trace headers**: 分散トレーシングシステム（例: Zipkin, Brave）で、リクエストのトレーシングIDやスパンIDを伝播させるために使用されるHTTPヘッダーのセットです。
*   **Cloud Composer**: Google Cloud上でApache Airflowを実行するためのマネージドサービス。データパイプラインのオーケストレーションに使用されます。
*   **DAGs (Directed Acyclic Graphs)**: Apache Airflowでワークフローを定義するために使用される、タスク間の依存関係を表すグラフ構造です。
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するマネージドなKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Kubernetes API server**: Kubernetesクラスターのコントロールプレーンの中心コンポーネント。APIリクエスト（`kubectl`コマンドなど）を処理し、クラスターの状態を管理します。
*   **コントロールプレーン**: Kubernetesクラスターを管理・制御するコンポーネントの集合体（APIサーバー、スケジューラー、コントローラーマネージャーなど）。
*   **データプレーン**: Kubernetesクラスターにおいて、実際にワークロード（Pod）が実行され、ネットワークトラフィックが流れる部分（ノード、Pod、Serviceなど）。
*   **Compute Engine Persistent Disk CSI driver**: GKEクラスター内でCompute Engineの永続ディスクをKubernetesのPersistentVolumeとして利用するためのドライバ。CSI（Container Storage Interface）標準に準拠しています。
*   **SAP NetWeaver**: SAP社のソフトウェア統合およびアプリケーションプラットフォーム。エンタープライズアプリケーションの基盤となります。
*   **C4D bare metal machine types**: Google Cloud Compute Engineが提供するベアメタルマシンタイプの一つで、高い性能と隔離性を提供します。
*   **Security Command Center**: Google Cloud全体のリスクと脆弱性を把握・管理するためのセキュリティ管理プラットフォーム。
*   **Model Armor**: Google Cloud Security Command Centerの一部で、AIモデルに対する攻撃（プロンプトインジェクション、ジェイルブレイクなど）から保護するための機能。
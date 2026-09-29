
# Title: September 28, 2026 
Link: https://docs.cloud.google.com/release-notes#September_28_2026<br>
Google Cloudインフラエンジニアとして、ご提示いただいたリリースノートについて製品ごとに影響調査を行いました。以下に調査結果を回答いたします。

---

# Cloud Logging
## Deprecated
原文: The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agents end of support.
[supported alternatives](https://docs.cloud.google.com/logging/docs/agent/index)
[Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/logging-agent)

説明：
以前のLogging agent（レガシーロギングエージェント）が正式にサポート終了となりました。これにより、エージェントに対する標準的なメンテナンスや定期的なバグ修正は提供されなくなります。Google Cloudは、サポートされている代替エージェントへの移行を強く推奨しています。

影響有無：
**影響あり**
現在、Compute Engine (VM) 等でレガシーなLogging agent (旧Stackdriver Logging agent) を利用してログ収集を行っている場合、今後バグ修正やセキュリティパッチが提供されなくなるため、将来的な問題発生のリスク、特にセキュリティ面でのリスクが高まります。

**影響なし**
Google Cloud Ops Agentを使用している場合、Cloud Logging APIを直接利用している場合、またはエージェントをデプロイしていない場合は影響ありません。

対処方法：
レガシーなLogging agentを使用しているかどうかを確認してください。もし使用している場合は、Google Cloud Ops Agent（推奨される統合エージェント）への移行を計画し、実行してください。リンク先のドキュメントに移行手順が記載されています。

用語説明：
*   **Legacy Logging agent (旧ロギングエージェント)**: Google CloudのCompute Engineインスタンスなどでログを収集するために以前使用されていたエージェント。
*   **Google Cloud Ops Agent**: Google Cloudが推奨する新しい統合エージェント。ログ収集とメトリクス収集の両方の機能を提供し、管理が簡素化されています。
*   **End of Support (サポート終了)**: 製品やサービスに対するベンダーからの公式サポート（バグ修正、セキュリティパッチ、技術サポートなど）が終了すること。

## Breaking
原文: Only platform services can write log entries to billing accounts. These logs have names with the format `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`. For more information, see `entries.write`.
[`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write)

説明：
課金アカウントにログエントリを直接書き込むことができるのは、Google Cloudプラットフォームサービスのみに限定されるようになりました。これにより、ユーザーが作成したアプリケーションやカスタムスクリプトが、直接`billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`形式のログ名を指定してログを書き込むことはできなくなります。

影響有無：
**影響あり**
カスタムアプリケーションやスクリプトがCloud Logging APIの`entries.write`メソッドを直接使用し、かつログのターゲットとして明示的に課金アカウントIDを指定している場合、そのログ書き込み処理は失敗するようになります。これは既存のワークフローに破壊的変更（Breaking Change）をもたらす可能性があります。

**影響なし**
通常、ユーザーアプリケーションはプロジェクトレベルのログ（`projects/[PROJECT_ID]/logs/[LOG_ID]`）にログを書き込むため、ほとんどのユーザーには影響がない可能性が高いです。

対処方法：
もしカスタムアプリケーションやスクリプトが課金アカウントに直接ログを書き込んでいる箇所がある場合は、代わりにプロジェクトIDを指定してログを書き込むように変更してください。課金に関する特定のログ要件がある場合は、ログルーターやエクスポート機能を利用して、プロジェクトレベルのログから必要な情報を収集することを検討してください。

用語説明：
*   **Billing Account (課金アカウント)**: Google Cloudのリソース使用量に対する支払いを管理するための最上位の管理単位。
*   **Log Entries (ログエントリ)**: Cloud Loggingに保存される個々のログ記録。
*   **`entries.write`**: Cloud Logging APIのメソッドの一つで、プログラムからログエントリをCloud Loggingに書き込むために使用されます。
*   **Platform services (プラットフォームサービス)**: Google Cloud自身が提供するサービスのこと。

---

# Cloud Monitoring
## Deprecated
原文: The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agent end of support.
[supported alternatives](https://docs.cloud.google.com/monitoring/agent/index)
[Legacy Monitoring and Logging agent end of support](https://docs.cloud.com/stackdriver/docs/deprecations/logging-agent)

説明：
以前のMonitoring agent（レガシーモニタリングエージェント）が正式にサポート終了となりました。これにより、エージェントに対する標準的なメンテナンスや定期的なバグ修正は提供されなくなります。Google Cloudは、サポートされている代替エージェントへの移行を強く推奨しています。

影響有無：
**影響あり**
現在、Compute Engine (VM) 等でレガシーなMonitoring agent (旧Stackdriver Monitoring agent) を利用してメトリクス収集を行っている場合、今後バグ修正やセキュリティパッチが提供されなくなるため、将来的な問題発生のリスク、特にセキュリティ面でのリスクが高まります。

**影響なし**
Google Cloud Ops Agentを使用している場合、Cloud Monitoring APIを直接利用している場合、またはエージェントをデプロイしていない場合は影響ありません。

対処方法：
レガシーなMonitoring agentを使用しているかどうかを確認してください。もし使用している場合は、Google Cloud Ops Agent（推奨される統合エージェント）への移行を計画し、実行してください。リンク先のドキュメントに移行手順が記載されています。

用語説明：
*   **Legacy Monitoring agent (旧モニタリングエージェント)**: Google CloudのCompute Engineインスタンスなどでシステムメトリクスを収集するために以前使用されていたエージェント。
*   **Google Cloud Ops Agent**: Google Cloudが推奨する新しい統合エージェント。ログ収集とメトリクス収集の両方の機能を提供し、管理が簡素化されています。

---

# Cloud Service Mesh
## Deprecated
原文: Cloud Service Mesh support for the in-cluster `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, in-cluster control plane components on GKE will not receive updates, security patches, or support from Google Cloud. You must migrate your clusters to managed Cloud Service Mesh by March 1, 2028.
[Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp)
[Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)
[migration guide](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster)
[Deprecations](https://docs.cloud.google.com/service-mesh/deprecations/)

説明：
Google Cloud上のGKEで、クラスタ内にデプロイするタイプの`ISTIOD`コントロールプレーン（In-cluster `ISTIOD` control plane）を利用したCloud Service Meshが、2026年9月28日に非推奨となり、**2028年3月1日**にサポートを終了します。この期日以降、in-clusterコントロールプレーンのコンポーネントはGoogle Cloudからの更新、セキュリティパッチ、サポートを受けられなくなります。そのため、2028年3月1日までに、マネージドCloud Service Meshへの移行が必須となります。

影響有無：
**影響あり**
現在、GKEクラスタにIstioを自己管理型（in-clusterデプロイメント）でインストールし、Cloud Service Meshの機能を使用している場合、2028年3月1日以降はサポートが受けられなくなり、セキュリティリスクや機能停止のリスクが発生します。

**影響なし**
GKEでCloud Service Meshを使用していない場合、または既にマネージドCloud Service Mesh (`TRAFFIC_DIRECTOR`コントロールプレーン) を使用している場合は影響ありません。

対処方法：
現在in-cluster `ISTIOD`コントロールプレーンを使用しているGKEクラスタを、2028年3月1日までにマネージドCloud Service Mesh (`TRAFFIC_DIRECTOR`コントロールプレーン) へ移行してください。提供されている移行ガイドとサポートされる機能リストを参照し、計画的に移行を進めることが重要です。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供する、オープンソースのIstioをベースとしたサービスメッシュソリューション。
*   **`ISTIOD`**: Istioコントロールプレーンの主要コンポーネント。サービスディスカバリ、設定、証明書管理などを担当します。
*   **In-cluster `ISTIOD` control plane**: IstioのコントロールプレーンコンポーネントをユーザーのGKEクラスタ内に直接デプロイし、ユーザー自身が管理するデプロイモデル。
*   **Managed Cloud Service Mesh**: Google CloudがIstioコントロールプレーンの一部を管理するサービス。特に`TRAFFIC_DIRECTOR`コントロールプレーンを利用する形態を指します。
*   **Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3)**: Composerは内部的にGKEクラスタを利用していますが、Cloud Service MeshはComposer環境の内部サービス管理ではなく、ユーザーアプリケーション間のサービスメッシュとして利用されるため、Composer自体が直接この変更の影響を受ける可能性は低いですが、ComposerがデプロイされているGKEクラスタでユーザーが個別にCloud Service Mesh (in-cluster Istio) を利用している場合は影響します。

## Deprecated
原文: Cloud Service Mesh support for the managed `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, managed `ISTIOD` control plane components on GKE on Google Cloud will not receive updates, security patches, or support from Google Cloud, and workload sidecars on unmodernized clusters will fail and be unable to receive or send requests.
Google Cloud is transitioning managed Cloud Service Mesh with Istio APIs to the `TRAFFIC_DIRECTOR` control plane implementation using Istio APIs. As part of this transition, support will also end for any features that are incompatible with the `TRAFFIC_DIRECTOR` control plane.
To continue using managed Cloud Service Mesh on GKE, you must modernize your clusters by March 1, 2028.
[Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)
[evaluate a fleet's compatibility for control plane modernization](https://docs.cloud.google.com/service-mesh/docs/migrate/eligibility)
[modernization guide](https://docs.cloud.google.com/service-mesh/docs/modernization)
[Managed control plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane-overview)
[release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes)

説明：
Google Cloud上のGKEで現在提供されているマネージド`ISTIOD`コントロールプレーン（マネージドCloud Service Meshの一部）が、2026年9月28日に非推奨となり、**2028年3月1日**にサポートを終了します。Google Cloudは、Istio APIを使用するマネージドCloud Service Meshを、より新しい`TRAFFIC_DIRECTOR`コントロールプレーンの実装へ移行しています。この移行に伴い、`TRAFFIC_DIRECTOR`コントロールプレーンと互換性のない一部の機能もサポートが終了します。2028年3月1日までにクラスタをモダナイズ（最新化）しない場合、ワークロードのサイドカーが機能しなくなり、リクエストの送受信ができなくなる可能性があります。

影響有無：
**影響あり**
現在、Google Cloudが管理する旧来のマネージド`ISTIOD`コントロールプレーンを使用しているCloud Service Meshユーザーは、2028年3月1日までにクラスタをモダナイズ（`TRAFFIC_DIRECTOR`コントロールプレーンへの移行）しないと、サポートが受けられなくなり、最終的にはワークロードの通信に障害が発生する可能性があります。

**影響なし**
GKEでCloud Service Meshを使用していない場合、または既に`TRAFFIC_DIRECTOR`コントロールプレーンを利用した最新のマネージドCloud Service Meshを使用している場合は影響ありません。

対処方法：
現在、旧来のマネージド`ISTIOD`コントロールプレーンを使用しているGKEクラスタを、2028年3月1日までに`TRAFFIC_DIRECTOR`コントロールプレーンを利用する新しい実装にモダナイズしてください。クラスタの互換性を確認するためのツールや、モダナイゼーションガイドが提供されていますので、これらを利用して計画的に移行を進めることが重要です。

用語説明：
*   **Managed `ISTIOD` control plane**: Google Cloudが管理するIstioコントロールプレーン。このリリースノートでは、新しい`TRAFFIC_DIRECTOR`実装へ移行する前の、既存のマネージドサービスメッシュ実装を指します。
*   **`TRAFFIC_DIRECTOR` control plane**: Google Cloudが提供する、Istio APIと互換性のある、より統合された新しいマネージドサービスメッシュコントロールプレーンの実装。グローバルロードバランシングやトラフィック管理機能も提供します。
*   **Workload sidecar**: サービスメッシュにおいて、アプリケーションのPodにEnvoyプロキシとして注入されるコンテナ。アプリケーションのネットワークトラフィックを傍受し、サービスメッシュの機能（トラフィックルーティング、ポリシー施行、テレメトリ収集など）を適用します。
*   **Modernization (モダナイゼーション)**: システムやアプリケーションを最新の技術やプラクティスに適合させること。この文脈では、古いマネージド`ISTIOD`コントロールプレーンから新しい`TRAFFIC_DIRECTOR`コントロールプレーンへの移行を指します。

---

# Title: September 29, 2026 
Link: https://docs.cloud.google.com/release-notes#September_29_2026<br>
Google Cloud インフラエンジニアとして、リリースノートの確認と影響調査のご依頼ありがとうございます。

現在、リリースノートの具体的な内容が提供されていないため、製品への影響有無や対処方法について詳細な調査を行うことができません。

お手数ですが、調査対象となるCloud SDKの「Breaking」カテゴリに関する具体的なリリースノートの原文をご提示いただけますでしょうか。

リリースノートの原文をご提示いただければ、以下のフォーマットに沿って速やかに調査を行い、回答させていただきます。

---

**（以下は、リリースノートが提供された場合の回答例のプレースホルダーです。）**

# Cloud SDK

## Breaking

原文: (ここに提供されたCloud SDKのBreaking変更に関するリリースノートの原文が入ります。)

説明：
(原文のリリースノートを元に、日本語で分かりやすく説明します。例えば、どのコマンド、API、または機能が変更され、どのような非互換性が生じるのかを具体的に記述します。)

影響有無：
(この変更がお客様の既存の構成、特にComposer 2.7.1やCI/CDパイプライン、自動化スクリプトなどに影響があるかどうかを判断し、その理由を簡潔に説明します。
「Breaking」カテゴリであるため、既存のワークフローやスクリプトが動作しなくなる可能性が高いことを前提に調査します。)

対処方法：
(影響がある場合、具体的にどのような対応が必要か（例：Cloud SDKのバージョンアップ、スクリプトの修正、認証方法の変更、代替APIへの移行など）を説明します。テスト環境での事前検証の重要性も強調します。)

用語説明：
*   **Breaking Change (破壊的変更)**: 既存のシステムやアプリケーションの動作を壊したり、互換性を失わせたりする変更のこと。通常、APIのシグネチャ変更、動作仕様の変更、機能の削除などが含まれ、対応しないと既存のコードが機能しなくなる可能性がある。
*   **Cloud SDK**: Google Cloud Platform のサービスやリソースを管理するためのコマンドラインツール (gcloud CLI) やライブラリのセット。開発者がローカル環境やCI/CDパイプラインからGCPを操作するために広く利用される。
*   **gcloud CLI**: Cloud SDKに含まれる主要なコマンドラインインターフェースツール。GCPのほぼすべてのサービスに対して操作を行うことができる。

---

リリースノートの提供をお待ちしております。
# Title: September 28, 2026 
Link: https://docs.cloud.google.com/release-notes#September_28_2026<br>
Google Cloud リリースノートに関する影響調査の結果を以下に報告いたします。

---

# Cloud Logging
## Deprecated
原文: The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agents end of support.

説明：レガシーなCloud Loggingエージェントのサポートが正式に終了しました。これにより、標準のメンテナンスおよび定期的なバグ修正は提供されなくなります。引き続きログ収集を行うためには、Googleが推奨するサポート対象の代替エージェント（例：Opsエージェント）への移行が強く推奨されます。

影響有無：
*   **影響なし（ほとんどの場合）**: Google Cloud Composer 2.7.1 は、基盤となるGKEクラスタノードのOSイメージに最新のOpsエージェント（またはその前身であるStackdriver Logging Agentのサポート対象バージョン）が含まれていることが一般的であり、ユーザーが明示的にレガシーエージェントを導入していない限り、直接的な影響はありません。
*   **影響あり（特定のケース）**: もしお客様の環境で、Composerが利用するGKEクラスタのカスタムノードイメージや、Composerとは独立したCompute EngineなどのVMインスタンスで、手動で導入されたレガシーLoggingエージェントが使用されている場合は影響を受けます。

対処方法：
レガシーLoggingエージェントを使用していることが確認された場合は、速やかにOpsエージェントなど、サポートされている代替エージェントへの移行を計画・実行してください。詳細は公式ドキュメント「[Supported alternatives](https://cloud.google.com/logging/docs/agent/index)」および「[Legacy Monitoring and Logging agents end of support](https://cloud.google.com/stackdriver/docs/deprecations/logging-agent)」を参照してください。

用語説明：
*   **Logging agent**: Compute Engineなどの仮想マシン（VM）インスタンスからシステムログやアプリケーションログを収集し、Cloud Loggingに送信するためのソフトウェアエージェント。
*   **Ops agent**: Google Cloudが推奨する新しい統合エージェント。Cloud MonitoringとCloud Loggingの両方の機能を統合し、OpenTelemetryベースで構築されています。レガシーエージェント（Stackdriver Logging Agent、Stackdriver Monitoring Agent）の後継にあたります。

---

## Breaking
原文: Only platform services can write log entries to billing accounts. These logs have names with the format `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`. For more information, see `entries.write`.

説明：請求アカウント（`billingAccounts/[BILLING_ACCOUNT_ID]`）に直接ログエントリを書き込むことができるのは、Google Cloudのプラットフォームサービスのみに制限されました。この変更は、`entries.write` APIを介したログの書き込みに適用されます。

影響有無：
*   **影響なし**: 一般的なアプリケーションやユーザーは、通常、プロジェクト単位でログを管理し、請求アカウントに直接ログを書き込むことはありません。Cloud Composer 2.7.1 もプロジェクト内のリソースとしてログを出力するため、この変更による直接的な影響はありません。

対処方法：
特になし。もし、非常に稀なケースで、ユーザーがカスタムで請求アカウントに直接ログを書き込むような実装を行っていた場合は、プロジェクトレベルのログに切り替えるか、プラットフォームサービスによるログ記録の仕組みに依存する必要があります。

用語説明：
*   **Billing account**: Google Cloudにおける請求の単位であり、複数のプロジェクトを紐付けて費用を管理します。
*   **Platform services**: Google Cloudの基盤となるサービス群。例えば、監査ログや使用量ログなど、Google Cloudサービス自体が生成するログが該当します。
*   **`entries.write`**: Cloud Logging APIの一部であり、プログラム的にログエントリをCloud Loggingに書き込むために使用されるメソッドです。

---

# Cloud Monitoring
## Deprecated
原文: The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agent end of support.

説明：レガシーなCloud Monitoringエージェントのサポートが正式に終了しました。これにより、標準のメンテナンスおよび定期的なバグ修正は提供されなくなります。引き続きメトリクス収集を行うためには、Googleが推奨するサポート対象の代替エージェント（例：Opsエージェント）への移行が強く推奨されます。

影響有無：
*   **影響なし（ほとんどの場合）**: Google Cloud Composer 2.7.1 は、基盤となるGKEクラスタノードのOSイメージに最新のOpsエージェント（またはその前身であるStackdriver Monitoring Agentのサポート対象バージョン）が含まれていることが一般的であり、ユーザーが明示的にレガシーエージェントを導入していない限り、直接的な影響はありません。
*   **影響あり（特定のケース）**: もしお客様の環境で、Composerが利用するGKEクラスタのカスタムノードイメージや、Composerとは独立したCompute EngineなどのVMインスタンスで、手動で導入されたレガシーMonitoringエージェントが使用されている場合は影響を受けます。

対処方法：
レガシーMonitoringエージェントを使用していることが確認された場合は、速やかにOpsエージェントなど、サポートされている代替エージェントへの移行を計画・実行してください。詳細は公式ドキュメント「[Supported alternatives](https://cloud.google.com/monitoring/agent/index)」および「[Legacy Monitoring and Logging agent end of support](https://cloud.google.com/stackdriver/docs/deprecations/logging-agent)」を参照してください。

用語説明：
*   **Monitoring agent**: Compute Engineなどの仮想マシン（VM）インスタンスからシステムやアプリケーションのメトリクス（CPU使用率、メモリ使用率など）を収集し、Cloud Monitoringに送信するためのソフトウェアエージェント。
*   **Ops agent**: (Cloud Loggingのセクションと同じ)

---

# Cloud SQL for PostgreSQL
## Breaking
原文: To improve security, removed the `cloudsql.instances.export` permission from the following roles: Cloud SQL Viewer (`roles/cloudsql.viewer`), Basic Reader (`roles/reader`), Basic Viewer (Legacy) (`roles/viewer`). To retain export capabilities, assign the Cloud SQL Editor (`roles/cloudsql.editor`) role or update custom roles to include the `cloudsql.instances.export` permission. For more information, see Cloud SQL roles.

説明：セキュリティ強化のため、Cloud SQL for PostgreSQLインスタンスのエクスポート操作を実行するための`cloudsql.instances.export`権限が、以下の既存のIAMロールから削除されました：Cloud SQL Viewer (`roles/cloudsql.viewer`)、Basic Reader (`roles/reader`)、Basic Viewer (Legacy) (`roles/viewer`)。今後もエクスポート機能を利用するには、Cloud SQL Editor (`roles/cloudsql.editor`) ロールを付与するか、カスタムIAMロールを作成して`cloudsql.instances.export`権限を明示的に含める必要があります。

影響有無：
*   **影響あり**: 既存のシステムで、削除されたロール（Cloud SQL Viewer, Basic Reader, Basic Viewer (Legacy)）を持つユーザーまたはサービスアカウントがCloud SQL for PostgreSQLインスタンスのエクスポート操作（例：`gcloud sql export`コマンド、またはAPI経由でのエクスポート）を実行している場合、それらの操作が失敗するようになります。
*   **影響なし（Composerサービス自体）**: Cloud Composer 2.7.1 はCloud SQL for PostgreSQLをメタデータデータベースとして利用しますが、Composerサービスアカウントがこれらの特定の「Viewer」系のロールでエクスポート操作を直接行うことは通常ないため、Composerサービス自体の動作に直接的な影響はありません。

対処方法：
もし、影響を受けるロールを持つユーザーやサービスアカウントがCloud SQL for PostgreSQLのエクスポート機能を引き続き必要とする場合は、以下のいずれかの対応を行ってください。
1.  当該ユーザーまたはサービスアカウントに`Cloud SQL Editor` (`roles/cloudsql.editor`) ロールを付与する。
2.  カスタムIAMロールを作成し、そのロールに`cloudsql.instances.export`権限を明示的に含め、当該ユーザーまたはサービスアカウントにそのカスタムロールを付与する。

用語説明：
*   **IAM Role (Identity and Access Management Role)**: Google Cloudリソースに対するアクセス権限の集合を定義するもので、ユーザーやサービスアカウントに付与されます。
*   **`cloudsql.instances.export`**: Cloud SQLインスタンスからデータをCloud Storageバケットにエクスポートする操作を許可する権限です。
*   **Cloud SQL Viewer (`roles/cloudsql.viewer`)**: Cloud SQLインスタンスの構成やデータを参照できる権限を持つ事前定義ロール。
*   **Cloud SQL Editor (`roles/cloudsql.editor`)**: Cloud SQLインスタンスに対する読み取りおよび書き込み操作を許可する事前定義ロールで、エクスポート機能も含まれます。

---

# Cloud Service Mesh
## Deprecated
原文: Cloud Service Mesh support for the in-cluster `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, in-cluster control plane components on GKE will not receive updates, security patches, or support from Google Cloud. You must migrate your clusters to managed Cloud Service Mesh by March 1, 2028.

説明：Google Cloud上のGKEで、クラスター内（in-cluster）にデプロイされる`ISTIOD`コントロールプレーンを使用するCloud Service Meshのサポートが、2026年9月28日をもって非推奨となり、2028年3月1日にサポートが終了します。2028年3月1日以降は、GKEクラスタ内のISTIODコントロールプレーンコンポーネントは、Google Cloudからの更新、セキュリティパッチ、およびサポートを受けられなくなります。この期日までに、マネージドCloud Service Meshへの移行が必須となります。

影響有無：
*   **影響なし（ほとんどの場合）**: Google Cloud Composer 2.7.1 環境は、標準ではCloud Service Meshを有効化しません。また、Airflowワークロード自体がService Meshを必須とするものではありません。
*   **影響あり（特定のケース）**: もしお客様が、Cloud ComposerがデプロイされているGKEクラスタに対して、明示的にこの「in-cluster ISTIOD」構成のCloud Service Meshを有効化し、利用している場合は影響を受けます。これは非常に特殊な利用ケースです。

対処方法：
もし、クラスター内ISTIODコントロールプレーンのCloud Service Meshを使用している場合は、2028年3月1日までにマネージドCloud Service Mesh（特に`TRAFFIC_DIRECTOR`コントロールプレーンへの移行）を計画し、実行してください。移行ガイド（[migration guide](https://cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster)）およびサポートされる機能（[Supported features](https://cloud.google.com/service-mesh/docs/supported-features-managed)）を確認し、移行計画を立ててください。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供する、Istioをベースとしたマネージドなサービスメッシュ。サービス間の通信、ポリシー適用、トラフィック管理、可観測性などを提供します。
*   **ISTIOD**: Istioのコントロールプレーンの主要コンポーネント。サービスディスカバリ、コンフィグレーション、証明書管理などを担当します。
*   **In-cluster control plane**: サービスメッシュのコントロールプレーン（ISTIODなど）が、ワークロードと同じKubernetesクラスタ内にデプロイされている構成。
*   **Managed Cloud Service Mesh**: Google Cloudによって完全に管理されるサービスメッシュ。ユーザーはコントロールプレーンの運用負荷を負う必要がありません。
*   **TRAFFIC_DIRECTOR**: マネージドCloud Service Meshのコントロールプレーン実装の一つ。GKEクラスタの外部で実行され、大規模なデプロイに適しています。

---

## Deprecated
原文: Cloud Service Mesh support for the managed `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, managed `ISTIOD` control plane components on GKE on Google Cloud will not receive updates, security patches, or support from Google Cloud, and workload sidecars on unmodernized clusters will fail and be unable to receive or send requests. Google Cloud is transitioning managed Cloud Service Mesh with Istio APIs to the `TRAFFIC_DIRECTOR` control plane implementation using Istio APIs. To continue using managed Cloud Service Mesh on GKE, you must modernize your clusters by March 1, 2028.

説明：Google Cloud上のGKEで、マネージド`ISTIOD`コントロールプレーンを使用するCloud Service Meshのサポートが、2026年9月28日をもって非推奨となり、2028年3月1日にサポートが終了します。2028年3月1日以降、Google Cloud上のGKEにおけるマネージド`ISTIOD`コントロールプレーンコンポーネントは、Google Cloudからの更新、セキュリティパッチ、サポートを受けられなくなり、移行されていないクラスター上のワークロードサイドカーは機能しなくなり、リクエストの送受信ができなくなります。Google Cloudは、Istio APIを使用するマネージドCloud Service Meshを、`TRAFFIC_DIRECTOR`コントロールプレーン実装へ移行しています。引き続きGKEでマネージドCloud Service Meshを使用するには、2028年3月1日までにクラスターをモダナイズ（移行）する必要があります。

影響有無：
*   **影響なし（ほとんどの場合）**: Google Cloud Composer 2.7.1 環境は、標準ではCloud Service Meshを有効化しません。また、Airflowワークロード自体がService Meshを必須とするものではありません。
*   **影響あり（特定のケース）**: もしお客様が、Cloud ComposerがデプロイされているGKEクラスタに対して、明示的にこの「マネージドISTIOD」構成のCloud Service Meshを有効化し、利用している場合は影響を受けます。これは非常に特殊な利用ケースです。

対処方法：
もし、マネージドISTIODコントロールプレーンのCloud Service Meshを使用している場合は、2028年3月1日までに`TRAFFIC_DIRECTOR`コントロールプレーンへの移行を計画し、実行してください。移行の計画にあたっては、サポートされる機能の互換性（[Supported features](https://cloud.google.com/service-mesh/docs/supported-features-managed)）、フリートの互換性（[evaluate a fleet's compatibility for control plane modernization](https://cloud.google.com/service-mesh/docs/migrate/eligibility)）、およびモダナイゼーションガイド（[modernization guide](https://cloud.google.com/service-mesh/docs/modernization)）を確認してください。

用語説明：
*   **Managed ISTIOD**: このコンテキストでは、`TRAFFIC_DIRECTOR`へ移行される前の、Google Cloudが管理するISTIODベースのサービスメッシュ実装を指します。
*   **TRAFFIC_DIRECTOR**: (Cloud Service Meshの「In-cluster ISTIOD」セクションと同じ)
*   **Workload sidecar**: サービスメッシュにおいて、アプリケーションコンテナと一緒にPod内にデプロイされ、アプリケーションのネットワーク通信をプロキシ・インターセプトするコンテナ（通常はEnvoyプロキシ）。
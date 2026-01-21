
# Title: January 20, 2026 
Link: https://docs.cloud.google.com/release-notes#January_20_2026<br>
# Cloud Service Mesh
## Announcement
原文: 1.28.2-asm.4 is now available for in-cluster Cloud Service Mesh. You can now download 1.28.2-asm.4 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.28.0 subject to the list of supported features. [Istio 1.28.0](https://istio.io/latest/news/releases/1.28.x/announcing-1.28/) [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster) The following environment variables, fields, and annotations are not supported: - `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY` - Additional attributes for `HTTPCookie` in the DestinationRule API - `caCertCredentialName` field in ServerTLSSettings API - Optional `NetworkPolicy` for Istiod deployment - Disable shadow host suffix - `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` Istio dual stack is not supported Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported. The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with legacy behavior. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.28.2-asm.4 uses Envoy v1.36.5-dev. [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: in-cluster Cloud Service Mesh (ASM) の新しいバージョンである 1.28.2-asm.4 が利用可能になりました。このバージョンには、Istio 1.28.0 の機能が含まれていますが、Google Cloud Service Mesh がサポートする機能リストに準拠します。
このリリースでは、以下の環境変数、フィールド、アノテーションがサポート対象外であることが明記されています。
*   `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
*   DestinationRule API における `HTTPCookie` の追加属性
*   ServerTLSSettings API における `caCertCredentialName` フィールド
*   Istiod デプロイメント用のオプションの `NetworkPolicy`
*   `Disable shadow host suffix`
*   `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP`
また、Istio のデュアルスタック機能と、Envoy 統計情報の遅延サブセット作成 (lazy subset creation) の実験的機能はサポートされません。
一方で、レガシーな動作との整合性を保つため、`ENABLE_AUTO_SNI` フラグは引き続きサポートされます。
このバージョンでは、Envoy v1.36.5-dev が使用されています。アップグレードの詳細については、公式ドキュメントを参照してください。

影響有無: **影響なし**（ただし、アップグレードを検討する際には注意が必要）
既存で稼働しているCloud Service Meshのバージョンが自動的に更新されるわけではないため、現在の運用に直接的な影響はありません。
しかし、今後Cloud Service Meshのバージョンアップを計画する際、この 1.28.2-asm.4 を選択する場合には、現在利用している機能が上記の「サポートされない機能」リストに含まれていないか、またはそれらの機能を計画しているIstioの利用方法に依存していないかを確認する必要があります。もしサポートされない機能を利用している場合、アップグレード後に既存の機能が動作しなくなる可能性があります。

対処方法:
*   **現状維持の場合:** 特に対処は不要です。
*   **アップグレードを検討する場合:**
    *   [Cloud Service Mesh のアップグレードガイド](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) を参照し、アップグレード手順を確認してください。
    *   [Cloud Service Mesh でサポートされる機能リスト](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster) を詳細に確認し、現在のワークロードや将来の計画において、リリースノートで明記されたサポートされない機能に依存していないかを確認してください。
    *   もしサポートされない機能に依存している場合は、代替手段の検討、またはアップグレードの再検討が必要です。

用語説明:
*   **Cloud Service Mesh (ASM):** Google Cloud が提供する、Istio をベースとしたフルマネージドなサービスメッシュプラットフォームです。サービスのトラフィック管理、セキュリティ、および可観測性を提供します。
*   **in-cluster Cloud Service Mesh:** ASM のデプロイメントモードの一つで、Istio のコントロールプレーン（Istiodなど）がユーザーの Google Kubernetes Engine (GKE) クラスタ内にデプロイされます。これにより、コントロールプレーンの管理をより詳細に制御できます。
*   **Istio:** マイクロサービス間で発生するネットワーク通信を管理、制御、保護するためのオープンソースのサービスメッシュプラットフォームです。
*   **Envoy:** Istio のデータプレーンとして広く利用されている高性能なオープンソースのプロキシです。サービス間のすべてのトラフィックをインターセプトし、ルーティング、負荷分散、メトリクス収集などを実行します。
*   **DestinationRule API:** Istio のリソースで、特定のサービスへのトラフィックがどのようにルーティングされ、負荷分散されるかを定義します。ロードバランシングアルゴリズム、接続プール設定、TLS設定などを構成できます。
*   **ServerTLSSettings API:** Istio のリソースで、サーバサイドの TLS (Transport Layer Security) 設定を定義します。クライアント証明書の検証や、特定のポートでの TLS の有効化などを行います。
*   **Istiod:** Istio のコントロールプレーンの主要コンポーネントです。設定の配布、証明書管理、メトリクス収集、Webhooks の管理などを担当します。
*   **Istio dual stack:** Istio が IPv4 と IPv6 の両方のアドレスをサポートするネットワーク構成で動作する機能です。
*   **lazy subset creation of envoy statistics:** Envoy の統計情報収集に関する実験的な機能です。すべての統計情報を常に生成するのではなく、必要に応じてオンデマンドで生成することで、リソース使用量を最適化しようとする試みです。
*   **ENABLE_AUTO_SNI:** Server Name Indication (SNI) を自動的に検出して処理を可能にするフラグです。SNI は、単一の IP アドレスで複数の TLS 証明書をホストするために使用されます。このフラグは、古い互換性のために残されています。
# Title: January 19, 2026 
Link: https://docs.cloud.google.com/release-notes#January_19_2026<br>
# BigQuery
## Breaking
原文:
Dataform workflows,
BigQuery notebooks,
pipelines,
and
data preparations
are enforcing strict act-as mode at the project level. To avoid failures and
maintain automatic releases, you must use custom service accounts instead of the
default Dataform service agent across all repositories. You must also grant the
Service Account User role (`roles/iam.serviceAccountUser`) to the default
Dataform service agent and relevant principals. For more information and to
verify act-as permissions, see
[Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

説明：
Google Cloud BigQueryに関連するデータ統合および分析サービス（Dataformワークフロー、BigQueryノートブック、BigQueryパイプライン、BigQueryデータ準備）において、プロジェクトレベルで「厳格なact-asモード」が強制されるようになりました。この変更は、サービスアカウントの権限管理をよりセキュアかつ詳細に制御するためのものです。この厳格化により、既存のデプロイメントや自動リリースが中断されるのを防ぐため、以下の対応が必要になります。
1.  **カスタムサービスアカウントの利用必須化**: Dataformの全リポジトリで、デフォルトで利用されていたDataformサービスエージェントの代わりに、ユーザーが管理するカスタムサービスアカウントを使用する必要があります。
2.  **IAMロールの付与**: デフォルトのDataformサービスエージェントおよび関連するプリンシパル（例えば、Dataformのデプロイや実行を行うユーザーや別のサービスアカウント）に対して、`Service Account User` (`roles/iam.serviceAccountUser`) ロールを付与する必要があります。これにより、Dataformサービスエージェントが、指定されたカスタムサービスアカウントの権限を借用して操作を実行できるようになります。

影響有無：
**影響あり（Breaking Change）**。
この変更は既存のワークロードに中断をもたらす可能性のある「Breaking Change」としてアナウンスされています。BigQueryのDataformワークフロー、BigQueryノートブック、BigQueryパイプライン、またはBigQueryデータ準備機能を利用しており、特にデフォルトのDataformサービスエージェントを直接使用している、またはカスタムサービスアカウントの設定が厳密に行われていない場合、これらの機能の実行やデプロイが失敗する可能性があります。自動リリースパイプラインにも影響を及ぼす可能性があります。

対処方法：
この変更による既存ワークロードへの影響を回避するため、以下の手順で対応を進めてください。

1.  **利用状況の確認**:
    *   ご自身のGoogle Cloudプロジェクトで、Dataformワークフロー、BigQueryノートブック、BigQueryパイプライン、またはBigQueryデータ準備機能が現在利用されているか確認します。
    *   これらの機能でデフォルトのDataformサービスエージェント (`service-<project-number>@gcp-sa-dataform.iam.gserviceaccount.com` の形式) が使用されているか確認します。

2.  **カスタムサービスアカウントの準備**:
    *   Dataformがアクセスする必要のあるBigQueryデータセット、Cloud Storageバケットなどに対する適切な権限（例: `BigQuery Data Editor`, `Storage Object Viewer` など）を持つカスタムサービスアカウントを作成、または特定します。
    *   可能な限り最小権限の原則に従い、必要な権限のみを付与してください。

3.  **Dataformリポジトリの構成変更**:
    *   Dataformの各リポジトリの設定で、SQLワークフローの実行に使用するサービスアカウントを、デフォルトのサービスエージェントから手順2で準備したカスタムサービスアカウントに変更します。
    *   詳細な設定手順については、Dataformの公式ドキュメント「[Configuring service accounts](https://cloud.google.com/dataform/docs/configuring-service-account)」を参照してください。

4.  **IAMロールの付与**:
    *   **デフォルトのDataformサービスエージェント** (`service-<project-number>@gcp-sa-dataform.iam.gserviceaccount.com`) に対して、`Service Account User` (`roles/iam.serviceAccountUser`) ロールを付与します。
    *   このロールは、Dataformサービスエージェントが、準備したカスタムサービスアカウントの権限を「act-as」するために必要です。
    *   Dataformワークフローのデプロイや実行を行うCI/CDパイプラインや、特定のユーザーなど、**関連するプリンシパル**にもこのロールが必要となる場合があります。

5.  **動作確認**:
    *   変更適用後、既存のDataformワークフロー、BigQueryノートブック、BigQueryパイプライン、またはBigQueryデータ準備が期待通りに動作するかどうか、特にデプロイ、コンパイル、実行の各ステップで問題がないか十分にテストしてください。

用語説明：
*   **act-asモード (Service Account Impersonation)**: あるプリンシパル（ユーザー、サービスアカウントなど）が、別のサービスアカウントの権限を一時的に借用して操作を実行する機能です。これにより、リソースへのアクセス権限を一元的に管理し、最小権限の原則を適用しやすくなります。このリリースノートでは、Dataformサービスエージェントが、より具体的な権限を持つカスタムサービスアカウントになり代わって操作を実行することを指します。
*   **Dataform workflows**: Google Cloud上でSQLワークフローを構築、スケジュール、管理するためのサービスです。BigQuery上でデータの変換やETL/ELTパイプラインを構築するのに利用されます。
*   **BigQuery notebooks**: BigQuery Studioの一部として提供されるJupyterノートブック環境で、BigQueryデータに対してPythonやSQLを使ってインタラクティブな分析やデータ操作を行うことができます。
*   **BigQuery pipelines**: BigQuery Studioの機能の一つで、複雑なデータ変換やETL/ELTワークフローを視覚的に構築し、スケジュール実行できる機能です。Dataformや他のBigQuery機能を統合して利用されることが多いです。
*   **BigQuery data preparations**: BigQuery Studioの機能の一部で、データを探索、クリーンアップ、変換し、分析に適した形式にするためのグラフィカルインターフェースを提供する機能です。
*   **デフォルトのDataformサービスエージェント**: Dataformサービスがプロジェクト内で動作するためにGoogle Cloudによって自動的に作成される、Google管理のサービスアカウントです。通常、`service-<project-number>@gcp-sa-dataform.iam.gserviceaccount.com` の形式です。
*   **Service Account User role (`roles/iam.serviceAccountUser`)**: このIAMロールを付与されたプリンシパルは、他のサービスアカウントになり代わって（act-asして）操作を実行する権限を持ちます。このロール自体はリソースへの具体的なアクセス権を付与するものではなく、あくまで「なり代わる」ための権限であり、リソースへのアクセス権は、なり代わったサービスアカウントが持つ権限によって決定されます。
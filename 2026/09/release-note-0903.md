
# Title: September 02, 2026 
Link: https://docs.cloud.google.com/release-notes#September_02_2026<br>
# BigQuery
## Change
原文: An updated version of the Simba JDBC driver for BigQuery is now available.
[Simba JDBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_jdbc_driver)

説明:
BigQueryにJavaアプリケーションから接続する際に使用される、Simba社が提供するJDBC（Java Database Connectivity）ドライバの新しいバージョンがリリースされました。このアップデートには、通常、バグ修正、パフォーマンスの最適化、セキュリティの改善などが含まれます。

影響有無:
**直接的な影響はありません。**
このリリースはBigQueryサービスそのものへの変更ではなく、BigQueryに外部のアプリケーション（BIツール、ETLツール、カスタムJavaアプリケーションなど）が接続する際に使用するクライアントドライバの更新です。既存のBigQuery環境やデータウェアハウスの動作に直接的な影響はありません。
ただし、JDBCドライバを介してBigQueryに接続しているシステムがある場合は、そのシステムの安定性、パフォーマンス、またはセキュリティ面で潜在的なメリットや、ごく稀に互換性の問題が発生する可能性が考えられます。

対処方法:
BigQueryにJDBCドライバを使用して接続しているアプリケーションが存在する場合、新しいドライバへのアップグレードを検討することを推奨します。
アップグレードに際しては、本番環境への適用前に開発環境やステージング環境で十分なテストを実施し、既存のワークロードが期待通りに動作することを確認してください。通常、最新版への更新は、セキュリティの向上やパフォーマンスの最適化に寄与します。

用語説明:
*   **JDBC (Java Database Connectivity)**: Javaプログラムからリレーショナルデータベースへの接続を可能にするための標準的なJava API（Application Programming Interface）です。これにより、Javaアプリケーションはデータベースのベンダーに依存せず、統一された方法でデータにアクセスできます。
*   **Simba JDBC driver for BigQuery**: Simba Technologies社が開発・提供している、BigQueryへのJDBC接続を可能にするための専用ドライバです。このドライバを使用することで、JavaベースのツールやアプリケーションがBigQueryと効率的に連携できます。
*   **BigQuery**: Google Cloudが提供する、フルマネージドでペタバイト規模のデータを分析できるエンタープライズデータウェアハウスです。SQLクエリを非常に高速に実行できる特徴があります。
# Title: September 01, 2026 
Link: https://docs.cloud.google.com/release-notes#September_01_2026<br>
Google Cloudのリリースノートに基づき、各製品の変更点とお客様のサービスへの影響を調査し、以下の通りご報告いたします。

---

# Cloud SDK

## Change
**原文:**
（この見出しの下に具体的なリリースノート内容が提供されていませんでした。）

**説明:**
Cloud SDKの変更に関するリリースノートですが、具体的な内容が提示されていないため、詳細な説明はできません。

**影響有無:**
リリースノートの内容が不明なため、影響の有無は判断できません。

**対処方法:**
追加の情報提供がない限り、特に対処は不要です。

**用語説明:**
*   **Cloud SDK:** Google Cloudとやり取りするためのコマンドラインツール（`gcloud`）、クライアントライブラリ、およびその他の開発ツール群。

---

# Cloud Service Mesh

## Security
**原文:**
```
Managed Cloud Service Mesh will start using proxy version
csm_mesh_proxy.20260819_RC00 for Gateway API on GKE clusters. This proxy
version maps closest to Envoy version 1.37. This change is rolling out to all
release channels and contains the fix for the managed Cloud Service Mesh
security vulnerabilities listed in
GCP-2026-057.

[GCP-2026-057](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057)
```

**説明:**
マネージドなCloud Service Meshが、GKEクラスター上のGateway API向けに新しいプロキシバージョン `csm_mesh_proxy.20260819_RC00` の利用を開始します。このプロキシバージョンはEnvoyバージョン1.37に相当し、GCP-2026-057で報告されたマネージドCloud Service Meshのセキュリティ脆弱性に対する修正が含まれています。この変更は、すべてのリリースチャネルに順次適用されます。

**影響有無:**
*   **Cloud Service Meshを利用している場合:** 影響があります。ただし、これはセキュリティ脆弱性の修正を含む自動的なアップデートであり、サービスに対するポジティブな影響が期待されます。マネージドサービスのため、お客様側での明示的な操作は不要です。
*   **Cloud Service Meshを利用していない場合:** 影響はありません。
*   **Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3) について:** Cloud ComposerはAirflowのマネージドサービスであり、直接Cloud Service Meshを利用するサービスではありません。したがって、本変更による影響はありません。

**対処方法:**
お客様側で特別な対処は必要ありません。マネージドサービスのため、Google Cloudによって自動的にアップデートが適用されます。セキュリティ修正が含まれるため、この更新が適用されることを待つことが推奨されます。

**用語説明:**
*   **Cloud Service Mesh:** Google Cloudが提供するフルマネージドなサービスメッシュソリューション。Istioをベースとしており、サービスの接続、監視、セキュリティ保護、トラフィック管理を容易にします。
*   **Envoy:** クラウドネイティブな高性能プロキシ。Istioのようなサービスメッシュのデータプレーンとして広く利用され、トラフィックルーティング、負荷分散、メトリクス収集などを担当します。
*   **Gateway API:** KubernetesのネットワーキングAPIで、Ingressの進化版として、より柔軟で拡張性の高いL4/L7ロードバランシング機能を提供します。
*   **GCP-2026-057:** Google Cloudが公開するセキュリティ脆弱性情報の識別子。通常、関連する脆弱性の詳細や影響、対処方法が記載されたドキュメントへのリンクとなります。

---

# Google Kubernetes Engine

## Change
**原文:**
```
GKE version 1.35.1-gke.1031000 and later include the following changes to automatically created firewall rules for Services:

[automatically created firewall rules for Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws)
- Changes the priority of multiple existing firewall rules for Services from `1000` to `999`.
- Creates additional firewall rules to deny traffic that is not explicitly allowed by other auto-created firewall rules.

If you use custom firewall rules to override GKE firewall rules for Services, these changes might cause unexpected behavior. Before you upgrade your clusters to version 1.35.1-gke.1031000 or later, do the following:

- If you have custom firewall rules that allow or deny traffic with a priority of `1000`, change the priority of those rules to a numerically lower value (such as `999` or lower) to maintain their precedence.
- Verify that the new auto-created deny rules do not block required traffic for load balancers that use external IP addresses.
```

**説明:**
GKE（Google Kubernetes Engine）のバージョン 1.35.1-gke.1031000 以降で、GKEが自動的に作成するサービス用ファイアウォールルールに以下の変更が導入されます。
1.  既存の複数のサービス用ファイアウォールルールの優先度が `1000` から `999` に変更されます。
2.  GKEが自動作成する他のファイアウォールルールによって明示的に許可されていないトラフィックを拒否する、追加のファイアウォールルールが作成されます。

これらの変更は、GKEの自動生成ファイアウォールルールをカスタムルールで上書きしている場合に、予期せぬ動作を引き起こす可能性があります。

**影響有無:**
*   **GKEを利用しており、かつGKEが自動生成するファイアウォールルールに対してカスタムファイアウォールルールを適用している場合:** 影響があります。
    *   もしカスタムファイアウォールルールで優先度 `1000` を使用している場合、GKEの自動生成ルール（優先度999）が先に評価され、意図した動作と異なる可能性があります。
    *   新しく追加される「拒否」ルールが、外部IPアドレスを使用するロードバランサー（例：External Load Balancer）に必要なトラフィックを誤ってブロックする可能性があります。
*   **GKEを利用しているが、GKEが自動生成するファイアウォールルールをカスタムルールで上書きしていない場合:** 通常、直接的な影響はありません。GKEの推奨設定に従っている限り問題ないと考えられます。
*   **GKEを利用していない場合:** 影響はありません。
*   **Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3) について:** Cloud Composerは内部的にGKEを利用していますが、Composer環境のネットワーク設定（ファイアウォールルールを含む）はGoogle Cloudによってマネージドされています。ユーザーが直接GKEクラスターのファイアウォールルールをカスタマイズすることは想定されていません。したがって、このGKEの変更がお客様のComposer環境に直接的な影響を与える可能性は極めて低いと考えられます。

**対処方法:**
*   **GKEを利用しており、かつカスタムファイアウォールルールを適用している場合:**
    1.  GKEクラスターをバージョン 1.35.1-gke.1031000 以降にアップグレードする前に、お客様が作成したカスタムファイアウォールルールで優先度 `1000` を使用しているものがある場合、それらのルールの優先度を **`999` よりも小さい数値（例：`998` 以下）** に変更し、既存の優先順位を維持するように調整してください。
    2.  アップグレード後、またはテスト環境で、新しく自動生成される拒否ルールが、外部IPアドレスを持つロードバランサーに必要なトラフィックを誤ってブロックしないことを確認してください。必要に応じて、特定のトラフィックを許可するカスタムルールを、より高い優先度（数値の小さい優先度）で追加することを検討してください。
*   **上記以外の場合:** 特段の対処は不要です。

**用語説明:**
*   **ファイアウォールルール:** ネットワークトラフィックの送信元、宛先、プロトコル、ポートなどに基づいて、トラフィックを許可または拒否するための設定です。Google CloudではVPCネットワークに適用されます。
*   **優先度 (Priority):** ファイアウォールルールが評価される順序を示す数値です。数値が小さいほど優先度が高く、同じトラフィックに複数のルールが適用される場合、最も優先度の高いルール（数値が最も小さいルール）が適用されます。
*   **Services (Kubernetes):** Kubernetesにおける`Service`リソースは、Podのセットへの安定したネットワークアクセスを提供する抽象化です。クラスタ内でのPod間の通信や、外部からのPodへのアクセスを管理するために使用されます。
*   **ロードバランサー (Load Balancer):** 複数のバックエンド（この場合、GKEのPodやVMインスタンス）にネットワークトラフィックを分散させるためのコンポーネントです。GKEでは、`Service`リソースの種類（`LoadBalancer`タイプなど）に応じて、Google Cloudのロードバランサーが自動的にプロビジョニングされることがあります。
# Title: August 31, 2026 
Link: https://docs.cloud.google.com/release-notes#August_31_2026<br>
Google Cloudのリリースノートに対する調査結果を以下に示します。

---

# BigQuery

## Fixed
原文: Support for configuring daily token quotas for BigQuery generative AI functions has been restored.
[configuring daily token quotas](https://docs.cloud.google.com/bigquery/docs/control-genai-costs)

説明: BigQueryの生成AI機能（例: `GENERATE_TEXT` 関数など）で使用されるトークンに対して、1日あたりの上限（クォータ）を設定する機能が以前利用できない状態でしたが、この機能が復旧しました。これにより、生成AI機能の利用コストを適切に管理するための設定が再び可能になります。

影響有無:
*   **影響あり**: BigQueryの生成AI機能を利用しており、コスト管理のために日次トークンクォータを設定していた、または設定を検討していたユーザーには影響があります。この機能が復旧したことで、以前は設定できなかったクォータ管理が可能になります。
*   **影響なし**: BigQueryの生成AI機能を利用していない場合、直接的な影響はありません。

対処方法:
BigQueryの生成AI機能を利用している場合は、コスト管理のために日次トークンクォータの設定状況を確認し、必要に応じて設定を適用または調整してください。特に、この機能が利用できなかった期間にクォータを設定しようとしていた場合は、改めて設定を試みてください。

用語説明:
*   **BigQuery generative AI functions**: BigQuery MLを通じて利用できる、Googleの基盤モデル（例: Gemini, PaLM 2）を活用して、SQLクエリ内でテキスト生成、要約、分類などの生成AIタスクを実行するための関数群。
*   **Daily token quotas**: BigQueryの生成AI関数が消費するトークン（言語モデルの入力および出力の最小単位）の1日あたりの使用量に設定できる上限。これにより、予期せぬ高コストの発生を抑制し、コストを制御することが可能になります。

---

# Cloud Service Mesh

## Announcement
原文: **1.30.4-asm.1 is now available for in-cluster Cloud Service Mesh.** You can now download 1.30.4-asm.1 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.30.4 subject to the list of supported features. The following are not supported: Failover Priority support for DNS clusters, `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`, Multiple `CUSTOM` external authorization providers per workload, The `DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES` flag. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.30.4-asm.1 uses Envoy v1.38.4-dev.
[Istio 1.30.4](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/)
[supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: Cloud Service Mesh (CSM) のインクラスタデプロイメント向けに、新バージョン1.30.4-asm.1がリリースされました。このバージョンはIstio 1.30.4の機能をベースとしていますが、一部のIstio機能（DNSクラスタのフェイルオーバー優先度サポート、特定のTLSエントリ、複数のカスタム外部認証プロバイダ、特定のデバッグフラグ）はサポート対象外です。また、このバージョンはEnvoy v1.38.4-devを使用しています。既存のCloud Service Meshユーザーは、この新バージョンへのアップグレードを検討できます。

影響有無:
*   **影響あり**: Cloud Service Meshを既存で利用しているユーザー、特にバージョンアップを検討しているユーザーにとっては、新しい機能やバグ修正の恩恵を受ける機会となります。ただし、サポート対象外として明記されたIstio機能を利用している、または利用を計画している場合は、その機能がCSMでは提供されないため、設計の見直しが必要になる可能性があります。
*   **影響なし**: Cloud Service Meshを現在利用していない場合、直接的な影響はありません。Google Cloud Composer 2 (2.7.1) は直接Cloud Service Meshを利用するサービスではないため、今回のリリースによる直接的な影響はございません。

対処方法:
Cloud Service Meshを利用している場合は、新しいバージョン1.30.4-asm.1へのアップグレードを検討してください。アップグレードを行う前に、現在の構成や利用している機能が新しいバージョンと互換性があるか、特に今回明記された「サポートされない機能」が自身のユースケースに影響しないかを確認することが重要です。アップグレード手順の詳細は提供されたドキュメント「Upgrade Cloud Service Mesh」を参照してください。

用語説明:
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供するマネージドなサービスメッシュプラットフォーム。オープンソースのIstioをベースにしており、Kubernetesクラスタ内外にデプロイされたサービス間のトラフィック管理、セキュリティポリシー適用、可観測性（モニタリング・ロギング・トレーシング）を提供します。
*   **In-cluster Cloud Service Mesh**: Cloud Service Meshのコントロールプレーンとデータプレーンが、ユーザーのGoogle Kubernetes Engine (GKE) クラスタ内にデプロイされる運用モデル。
*   **Istio**: マイクロサービス間の通信を制御、保護、監視するためのオープンソースのサービスメッシュ。プロキシとしてEnvoyを使用し、サービス間のトラフィックをインターセプト・制御します。
*   **Envoy**: 高性能なオープンソースのL7プロキシおよび通信バス。Istioのデータプレーンとして機能し、サイドカープロキシとして各サービスにデプロイされ、全てのネットワークトラフィックを処理します。

---

## Announcement
原文: In-cluster Cloud Service Mesh 1.27 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明: Cloud Service Meshのインクラスタデプロイメント向けバージョン1.27のサポートが終了しました。これにより、このバージョンを使用しているユーザーは、今後のセキュリティパッチ、バグ修正、およびGoogleからのテクニカルサポートを受けられなくなります。他のバージョンのサポート終了日については、提供されている「Supported versions」ドキュメントで確認できます。

影響有無:
*   **影響あり**: Cloud Service Meshバージョン1.27を現在利用しているユーザーは、直ちに影響を受けます。サポート終了により、セキュリティリスクの増大や問題発生時のサポート不可といったリスクが生じます。
*   **影響なし**: Cloud Service Meshバージョン1.27を利用していない場合、直接的な影響はありません。Google Cloud Composer 2 (2.7.1) は直接Cloud Service Meshを利用するサービスではないため、今回のリリースによる直接的な影響はございません。

対処方法:
Cloud Service Meshバージョン1.27を使用している場合は、**速やかにサポートされている最新バージョン（例: 今回リリースされた1.30.4-asm.1など）へのアップグレードを計画し、実行してください。** アップグレードの前に、現在の構成との互換性や、新しいバージョンでの変更点を確認することが重要です。サポートされているバージョンのリストと各バージョンのサポート終了日については、「Supported versions」ドキュメントを参照してください。

用語説明:
*   **End-of-Life (EOL)**: ソフトウェアやサービスのライフサイクルの最終段階。EOLに達すると、通常、ベンダーからのバグ修正、セキュリティアップデート、テクニカルサポートが提供されなくなります。継続して利用すると、セキュリティ上の脆弱性や予期せぬ動作のリスクが高まります。
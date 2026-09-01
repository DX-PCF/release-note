
# Title: August 31, 2026 
Link: https://docs.cloud.google.com/release-notes#August_31_2026<br>
はい、承知いたしました。
Google Cloudのリリースノートに基づき、各製品の変更点について影響調査と対応策を以下の通りご報告いたします。

---

# BigQuery

## Fixed

原文: Support for configuring daily token quotas for BigQuery generative AI functions has been restored.
[configuring daily token quotas](https://docs.cloud.google.com/bigquery/docs/control-genai-costs)

説明:
BigQueryの生成AI機能（`ML.GENERATE_TEXT` などのAI関数）において、日次トークン割り当て（Daily Token Quotas）を設定する機能が復旧しました。この機能は、生成AIの利用にかかるコストを制御するために、1日あたりのAIモデルのトークン使用量に上限を設定するものです。

影響有無:
影響は限定的ですが、ポジティブな影響です。
これまで生成AI機能のトークン割り当て設定が一時的に利用できなかった期間がありましたが、この変更により、ユーザーは再び生成AIの利用コストをきめ細かく制御できるようになります。

対処方法:
特別な対応は不要ですが、BigQueryの生成AI機能を多用しており、コスト管理のためにトークン割り当てを設定したい場合は、この機能を利用して適切なクォータを設定することを推奨します。

用語説明:
*   **BigQuery generative AI functions**: BigQuery MLの一部として提供される、Googleの生成AIモデル（例: Gemini, PaLM）をSQLインターフェースから直接利用できる機能群です。データの分析・変換と同時にAIモデルによるテキスト生成や要約などが可能です。
*   **Daily token quotas**: BigQueryの生成AI機能における、1日あたりのAIモデルが処理できるトークン（言語モデルにおける単語や記号などの最小単位）の総量に設定される上限です。これにより、意図しない大量利用によるコスト増大を防ぐことができます。

---

# Cloud Service Mesh

## Announcement

原文: 1.30.4-asm.1 is now available for in-cluster Cloud Service Mesh. You can now download 1.30.4-asm.1 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.30.4 subject to the list of supported features.
[Istio 1.30.4](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/)
[supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)
The following are not supported:
- Failover Priority support for DNS clusters
- `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`
- Multiple `CUSTOM` external authorization providers per workload
- The `DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES` flag
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.30.4-asm.1 uses Envoy v1.38.4-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明:
Cloud Service Mesh (in-clusterデプロイモード) の新バージョン `1.30.4-asm.1` がリリースされました。このバージョンは、オープンソースのIstio `1.30.4` の機能に基づいていますが、一部の機能（例: DNSクラスタのフェイルオーバー優先度サポート、特定のTLS設定、複数のカスタム外部認証プロバイダ、デバッグフラグ）はサポート対象外です。また、Envoyのバージョンは `v1.38.4-dev` が使用されています。

影響有無:
新しいバージョンが利用可能になったことで、以下の影響があります。
*   **ポジティブな影響**: Istio 1.30.4が持つ新機能や改善、セキュリティ修正、バグ修正などを利用できるようになります。これにより、サービスメッシュの機能性、信頼性、セキュリティが向上する可能性があります。
*   **検討が必要な影響**: 現在Cloud Service Meshを利用している場合、アップグレードを検討するタイミングとなります。ただし、サポート対象外となる機能が既存の構成で使用されていないか、事前に確認が必要です。

対処方法:
*   現行のCloud Service Meshのバージョンが`1.30.4-asm.1`よりも古い場合、アップグレードを検討してください。
*   アップグレード前に、リリースノートに記載されている「サポートされない機能」が現在の環境で利用されていないか確認し、影響がないことを検証してください。
*   アップグレード手順については、提供されている[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)ドキュメントを参照し、計画的に実施してください。
*   Istio 1.30.4の[リリースノート](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/)も確認し、追加の変更点や考慮事項がないか把握してください。

用語説明:
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供するマネージドなサービスメッシュソリューションで、Istioをベースに構築されています。サービス間のトラフィック管理、セキュリティ、可観測性を提供します。
*   **in-cluster Cloud Service Mesh**: サービスメッシュのコントロールプレーンをユーザーのGKEクラスタ内にデプロイし、ユーザー自身が管理するデプロイメントモードです。
*   **Istio**: オープンソースのサービスメッシュプラットフォームです。Kubernetesクラスタ内のサービスにトラフィック管理、ポリシー適用、可観測性などの機能を追加します。
*   **Envoy**: Istioのデータプレーンとして広く利用される高性能なL7プロキシです。サービス間のすべてのネットワークトラフィックを処理します。

## Announcement

原文: In-cluster Cloud Service Mesh 1.27 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明:
Cloud Service Mesh (in-clusterデプロイモード) のバージョン `1.27` がサポート対象外となりました。これは、このバージョンに対するGoogle Cloudからのセキュリティパッチ、バグ修正、および技術サポートが提供されなくなることを意味します。

影響有無:
**Cloud Service Mesh 1.27を利用している環境では、直ちにアップグレードを検討する必要があります。**
サポートが終了したバージョンを使い続けることは、セキュリティリスクの増大、既知のバグ修正の未適用、および将来的な問題発生時のベンダーサポートの欠如につながります。

対処方法:
*   現在Cloud Service Mesh `1.27` を利用している場合は、速やかにサポートされているバージョン（例: 今回アナウンスされた `1.30.4-asm.1` など）へのアップグレードを計画し、実行してください。
*   アップグレードの計画にあたっては、Cloud Service Meshの[サポートされているバージョン](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)のドキュメントを参照し、ターゲットとするバージョンのEOL（End-of-Life）スケジュールも確認してください。
*   アップグレード手順については、公式ドキュメント[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)を参照してください。

用語説明:
*   **サポート対象外 (No longer supported)**: ソフトウェアやサービスの特定のバージョンに対して、ベンダーからの公式なメンテナンス（セキュリティパッチ、バグ修正、機能強化）や技術サポートが提供されなくなる状態を指します。
*   **End-of-Life (EOL)**: ソフトウェア製品やバージョンのライフサイクルが終了し、サポートが完全に停止する日付を指す用語です。EOLを過ぎたソフトウェアは、セキュリティ上の脆弱性が発見されても修正が提供されないため、利用を継続することは推奨されません。
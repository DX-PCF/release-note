
# Title: September 03, 2026 
Link: https://docs.cloud.google.com/release-notes#September_03_2026<br>
Google Cloud インフラエンジニアとして、API Gatewayのリリースノートについて調査し、以下の通りご報告いたします。

---

# API Gateway
## Change
原文: release note.
```
 New model routing gateways might use a gateway.dev default hostname

 If you create a gateway that uses model routing on or after September 3, 2026, it
might receive a gateway.dev default hostname instead of a run.app one, in the
form https://GATEWAY_ID-PROJECT_NUMBER.REGION.gateway.dev — for example, https://my-gateway-123456789012.us-central1.gateway.dev. This is a second gateway.dev format; other gateways keep the existing one.

 To get a gateway's URL, read its defaultHostname property.

 For more information, see Deploy an API to a gateway.

[Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api)
```
説明：
2026年9月3日以降にモデルルーティングを使用するAPI Gatewayを新規作成する場合、デフォルトのホスト名が `run.app` ドメインではなく、新しい形式の `gateway.dev` ドメインになる可能性があります。新しいホスト名の形式は `https://GATEWAY_ID-PROJECT_NUMBER.REGION.gateway.dev` となります。これは、既存の `gateway.dev` ドメインとは異なる、2つ目の `gateway.dev` フォーマットとして導入されます。既存のゲートウェイのホスト名に変更はありません。ゲートウェイのURLは、`defaultHostname` プロパティから取得できます。

影響有無：
**影響なし**
*   **既存のサービスへの影響はありません。** この変更は、2026年9月3日以降にモデルルーティングを利用して新規作成されるAPI Gatewayにのみ適用されます。既存のAPI Gatewayのホスト名が自動的に変更されることはありません。
*   既存のAPI Gatewayを使用しているシステムにおいては、ホスト名の変更に伴う設定変更やコード修正は不要です。

対処方法：
**特段の対処は不要です。**
*   将来的に新しいAPI Gatewayをデプロイする際、この変更が適用される可能性があることを認識しておいてください。
*   API GatewayのURLをハードコードするのではなく、API Gatewayの`defaultHostname` プロパティから動的に取得することを推奨します。これにより、将来的なホスト名フォーマットの変更にも柔軟に対応できます。

用語説明：
*   **API Gateway (API ゲートウェイ)**: バックエンドサービスへのアクセスを管理し、ルーティング、認証、レート制限などを提供するサービスです。
*   **Model Routing (モデルルーティング)**: OpenAPI SpecificationなどのAPI定義に基づいて、API Gatewayが受信したリクエストをどのバックエンドサービスにルーティングするかを決定する機能です。
*   **Hostname (ホスト名)**: インターネット上のサーバーやリソースを一意に識別するための名前です。URLの一部を構成します。
*   **defaultHostname (デフォルトホスト名)**: Google Cloudがサービスに対して自動的に割り当てる標準のホスト名です。
*   **run.app**: Google Cloudの特定のサービス（例: Cloud Run）でデフォルトのURLとして使用されるドメインです。
*   **gateway.dev**: API GatewayサービスでデフォルトのURLとして使用されるドメインです。今回の変更で、このドメインの新しい形式が追加されます。
# Title: September 02, 2026 
Link: https://docs.cloud.google.com/release-notes#September_02_2026<br>
## BigQuery
### Change
原文: An updated version of the Simba JDBC driver for BigQuery is now available.
[Simba JDBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_jdbc_driver)

説明：
BigQuery に接続するための Simba JDBC ドライバの更新版がリリースされ、利用可能になりました。この更新には、パフォーマンスの改善やバグ修正が含まれている可能性があります。

影響有無：
**影響なし（直接的な影響）**
この変更は BigQuery サービス自体ではなく、BigQuery へ接続するアプリケーションが使用する JDBC ドライバの更新です。既存の BigQuery サービスやデータに直接的な影響はありません。

対処方法：
現在 BigQuery に JDBC ドライバを使用して接続しているアプリケーションがある場合、最新版のドライバへのアップデートを検討してください。アップデートにより、パフォーマンスの向上や安定性の改善が見込まれます。アップデートを実施する際は、既存のアプリケーションとの互換性を十分にテストしてください。

用語説明：
*   **JDBC ドライバ (Java Database Connectivity driver)**: Java アプリケーションからデータベースに接続し、データ操作を行うための標準的な API (Application Programming Interface) を提供するソフトウェアコンポーネントです。BigQuery 用の Simba JDBC ドライバは、Java アプリケーションが BigQuery に接続できるようにします。

## Google Kubernetes Engine
### Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

### No channel (deprecated)
原文:
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.7-gke.1150000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.34.11-gke.1044000
    - 1.35.8-gke.1225000
    - 1.36.4-gke.1082000
- The following node versions are now available:
    - 1.31.14-gke.2667000
    - 1.32.13-gke.2393000
    - 1.33.13-gke.1613000
    - 1.34.11-gke.1044000
    - 1.35.8-gke.1225000
    - 1.36.4-gke.1082000
- The following versions are no longer available:
    - 1.34.9-gke.1610001 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.35.6-gke.1710000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.35.8-gke.1026000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.36.2-gke.2064000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.33 to 1.34.9-gke.1655001
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.34 to 1.34.9-gke.1655001
        - 1.35 to 1.35.7-gke.1150000
        - 1.36 to 1.36.3-gke.1537000

説明：
GKE クラスターのバージョンが更新され、新規クラスター作成および既存クラスターの手動アップグレード（コントロールプレーンおよびノード）で利用可能になりました。リリースノート公開時点でロールアウトが進行中であり、全 Google Cloud ゾーンに展開されるまでに数日かかる場合があります。
具体的には、「No channel」と記載されたクラスター（リリースチャネルを使用しない標準的なクラスター）において、バージョン `1.35.7-gke.1150000` がクラスター作成のデフォルトバージョンになりました。また、複数の新しいバージョン（例: `1.34.11-gke.1044000`、`1.35.8-gke.1225000`、`1.36.4-gke.1082000`）が利用可能になり、対応するノードバージョンも追加されました。
同時に、一部の古いバージョン（例: `1.34.9-gke.1610001`、`1.35.6-gke.1710000` など）が非推奨となり、90日以内、またはサポート終了時に削除される予定です。
自動アップグレードのターゲットバージョンも更新され、メンテナンス除外期間や非推奨 API の使用などの要因がなければ、クラスターは新しいマイナーバージョンやパッチバージョンにアップグレードされる可能性があります。

影響有無：
**影響あり（要確認）**
*   **既存クラスターのバージョン:** 現在運用中の GKE クラスターのバージョンが、今回非推奨となったバージョン（例: `1.34.9-gke.1610001` など）に含まれる場合、90日以内にアップグレードが必須となります。これを行わない場合、サポートが終了し、セキュリティリスクや機能停止のリスクが高まります。
*   **自動アップグレード:** 自動アップグレードを有効にしている場合、クラスターは新たなターゲットバージョン（例: `1.33` から `1.34.9-gke.1655001` など）へ自動的にアップグレードされる可能性があります。このアップグレードにより、アプリケーションの互換性問題が発生しないか、事前にテスト環境で確認することが推奨されます。
*   **Google Cloud Composer 2:** Google Cloud Composer 2 (Compoer version 2.7.1、Airflow version 2.7.3) は GKE 上で動作するマネージドサービスです。Composer の GKE 基盤バージョンは Google によって管理されますが、今回の GKE バージョン更新が Composer の基盤バージョンに影響を及ぼす可能性があります。Composer の基盤 GKE バージョンが自動的にアップグレードされる場合、Airflow の特定のオペレーターやカスタムコードが新しい Kubernetes バージョンと互換性があるか確認が必要です。ただし、Composer は安定性を重視するため、最新の GKE バージョンがすぐに適用されるわけではありません。Composer の公式ドキュメントやリリースノートでサポートされる GKE バージョン範囲を確認してください。現時点では、直接的な非互換性の報告はありません。

対処方法：
1.  **既存 GKE クラスターの確認:** 現在使用している GKE クラスターのバージョンを確認し、非推奨リストに含まれる場合は、速やかにアップグレード計画を策定し実行してください。アップグレード前に、テスト環境でアプリケーションの動作確認を行うことを強く推奨します。
2.  **自動アップグレード設定の確認:** 自動アップグレードを有効にしている場合、メンテナンスウィンドウや除外設定を確認し、計画外のアップグレードを避けるための適切な設定が行われているか確認してください。
3.  **Google Cloud Composer 2:** Composer インスタンスの基盤となる GKE バージョンの変更が通知された場合、Composer のドキュメントや Airflow の変更履歴を参照し、既存の DAG やカスタムコードが新しい GKE/Kubernetes バージョンと互換性があるか確認してください。通常、Composer は後方互換性を保つように設計されていますが、重要なマイナーバージョンアップグレードには注意が必要です。

用語説明：
*   **GKE クラスターバージョン (GKE Cluster Versions)**: Google Kubernetes Engine (GKE) のクラスターが使用する Kubernetes のバージョンとその GKE 固有のパッチバージョンを指します。
*   **コントロールプレーン (Control Plane)**: Kubernetes クラスターの頭脳となる部分で、API サーバー、スケジューラー、コントローラーマネージャーなどが含まれます。
*   **ノード (Node)**: Kubernetes クラスターのワーカーマシンで、コンテナ化されたアプリケーション（Pod）が実際に実行される仮想マシンまたは物理マシンです。
*   **非推奨 (Deprecated)**: 将来的にサポートが終了し、削除される予定の機能やバージョンを指します。非推奨とされたものは、新しいものに移行することが推奨されます。
*   **自動アップグレードターゲット (Auto-upgrade targets)**: GKE の自動アップグレード機能が、クラスターをアップグレードする際の目標となるバージョンです。
*   **メンテナンス除外 (Maintenance Exclusions)**: GKE クラスターの自動メンテナンス（アップグレードなど）が実行されない期間をユーザーが設定できる機能です。
*   **非推奨 API (Deprecated APIs)**: Kubernetes のバージョンアップに伴い、使用が推奨されなくなった API です。これらの API を使用しているアプリケーションは、新しい API に移行する必要があります。

### Security
原文:
This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:
| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.31.14-gke.2667000 | cos-117-18613-675-64 | [cos-117-18613-675-64 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-675-64_) |
| 1.32.13-gke.2393000 | cos-121-18867-584-3 | [cos-121-18867-584-3 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-584-3_) |
| 1.35.8-gke.1225000 | cos-125-19216-532-135 | [cos-125-19216-532-135 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-532-135_) |
| 1.36.4-gke.1082000 | cos-129-19506-299-161 | [cos-129-19506-299-161 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#cos-129-19506-299-161_) |
| 1.37.0-gke.2155000 | cos-129-19506-299-82 | [cos-129-19506-299-82 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#cos-129-19506-299-82_) |

説明：
この GKE リリースには、更新された Container-Optimized OS (COS) イメージを使用する新しい GKE バージョンが含まれています。これらの更新されたイメージは、前回の GKE リリース以降に公開されたすべての COS バージョンからの累積的なセキュリティ修正を含んでいます。各 COS イメージで解決された特定の脆弱性については、リンク先のリリースノートで確認できます。

影響有無：
**影響なし（ポジティブな影響）**
この変更は、GKE クラスターのセキュリティ体制を強化するものです。新しい GKE バージョンにアップグレードすることで、基盤となるノード OS のセキュリティ脆弱性が修正され、クラスターの全体的なセキュリティが向上します。既存のワークロードに直接的な悪影響はありません。

対処方法：
GKE クラスターのセキュリティを維持するため、定期的に GKE クラスターを最新のバージョンにアップグレードすることを推奨します。自動アップグレードを有効にすることで、これらのセキュリティ修正が自動的に適用されるようになります。アップグレード前に、テスト環境でアプリケーションの互換性テストを実施してください。

用語説明：
*   **Container-Optimized OS (COS)**: Google Cloud が提供する、コンテナの実行に最適化された軽量なオペレーティングシステムです。GKE クラスターのノードイメージとして使用されます。
*   **セキュリティ修正 (Security Fixes)**: ソフトウェアの脆弱性（セキュリティホール）を修正するためのパッチやアップデートです。

### Change (Stable Channel)
原文:
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.10-gke.1079000 is now available in the Stable channel.
- Version 1.34.9-gke.1610001 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.33 to 1.34.9-gke.1655001
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.34 to 1.34.9-gke.1655001

説明：
GKE の Stable チャネルにおいて、バージョン `1.34.10-gke.1079000` が利用可能になりました。同時に、バージョン `1.34.9-gke.1610001` が Stable チャネルで非推奨となり、90日以内、またはサポート終了時に削除されます。このチャネルで稼働しているクラスターは、新たな自動アップグレードターゲットにアップグレードされる可能性があります。

影響有無：
**影響あり（要確認）**
*   **既存 Stable チャネルクラスター:** 現在 Stable チャネルで `1.34.9-gke.1610001` を使用しているクラスターは、90日以内にアップグレードが必要となります。
*   **自動アップグレード:** Stable チャネルで自動アップグレードを有効にしている場合、クラスターは `1.34.9-gke.1655001` などの新しいパッチバージョンまたはマイナーバージョンに自動的にアップグレードされる可能性があります。アップグレード時の互換性リスクを評価するため、アプリケーションのテストが推奨されます。
*   **Google Cloud Composer 2:** Composer インスタンスの基盤GKEバージョンがStableチャネルを使用している可能性は低いですが、Googleが管理するGKEバージョンポリシーに変更がないかComposerのリリースノートを確認するのが最善です。

対処方法：
Stable チャネルで GKE クラスターを運用している場合は、クラスターのバージョンを確認し、非推奨バージョンを使用している場合は速やかにアップグレードを計画・実行してください。自動アップグレードを有効にしている場合は、メンテナンスウィンドウの設定を確認し、アップグレードによる影響を最小限に抑えるための対策を検討してください。

用語説明：
*   **Stable チャネル (Stable Channel)**: GKE のリリースチャネルの一つで、最も安定性が高く、エンタープライズ向けのワークロードに適しています。新機能の導入は他のチャネルに比べて遅めです。

### Change (Regular Channel)
原文:
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.7-gke.1150000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
    - 1.34.10-gke.1236000
    - 1.35.7-gke.1222000
    - 1.36.3-gke.1640000
- The following versions are no longer available in the Regular channel:
    - 1.34.10-gke.1079000
    - 1.35.7-gke.1027000
    - 1.36.2-gke.2064000 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.33 to 1.34.10-gke.1106000
        - 1.34 to 1.35.7-gke.1150000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.34 to 1.34.10-gke.1106000
        - 1.35 to 1.35.7-gke.1150000
        - 1.36 to 1.36.3-gke.1537000

説明：
GKE の Regular チャネルにおいて、バージョン `1.35.7-gke.1150000` が新規クラスター作成のデフォルトバージョンになりました。複数の新しいバージョンが利用可能になり、一部の古いバージョンが利用不可（非推奨を含む）になりました。特に `1.36.2-gke.2064000` は非推奨となり、90日以内に削除されます。自動アップグレードターゲットも更新されています。

影響有無：
**影響あり（要確認）**
*   **既存 Regular チャネルクラスター:** 現在 Regular チャネルで `1.36.2-gke.2064000` を使用しているクラスターは、90日以内にアップグレードが必要となります。
*   **自動アップグレード:** Regular チャネルで自動アップグレードを有効にしている場合、クラスターは `1.33` から `1.34.10-gke.1106000` へのマイナーバージョンアップグレード、またはパッチバージョンアップグレード（例: `1.34` から `1.34.10-gke.1106000`）が適用される可能性があります。
*   **Google Cloud Composer 2:** Composer インスタンスの基盤GKEバージョンがRegularチャネルを使用している可能性は低いですが、Googleが管理するGKEバージョンポリシーに変更がないかComposerのリリースノートを確認するのが最善です。

対処方法：
Regular チャネルで GKE クラスターを運用している場合は、クラスターのバージョンを確認し、非推奨バージョンを使用している場合は速やかにアップグレードを計画・実行してください。自動アップグレードによる影響を考慮し、アプリケーションの互換性テストを事前に行うことを推奨します。

用語説明：
*   **Regular チャネル (Regular Channel)**: GKE のリリースチャネルの一つで、Stable チャネルより新しい機能をより早く利用できますが、Stable より検証期間が短くなります。

### Change (Rapid Channel)
原文:
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.36.3-gke.1767000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
    - 1.34.11-gke.1044000
    - 1.35.8-gke.1225000
    - 1.36.4-gke.1082000
    - 1.37.0-gke.2155000
    - 1.37.0-gke.2941000
- The following versions are no longer available in the Rapid channel:
    - 1.34.10-gke.1236000
    - 1.35.7-gke.1222000
    - 1.35.8-gke.1026000 is deprecated in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.36.3-gke.1640000
- The following alpha versions are no longer available in the Rapid channel:
    - 1.37.0-gke.2034000+preview
    - 1.37.0-gke.2048000+preview
    - 1.37.0-gke.2074000+preview
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.33 to 1.34.10-gke.1328000
        - 1.34 to 1.35.8-gke.1036000
        - 1.35 to 1.36.3-gke.1767000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.34 to 1.34.10-gke.1328000
        - 1.35 to 1.35.8-gke.1036000
        - 1.36 to 1.36.3-gke.1767000
        - 1.37 to 1.37.0-gke.2155000

説明：
GKE の Rapid チャネルにおいて、バージョン `1.36.3-gke.1767000` が新規クラスター作成のデフォルトバージョンになりました。複数の最新バージョン（例: `1.37.0-gke.2155000` など）が利用可能になり、一部の古いバージョンが利用不可（非推奨を含む）になりました。特に `1.35.8-gke.1026000` は非推奨となり、90日以内に削除されます。プレビュー版のアルファバージョンも利用不可となりました。自動アップグレードターゲットも更新されています。

影響有無：
**影響あり（要確認）**
*   **既存 Rapid チャネルクラスター:** 現在 Rapid チャネルで `1.35.8-gke.1026000` を使用しているクラスターは、90日以内にアップグレードが必要となります。Rapid チャネルは最新機能が提供される一方で、変更頻度が高く、非推奨化も早いため、継続的なバージョン管理が重要です。
*   **自動アップグレード:** Rapid チャネルで自動アップグレードを有効にしている場合、クラスターは新しいマイナーバージョンやパッチバージョンに積極的にアップグレードされます。これにより、アプリケーションの互換性問題が発生するリスクが他のチャネルよりも高いため、入念なテストが不可欠です。
*   **Google Cloud Composer 2:** Google Cloud ComposerはRapidチャネルのGKEバージョンを基盤として採用することは通常ありません。したがって、直接的な影響は極めて低いと考えられます。

対処方法：
Rapid チャネルで GKE クラスターを運用している場合は、クラスターのバージョンを常に最新に保つことを検討してください。非推奨バージョンを使用している場合は速やかにアップグレードを計画・実行し、最新バージョンへの自動アップグレードに備えて、定期的にアプリケーションの互換性テストを実施する CI/CD パイプラインを構築することを推奨します。

用語説明：
*   **Rapid チャネル (Rapid Channel)**: GKE のリリースチャネルの一つで、最新の機能を最も早く利用できます。ただし、変更頻度が高く、安定性は他のチャネルに比べて低いため、開発環境や新しい技術の先行導入に適しています。

### Change (Extended Channel)
原文:
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.7-gke.1150000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.31.14-gke.2613000
    - 1.31.14-gke.2667000
    - 1.32.13-gke.2314000
    - 1.32.13-gke.2393000
    - 1.33.13-gke.1499000
    - 1.33.13-gke.1613000
    - 1.34.10-gke.1236000
    - 1.35.7-gke.1222000
    - 1.36.3-gke.1640000
- The following versions are no longer available in the Extended channel:
    - 1.31.14-gke.2543000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.31.14-gke.2630000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.32.13-gke.2231000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.32.13-
# Title: September 01, 2026 
Link: https://docs.cloud.google.com/release-notes#September_01_2026<br>
Google Cloud のインフラエンジニアとして、提供されたリリースノートを基に、構築済みのサービスへの影響調査結果を報告します。

---

# Cloud SDK
## Change
原文: (詳細な変更内容がリリースノートに記載されていません)

説明：
Cloud SDKに関するリリースノートの項目はありますが、具体的な変更内容が原文に記載されていません。そのため、このリリースサイクルにおける詳細な変更点は不明です。

影響有無：
不明。リリースノートに詳細な変更内容が記載されていないため、現状では構築済みのサービスへの影響有無を判断できません。

対処方法：
特になし。今後のリリースノートや公式ドキュメントで詳細が公開された際に改めて確認が必要です。

用語説明：
*   **Cloud SDK**: Google Cloud Platformと対話するためのコマンドラインツール、ライブラリ、およびその他のユーティリティのセット。

---

# Cloud Service Mesh
## Security
原文:
Managed Cloud Service Mesh will start using proxy version csm_mesh_proxy.20260819_RC00 for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.37. This change is rolling out to all release channels and contains the fix for the managed Cloud Service Mesh security vulnerabilities listed in GCP-2026-057.
[GCP-2026-057](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057)

説明：
マネージドCloud Service Meshが、GKEクラスター上のGateway API向けに新しいプロキシバージョン `csm_mesh_proxy.20260819_RC00` の使用を開始します。このプロキシバージョンは、Envoyのバージョン1.37に最も近いものとなります。この変更はすべてのリリースチャネルに展開され、`GCP-2026-057` で開示されているマネージドCloud Service Meshのセキュリティ脆弱性に対する修正が含まれています。

影響有無：
**影響あり（ポジティブな影響）**
本変更はセキュリティ脆弱性の修正を含むアップデートであり、マネージドサービスであるCloud Service Meshのプロキシが自動的に更新されます。これにより、お客様のサービスは強化されたセキュリティ状態で運用されることになります。
特に、GKE上でGateway APIを利用しており、Cloud Service Meshを導入している環境にとっては、自動的にセキュリティが向上します。

対処方法：
**特になし**
マネージドサービスであるため、お客様側で特別な操作や設定変更は不要です。更新はGoogle Cloudによって自動的に適用されます。`GCP-2026-057` の詳細を確認し、脆弱性の内容を把握しておくことを推奨します。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するフルマネージドのサービスメッシュソリューション。Istioベースで、GKEワークロードのトラフィック管理、セキュリティ、可観測性を向上させます。
*   **Gateway API**: Kubernetesにおける次世代のネットワーキングAPIで、GKE Service Meshのコンポーネントとしても利用され、柔軟なイングレスおよびサービスメッシュ機能を可能にします。
*   **Envoy**: クラウドネイティブなアプリケーション向けに設計された高性能オープンソースエッジ/サービスプロキシ。サービスメッシュのデータプレーンとして広く使用されます。
*   **GKE**: Google Kubernetes Engineの略で、Google Cloudが提供するマネージドKubernetesサービスです。

---

# Google Kubernetes Engine
## Change
原文:
GKE version 1.35.1-gke.1031000 and later include the following changes to automatically created firewall rules for Services:
[automatically created firewall rules for Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws)
- Changes the priority of multiple existing firewall rules for Services from `1000` to `999`.
- Creates additional firewall rules to deny traffic that is not explicitly allowed by other auto-created firewall rules.
If you use custom firewall rules to override GKE firewall rules for Services, these changes might cause unexpected behavior. Before you upgrade your clusters to version 1.35.1-gke.1031000 or later, do the following:
- If you have custom firewall rules that allow or deny traffic with a priority of `1000`, change the priority of those rules to a numerically lower value (such as `999` or lower) to maintain their precedence.
- Verify that the new auto-created deny rules do not block required traffic for load balancers that use external IP addresses.

説明：
GKEバージョン1.35.1-gke.1031000以降において、GKE Services向けに自動作成されるファイアウォールルールに以下の変更が導入されます。
1.  Services用の既存の複数のファイアウォールルールの優先度が `1000` から `999` に変更されます。
2.  他の自動作成ファイアウォールルールによって明示的に許可されていないトラフィックを拒否する、追加のファイアウォールルールが作成されます。
もしお客様がGKEの自動作成ファイアウォールルールを上書きするためにカスタムファイアウォールルールを使用している場合、これらの変更によって予期せぬ動作が発生する可能性があります。

影響有無：
**影響あり（潜在的に非互換性）**
GKEの自動作成ファイアウォールルールの優先度変更と、新しい拒否ルールの追加は、既存のネットワーク構成、特にカスタムファイアウォールルールを使用している環境に直接影響を与える可能性があります。

*   **機能の変更**: GKE Servicesに関連するファイアウォールルールの動作が変わります。
*   **非互換性**:
    *   もしお客様の環境で、自動作成されるGKEファイアウォールルールを上書きする目的で、優先度 `1000` のカスタムファイアウォールルール（許可または拒否）を設定している場合、GKEの自動ルールが `999` に変更されることで、カスタムルールよりもGKEの自動ルールが優先されてしまう可能性があります（数値が低いほど優先度が高い）。
    *   新しく追加される「明示的に許可されていないトラフィックを拒否するルール」が、意図しない必要な通信（特に外部IPアドレスを持つロードバランサーへのトラフィックなど）をブロックする可能性があります。
*   **Cloud Composer 2への影響**: Composer 2はGKE上で動作します。Composer 2.7.1のGKEバージョンが、将来的にこの変更を含むバージョン (1.35.1-gke.1031000以降) にアップグレードされる可能性があります。通常、ComposerはマネージドサービスとしてGKEクラスターのバージョンアップをGoogleが管理しますが、ユーザーがComposer環境に関連付けられたGKEクラスターに対してカスタムファイアウォールルールを適用している場合、この変更の影響を受ける可能性があります。Composerのベストプラクティスとしては、Composerが管理するGKEクラスターにカスタムファイアウォールルールを直接適用することは推奨されませんが、 VPC Service Controlsなどのネットワーク境界設定において、間接的に影響を受ける可能性も考慮すべきです。

対処方法：
GKEクラスターをバージョン1.35.1-gke.1031000以降にアップグレードする前に、以下の対応を**必ず実施**してください。

1.  **カスタムファイアウォールルールの優先度確認と変更**:
    *   Google Cloud Console、`gcloud` コマンド、またはTerraformなどのIaCツールで、プロジェクト内の既存のファイアウォールルールを確認してください。
    *   もし、GKE Servicesに関連する目的で、優先度 `1000` のカスタムファイアウォールルール（許可または拒否）が存在する場合、その優先度を**数値的に低い値**（例: `999` 以下）に変更し、既存の優先度関係を維持してください。
2.  **新規拒否ルールによる影響の検証**:
    *   外部IPアドレスを使用するロードバランサー（例: GKE Ingressによって作成された外部ロードバランサー）など、外部からのアクセスが必要なサービスについて、新しい自動作成拒否ルールがそのトラフィックを誤ってブロックしないことを検証してください。
    *   可能であれば、本番環境アップグレード前にStaging環境などで影響を十分にテストしてください。
3.  **Cloud Composer 2をご利用の場合**:
    *   Composerの環境でカスタムファイアウォールルールを直接設定しているケースは稀ですが、もし設定されている場合は上記と同様の確認と対応が必要です。
    *   Composer環境のGKEバージョンアップはGoogle側で管理されるため、この変更による意図しない通信断が発生しないよう、ネットワークのアクセスパターンを再確認し、必要であればGoogle Cloudサポートに相談することも検討してください。

用語説明：
*   **ファイアウォールルール**: Google CloudのVPCネットワークにおいて、仮想マシンインスタンスとの間で送受信されるトラフィックを許可または拒否するためのルールセットです。
*   **優先度 (Priority)**: ファイアウォールルールが評価される順序を決定する数値です。数値が低いほど優先度が高く、先に評価・適用されます。同じトラフィックに複数のルールが適用される場合、最も優先度の高い（数値が低い）ルールが適用されます。
*   **GKE Services**: Kubernetesの `Service` リソースによって定義されるネットワークサービスに対応する、Google Cloudのロードバランサー、内部IPアドレス、DNSエントリなど。
*   **カスタムファイアウォールルール**: GKEが自動で作成するルールとは別に、ユーザーが手動で作成・管理するファイアウォールルール。
# Title: August 31, 2026 
Link: https://docs.cloud.google.com/release-notes#August_31_2026<br>
Google Cloudのリリースノートに基づき、構築済みのサービスへの影響調査結果を報告します。

---

# BigQuery

## Fixed
原文: Support for configuring daily token quotas for BigQuery generative AI functions has been restored.
[configuring daily token quotas](https://docs.cloud.google.com/bigquery/docs/control-genai-costs)

説明: BigQueryの生成AI（Generative AI）関数で、1日あたりのトークンクォータを設定する機能が復元されました。これまで設定ができなかった、あるいは設定しても適用されなかった不具合が修正されたことを意味します。これにより、生成AI関数の利用にかかる費用をより細かく制御できるようになります。

影響有無:
*   **影響あり（改善）**: BigQueryの生成AI機能を利用しており、コスト管理のために日次トークンクォータを設定したいと考えていた、または以前設定したが機能していなかったユーザーにとっては、この機能が利用可能になったため、費用管理の改善に繋がります。
*   **影響なし**: BigQueryの生成AI機能を利用していない場合、または日次トークンクォータの設定を必要としない場合には、直接的な影響はありません。

対処方法:
*   BigQueryの生成AI機能をご利用中で、トークン利用量に応じた費用を制御したい場合は、[configuring daily token quotas](https://docs.cloud.google.com/bigquery/docs/control-genai-costs) のドキュメントを参照し、必要に応じて日次トークンクォータの設定を見直してください。

用語説明:
*   **BigQuery**: Google Cloudが提供するフルマネージドなペタバイト規模のデータウェアハウスサービスです。SQLを用いて大量のデータを分析できます。
*   **生成AI関数 (Generative AI functions)**: BigQueryに組み込まれた、大規模言語モデル（LLM）などの生成AIモデルを利用するためのSQL関数です。テキスト生成、要約、分類などのタスクをデータウェアハウス内で直接実行できます。
*   **トークンクォータ (Token Quotas)**: 生成AIモデルの入力および出力の単位である「トークン」の利用量に設定される上限です。これにより、予期せぬ高額な料金発生を防ぎ、コストを管理できます。

---

# Cloud Service Mesh

## Announcement
原文: **1.30.4-asm.1 is now available for in-cluster Cloud Service Mesh.**
You can now download 1.30.4-asm.1 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.30.4 subject to the list of supported features.
[Istio 1.30.4](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/)
[supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)
The following are not supported:
- Failover Priority support for DNS clusters
- `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`
- Multiple `CUSTOM` external authorization providers per workload
- The `DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES` flag
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.30.4-asm.1 uses Envoy v1.38.4-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: Cloud Service Meshの新しいバージョンである1.30.4-asm.1が、クラスター内デプロイメント（in-cluster）向けにリリースされました。このバージョンには、オープンソースのサービスメッシュであるIstio 1.30.4の機能が含まれていますが、Cloud Service Meshの「サポートされる機能リスト」に従い、一部のIstio機能はサポートされません。特に、DNSクラスターのフェイルオーバー優先度、TLS用のワイルドカードホストサービスエントリ、複数のカスタム外部認証プロバイダ、および特定のデバッグフラグはサポート対象外です。また、このバージョンではEnvoy v1.38.4-devが使用されます。

影響有無:
*   **影響あり（アップグレードの選択肢と機能変更）**: Cloud Service Meshを運用中の場合、新しいバージョンへのアップグレードを検討する選択肢が生まれました。Istio 1.30.4の新機能や改善を利用できる可能性があります。
*   **機能の非互換性**: 上記リストに記載されているIstioの機能（例えば、`ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`など）を現在利用している、または利用を計画している場合は、このバージョンへのアップグレードによってそれらの機能が利用できなくなるか、期待通りに動作しない可能性があります。アップグレード前に、既存の構成や利用機能がサポート対象外リストに該当しないか、詳細に確認が必要です。
*   **Envoyバージョンの変更**: 基盤となるEnvoyプロキシのバージョンが変更されています。これにより、パフォーマンス特性やデバッグ機能などに微細な影響がある可能性があります。

対処方法:
*   Cloud Service Meshを運用中の場合、この新しいバージョンへのアップグレードを検討してください。アップグレード計画を立てる際は、以下の点に特に注意してください。
    *   [Istio 1.30.4](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/)のリリースノートを確認し、追加された機能や修正内容が自社のワークロードにメリットをもたらすか確認してください。
    *   [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)のリスト、特に「サポートされない機能」のリストと、現在のCloud Service Meshの構成を照らし合わせ、非互換性がないかを確認してください。
    *   アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)のドキュメントを参照し、計画的なアップグレードを実施してください。可能であれば、本番環境適用前にテスト環境で十分な検証を行ってください。

用語説明:
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供するフルマネージドなサービスメッシュプラットフォームです。オープンソースのIstioをベースにしており、マイクロサービス間のトラフィック管理、セキュリティ、可観測性を提供します。
*   **in-cluster**: サービスメッシュのコントロールプレーンが、ユーザーのKubernetesクラスター内にデプロイされる形態を指します。
*   **Istio**: マイクロサービス接続のネットワークレイヤーを制御するためのオープンソースのサービスメッシュです。トラフィックルーティング、ポリシー適用、可観測性などの機能を提供します。
*   **Envoy**: クラウドネイティブなマイクロサービスアーキテクチャのために設計された、高性能なオープンソースのプロキシです。Istioなどのサービスメッシュのデータプレーンとして広く利用されています。

## Announcement
原文: In-cluster Cloud Service Mesh 1.27 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明: クラスター内デプロイメントのCloud Service Meshバージョン1.27は、サポートが終了しました。これは、このバージョンに対するセキュリティアップデートやバグフィックス、技術サポートが提供されなくなることを意味します。他のバージョンのサポート終了日については、[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)のドキュメントで確認できます。

影響有無:
*   **重大な影響あり**: 現在Cloud Service Mesh 1.27を使用している場合、このバージョンはサポート対象外となるため、セキュリティ上の脆弱性が発見されても修正パッチが提供されず、不具合発生時もサポートが受けられなくなります。これにより、運用上のリスクが大幅に増加します。
*   **影響なし**: Cloud Service Mesh 1.27以外のバージョンを使用している場合、このアナウンスによる直接的な影響はありません。ただし、利用中のバージョンのサポート状況も確認し、計画的なアップグレードを検討する良い機会です。

対処方法:
*   Cloud Service Mesh 1.27を現在ご利用中の場合は、**直ちに最新のサポート対象バージョンへのアップグレードを計画し、実行してください。**
    *   アップグレード先のバージョンについては、最新の安定版および長期サポート版を考慮してください。
    *   アップグレードパスや互換性に関する情報は、Google Cloudの公式ドキュメント（[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)など）を十分に確認してください。
    *   アップグレード前に、テスト環境で十分な検証を行い、既存のワークロードへの影響がないことを確認してください。
*   Cloud Service Meshの他のバージョンをご利用の場合でも、定期的に[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)のページを確認し、EOL（End-of-Life）スケジュールを把握し、計画的なアップグレードパスを立てることを推奨します。

用語説明:
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供するフルマネージドなサービスメッシュプラットフォームです。オープンソースのIstioをベースにしています。
*   **in-cluster**: サービスメッシュのコントロールプレーンが、ユーザーのKubernetesクラスター内にデプロイされる形態を指します。
*   **サポート終了 (End-of-Life / EOL)**: ソフトウェアや製品のライフサイクルにおいて、ベンダーからの技術サポート、セキュリティパッチ、バグフィックスの提供が終了する時点を指します。EOLを迎えたソフトウェアは、セキュリティリスクが高まり、安定した運用が困難になるため、速やかにサポート対象バージョンへ移行する必要があります。
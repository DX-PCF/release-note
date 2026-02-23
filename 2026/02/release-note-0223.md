
# Title: February 19, 2026 
Link: https://docs.cloud.google.com/release-notes#February_19_2026<br>
## Google Kubernetes Engine
### Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:

GKE version | Container-Optimized OS version | Details
---|---|---
1.30.14-gke.2071000 | cos-113-18244-582-2 | [cos-113-18244-582-2 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-582-2_)
1.31.14-gke.1423000 | cos-117-18613-439-120 | [cos-117-18613-439-120 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-439-120_)

説明: 今回のリリースには、Container-Optimized OS (COS) イメージを更新した新しいGKEバージョンが含まれています。これらの更新されたイメージは累積的なものであり、前回のGKEリリース以降に公開されたすべてのCOSバージョンからのセキュリティ修正が組み込まれています。具体的な脆弱性の解消内容については、各COSイメージのセキュリティリリースノートを参照できます。

影響有無: 影響あり（ポジティブ）。
理由: GKEノードの基盤となるオペレーティングシステムであるContainer-Optimized OSのセキュリティパッチが適用されるため、セキュリティ体制が向上します。Google Cloud Composer 2は内部でGKEを利用しており、自動アップグレードによってノードイメージの脆弱性が解消され、よりセキュアな環境でAirflowワークロードを実行できるようになります。

対処方法: 通常、GKEのノードイメージは自動アップグレードの対象となるため、ユーザー側で直接的な対処は不要です。GKEクラスターにメンテナンスウィンドウやメンテナンス除外期間を設定している場合は、それらの設定に従って自動アップグレードが実行されます。

用語説明:
*   **Container-Optimized OS (COS)**: Google Cloudが提供する、GKEノードに推奨される、コンテナ実行に特化した軽量かつセキュアなLinuxベースのオペレーティングシステムです。セキュリティ、安定性、使いやすさに重点が置かれています。
*   **累積的セキュリティ修正 (Cumulative Security Fixes)**: 過去のすべての修正を含む形で提供されるセキュリティパッチ。これにより、最新バージョンにアップグレードするだけで、それまでの全てのセキュリティ脆弱性に対処できます。

### Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

説明: GKEクラスターのバージョンが更新され、新しいバージョンが利用可能になりました。これらの新バージョンは、新規GKEクラスターの作成、および既存クラスターのコントロールプレーンやノードの手動アップグレードに利用できます。バージョン管理とアップグレードの詳細については、GKEの公式ドキュメントを参照してください。

影響有無: 影響あり。
理由: Google Cloud Composer 2は内部でGKEクラスターを利用しており、GKEのバージョン更新はComposerの基盤にも影響を与えます。Composerはマネージドサービスであるため、GKEクラスターのバージョンはGoogleによって管理され、Composerのメンテナンスやアップグレードポリシーに従って内部的に更新される可能性があります。これにより、新しいGKE機能や改善点がComposer環境に反映されることになります。

対処方法:
*   Google Cloud Composer 2を利用している場合、Composerのバージョンアップグレード時に内部GKEバージョンも更新されることが一般的です。Composerの公式ドキュメントやリリースノートで、Composerの特定のバージョンがどのGKEバージョンに対応しているかを確認し、Composerのアップグレード計画を立てる際に考慮してください。
*   直接GKEクラスターを運用している場合は、自身のGKEクラスターが利用しているチャネルとバージョンを確認し、必要に応じてアップグレード計画を立ててください。自動アップグレードを有効にしている場合は、自動的に新しいバージョンへ更新されますが、メンテナンスウィンドウや非推奨APIの使用状況に注意してください。

用語説明:
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスターを管理する中枢部分です。APIサーバー、スケジューラー、コントローラーマネージャーなどから構成され、クラスターの状態を管理し、ノードとPodの動作を調整します。
*   **ノード (Node)**: Kubernetesクラスターのワーカーマシンであり、Pod（コンテナ化されたアプリケーション）を実行するためのリソース（CPU、メモリ、ストレージ）を提供します。

### Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.34.3-gke.1245000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.30.14-gke.1991000
    - 1.30.14-gke.2071000
    - 1.31.14-gke.1336000
    - 1.31.14-gke.1423000
    - 1.32.11-gke.1211000
    - 1.33.5-gke.2392000
    - 1.34.3-gke.1318000
    - 1.35.0-gke.2232003
    - 1.35.0-gke.2398002
- The following versions are no longer available in the Extended channel:
    - 1.30.14-gke.1922000
    - 1.30.14-gke.2026000
    - 1.31.14-gke.1243000
    - 1.31.14-gke.1376000
    - 1.32.11-gke.1038000
    - 1.33.5-gke.2228001
    - 1.34.3-gke.1051003
    - 1.35.0-gke.2232000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.29 to [1.30.14-gke.1973000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.30 to [1.30.14-gke.1973000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
        - 1.31 to [1.31.14-gke.1319000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
        - 1.32 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
        - 1.33 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
        - 1.34 to [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
        - 1.35 to [1.35.0-gke.2232003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)

説明: GKEのExtendedチャネルにおいて、新しいGKEバージョンが利用可能になり、一部のバージョンは利用不可になりました。特に、`1.34.3-gke.1245000` が新規クラスター作成時のデフォルトバージョンとなりました。また、このチャネルのクラスターに対する自動アップグレードのターゲットバージョンも更新されました。リリースノートが公開されても、すべてのGoogle Cloudゾーンでこれらのバージョンがすぐに利用可能になるわけではなく、ロールアウトには数日かかる場合があります。

影響有無: 影響あり。
理由: Google Cloud Composer 2の基盤となるGKEクラスターがExtendedチャネルを使用している場合、Composerの自動アップグレードや手動アップグレードの際にこれらの新しいGKEバージョンが適用される可能性があります。既存のクラスターが現在利用しているバージョンが利用不可リストに含まれている場合、今後自動アップグレードの対象となります。新しいデフォルトバージョンは、新規でGKEクラスターを作成する際の挙動に影響します。

対処方法:
*   現在運用しているGKEクラスター（またはComposer 2の基盤となるGKEクラスター）がExtendedチャネルを使用しているか確認してください。
*   もし該当チャネルを利用している場合、利用不可となったバージョンを使用しているクラスターは自動アップグレードの対象となるため、事前にアプリケーションの互換性を確認し、必要であれば[メンテナンスウィンドウ](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)や[メンテナンス除外期間](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)を設定してください。
*   新規クラスターを作成する場合、デフォルトバージョンが変更されていることを認識しておいてください。

用語説明:
*   **Extended Channel**: GKEのリリースチャネルの一つで、Regularチャネルよりも長期的なサポートを提供し、安定性を重視します。ただし、最新機能の導入は他のチャネルに比べて遅れる傾向があります。
*   **自動アップグレードターゲット (Auto-upgrade targets)**: GKEが自動アップグレードの際に目指す目標バージョンです。マイナーバージョンアップグレードとパッチバージョンアップグレードのターゲットが設定されます。
*   **非推奨API (Deprecated APIs)**: KubernetesのAPIで、将来のバージョンで削除されることが決定しているものです。非推奨APIを使用しているアプリケーションは、GKEアップグレード前に対応が必要です。

### Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.34.3-gke.1245000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.32.12-gke.1026000
    - 1.33.8-gke.1026000
    - 1.34.4-gke.1047000
    - 1.35.0-gke.2232003
    - 1.35.0-gke.2398002
    - 1.35.0-gke
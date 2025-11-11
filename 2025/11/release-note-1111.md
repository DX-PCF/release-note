
# Title: November 07, 2025 
Link: https://docs.cloud.google.com/release-notes#November_07_2025<br>
以下にGoogle Kubernetes Engine (GKE) のリリースノートに対する調査結果を報告します。

---

# Google Kubernetes Engine

## Changed
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明: GKEクラスタの新しいバージョンがリリースされ、新規クラスタの作成、および既存クラスタのコントロールプレーンとノードの手動アップグレードで利用可能になりました。具体的なバージョン情報は、GKEのバージョン管理とアップグレードに関するドキュメントで確認できます。

影響有無: 影響なし。これは新しいバージョンの利用開始を知らせる一般的なアナウンスであり、既存の稼働中のサービスに直接的な影響を与えるものではありません。

対処方法: なし。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.28.15-gke.2966000 | cos-113-18244-521-7 | cos-113-18244-521-7 release notes |
| 1.29.15-gke.2236000 | cos-113-18244-448-79 | cos-113-18244-448-79 release notes |
| 1.30.14-gke.1525000 | cos-113-18244-521-7 | cos-113-18244-521-7 release notes |
| 1.31.13-gke.1231000 | cos-117-18613-439-9 | cos-117-18613-439-9 release notes |
| 1.32.9-gke.1330000 | cos-117-18613-439-9 | cos-117-18613-439-9 release notes |
| 1.33.5-gke.1521000 | cos-121-18867-294-2 | cos-121-18867-294-2 release notes |
| 1.34.1-gke.2037001 | cos-125-19216-0-94 | cos-125-19216-0-94 release notes |
| 1.34.1-gke.2541000 | cos-125-19216-0-115 | cos-125-19216-0-115 release notes |
[cos-113-18244-521-7 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-521-7_)
[cos-113-18244-448-79 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-448-79_)
[cos-113-18244-521-7 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-521-7_)
[cos-117-18613-439-9 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-439-9_)
[cos-117-18613-439-9 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-439-9_)
[cos-121-18867-294-2 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-294-2_)
[cos-125-19216-0-94 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-0-94_)
[cos-125-19216-0-115 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-0-115_)

説明: 今回のGKEリリースに含まれる新しいGKEバージョンでは、更新されたContainer-Optimized OS (COS) イメージが使用されています。これらのイメージには、前回のGKEリリース以降に公開された全てのCOSバージョンからの累積的なセキュリティ修正が含まれています。詳細なセキュリティ脆弱性の修正内容については、各COSバージョンにリンクされたリリースノートを参照してください。

影響有無: 影響あり（ポジティブ）。ノードOSのセキュリティ脆弱性修正が含まれるため、クラスタのセキュリティ体制が向上します。既存のワークロードへの直接的な非互換性変更は通常ありませんが、OSレベルの変更による予期せぬ動作がないか、アップグレード前のテストが推奨されます。Google Cloud Composer 2.7.1はGKE上に構築されており、GKEのノードOSがアップデートされることで、間接的に基盤のセキュリティが強化されます。

対処方法: 最新のセキュリティ修正を適用するため、GKEクラスタをこれらの新しいバージョンへアップグレードすることを推奨します。GKEの自動アップグレードが有効になっている場合、メンテナンス期間中に自動的に適用されます。手動アップグレードやComposer環境の場合は、GCPが管理する自動アップグレードに依存するか、Composerのリリースノートで基盤バージョンの更新がアナウンスされた際に確認します。

用語説明:
*   **Container-Optimized OS (COS):** Google Cloudによって提供される、コンテナワークロードの実行に特化したオペレーティングシステム。高いセキュリティと効率性を特徴とします。
*   **累積的なセキュリティ修正:** 過去の全てのセキュリティ修正が最新バージョンに統合されていることを意味します。これにより、最新バージョンにアップグレードするだけで、以前の脆弱性もまとめて対処されます。

## Changed (Extended Channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.1201000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.28.15-gke.2793000, 1.28.15-gke.2966000, 1.29.15-gke.2085000, 1.29.15-gke.2236000, 1.30.14-gke.1408000, 1.30.14-gke.1525000, 1.31.13-gke.1123000, 1.32.9-gke.1207000, 1.33.5-gke.1308000
- The following versions are no longer available in the Extended channel:
    - 1.28.15-gke.2751000, 1.28.15-gke.2857000, 1.29.15-gke.1989000, 1.29.15-gke.2109000, 1.30.14-gke.1336000, 1.30.14-gke.1426000, 1.31.13-gke.1023000, 1.32.9-gke.1108000, 1.33.5-gke.1162000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.27 to 1.28.15-gke.2767000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.28 to 1.28.15-gke.2767000, 1.29 to 1.29.15-gke.2002000, 1.30 to 1.30.14-gke.1349000, 1.31 to 1.31.13-gke.1040000, 1.32 to 1.32.9-gke.1130000, 1.33 to 1.33.5-gke.1201000
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)

説明: ExtendedチャネルにおけるGKEクラスタのデフォルトバージョンが1.33.5-gke.1201000に変更されました。また、このチャネルで利用可能になったバージョンと、利用できなくなったバージョンが更新されています。この更新により、既存のクラスタの自動アップグレードターゲットも変更されており、メンテナンス除外期間や非推奨APIの使用などの制約がない場合、コントロールプレーンとノードが新しいマイナーバージョンやパッチバージョンに自動アップグレードされる可能性があります。

影響有無: 影響あり。
*   **既存クラスタ (Extendedチャネル利用時):** 自動アップグレードターゲットが変更されたため、GKEによる自動アップグレードが新しいバージョンに対して行われる可能性があります。特にマイナーバージョンアップグレードでは、Kubernetesの非推奨APIや動作変更により、ワークロードの互換性に影響が出る可能性があります。
*   **新規クラスタ (Extendedチャネル利用時):** クラスタ作成時のデフォルトバージョンが変更されるため、意図せず新しいバージョンでクラスタがプロビジョニングされる可能性があります。

対処方法:
1.  **チャネルとバージョンの確認:** 運用中のGKEクラスタがExtendedチャネルを使用しているか、また現在のバージョンが何かを確認します。
2.  **自動アップグレード設定の確認:** メンテナンスウィンドウやメンテナンス除外設定が適切に構成されているか確認し、意図しないタイミングでのアップグレードが発生しないようにします。
3.  **非推奨APIの確認:** アップグレードターゲットとなるバージョンで非推奨となったAPIや機能変更がないか、KubernetesのCHANGELOGを事前に確認し、アプリケーションの互換性を評価します。必要に応じてアプリケーションを修正・テストします。
4.  **新規クラスタ作成時:** 明示的にバージョンを指定しない場合、新しいデフォルトバージョンでクラスタが作成されることを認識し、必要に応じてバージョンを指定してプロビジョニングします。

用語説明:
*   **リリースチャネル (Release Channels):** GKEクラスタのバージョンとアップグレード動作を管理する仕組み。Stable, Regular, Rapid, Extendedの4つのチャネルがあり、それぞれ更新頻度と安定性の特性が異なります。
*   **自動アップグレードターゲット:** GKEがクラスタのコントロールプレーンとノードを自動的にアップグレードする際の目標となるバージョン。

## Changed (Rapid Channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.1-gke.2037001 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
    - 1.31.13-gke.1231000, 1.32.9-gke.1330000, 1.33.5-gke.1521000, 1.34.1-gke.2037001, 1.34.1-gke.2541000
- The following versions are no longer available in the Rapid channel:
    - 1.31.13-gke.1123000, 1.32.9-gke.1207000, 1.33.5-gke.1308000, 1.34.1-gke.2037000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.30 to 1.31.13-gke.1139000, 1.31 to 1.32.9-gke.1239000, 1.32 to 1.33.5-gke.1350000, 1.33 to 1.34.1-gke.2037001
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.31 to 1.31.13-gke.1139000, 1.32 to 1.32.9-gke.1239000, 1.33 to 1.33.5-gke.1350000, 1.34 to 1.34.1-gke.2037001
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)

説明: RapidチャネルにおけるGKEクラスタのデフォルトバージョンが1.34.1-gke.2037001に変更されました。このチャネルで利用可能になったバージョンと利用できなくなったバージョンが更新されています。また、既存クラスタの自動アップグレードターゲットも変更され、メンテナンス除外期間や非推奨APIの使用などの制約がない場合、コントロールプレーンとノードが新しいマイナーバージョンやパッチバージョンに自動アップグレードされる可能性があります。

影響有無: 影響あり。
*   **既存クラスタ (Rapidチャネル利用時):** 自動アップグレードターゲットが変更されたため、GKEによる自動アップグレードが新しいバージョンに対して行われる可能性があります。Rapidチャネルは更新頻度が高く、最新のKubernetes機能や修正が含まれる反面、早期に非互換性変更に遭遇するリスクがあります。特にマイナーバージョンアップグレードでは、非推奨APIや動作変更によりワークロードの互換性に影響が出る可能性があります。
*   **新規クラスタ (Rapidチャネル利用時):** クラスタ作成時のデフォルトバージョンが変更されるため、意図せず新しいバージョンでクラスタがプロビジョニングされる可能性があります。

対処方法:
1.  **チャネルとバージョンの確認:** 運用中のGKEクラスタがRapidチャネルを使用しているか、また現在のバージョンが何かを確認します。
2.  **自動アップグレード設定の確認:** メンテナンスウィンドウやメンテナンス除外設定が適切に構成されているか確認し、意図しないタイミングでのアップグレードが発生しないようにします。
3.  **非推奨APIの確認:** Rapidチャネルは機能の変更が早いため、アップグレードターゲットとなるバージョンで非推奨となったAPIや機能変更がないか、KubernetesのCHANGELOGを事前に念入りに確認し、アプリケーションの互換性を評価します。本番環境への適用前に十分なテストを実施することを強く推奨します。
4.  **新規クラスタ作成時:** 明示的にバージョンを指定しない場合、新しいデフォルトバージョンでクラスタが作成されることを認識し、必要に応じてバージョンを指定してプロビジョニングします。

用語説明:
*   **Rapidチャネル:** GKEのリリースチャネルの一つで、最新のKubernetesバージョンとGKE機能が最も早く提供されます。ただし、他のチャネルに比べて安定性は相対的に低く、変更頻度が高いです。

## Changed (Regular Channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.1201000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
    - 1.31.13-gke.1123000, 1.32.9-gke.1207000, 1.33.5-gke.1308000
- The following versions are no longer available in the Regular channel:
    - 1.31.13-gke.102300
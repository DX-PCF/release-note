
# Title: June 04, 2026 
Link: https://docs.cloud.google.com/release-notes#June_04_2026<br>
Google Cloudのインフラエンジニアとして、ご提示いただいたGoogle Kubernetes Engine (GKE) のリリースノートについて、構築済みのサービス（特にGoogle Cloud Composer 2, Composer version 2.7.1, Airflow version 2.7.3）への影響有無を調査し、以下の通りご報告いたします。

---

# Google Kubernetes Engine

## Change
原文: GKE cluster versions have been updated.

 **New versions available for upgrades and new clusters.**

 The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

[GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明: GKEクラスターのバージョンが更新され、新規クラスター作成や既存クラスターのコントロールプレーンおよびノードの手動アップグレード向けに、新しいバージョンが利用可能になりました。詳細については、GKEのバージョニングとサポート、およびクラスターアップグレードに関するドキュメントを参照してください。

影響有無: 影響なし。
これはGKEのバージョンラインナップが更新されたことに関する一般的なアナウンスです。具体的なチャネルごとのバージョン情報や非推奨化情報はこの後に続くセクションで詳述されるため、このアナウンス自体が直接既存のサービスに影響を与えることはありません。

対処方法: なし。

## Security
原文: This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

 To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

 GKE version
Container-Optimized OS version
Details


1.34.8-gke.1218000
cos-125-19216-395-7
cos-125-19216-395-7 release notes


1.36.0-gke.2684000
cos-129-19506-120-64
cos-129-19506-120-64 release notes

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.34.8-gke.1218000 | cos-125-19216-395-7 | [cos-125-19216-395-7 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-395-7_) |
| 1.36.0-gke.2684000 | cos-129-19506-120-64 | [cos-129-19506-120-64 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#cos-129-19506-120-64_) |

説明: このリリースには、セキュリティ修正が適用された最新のContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのCOSイメージは、前回のGKEリリース以降に公開されたすべてのセキュリティ修正を累積的に含んでいます。具体的な脆弱性の詳細は、各COSイメージのリリースノートで確認できます。例として、GKEバージョン1.34.8-gke.1218000にはcos-125-19216-395-7が、1.36.0-gke.2684000にはcos-129-19506-120-64が使用されています。

影響有無: 影響なし（むしろ好影響）。
ノードイメージのセキュリティ修正は、既存のGKEクラスターのセキュリティ体制を強化するため、サービス運用にポジティブな影響を与えます。Google Cloud Composer環境はGKEノード上で動作するため、基盤となるインフラのセキュリティ向上の恩恵を受けます。

対処方法: 推奨。
GKEクラスターの自動アップグレードが有効になっていることを確認してください。これにより、これらのセキュリティ修正が適用された最新のノードイメージが自動的に適用されます。自動アップグレードが無効な場合は、計画的な手動アップグレードを検討し、セキュリティパッチを適用することを強く推奨します。

用語説明:
*   **Container-Optimized OS (COS)**: Google CloudでKubernetesワークロードを実行するために最適化された、セキュリティと効率性を重視したLinuxベースのオペレーティングシステムです。GKEのノードプールで使用されます。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.34.7-gke.1055000 is now the default version for cluster creation in the Stable channel.
- The following versions are no longer available in the Stable channel:
- 1.33.11-gke.1013000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.6-gke.1307000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.11-gke.1074000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.11-gke.1074000
- 1.34 to 1.34.7-gke.1055000

[1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
[1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
[1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)

説明: Stableチャネルにおいて、新規クラスター作成時のデフォルトバージョンが1.34.7-gke.1055000になりました。また、1.33.11-gke.1013000はStableチャネルで非推奨となり、90日以内またはサポート終了時に削除されます。1.34.6-gke.1307000も利用できなくなりました。このチャネルで稼働しているクラスターの自動アップグレードターゲットが更新され、例えば1.32から1.33.11-gke.1074000へのマイナーバージョンアップグレードや、1.33から1.33.11-gke.1074000、1.34から1.34.7-gke.1055000へのパッチバージョンアップグレードが行われる
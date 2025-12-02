
# Title: November 28, 2025 
Link: https://docs.cloud.google.com/release-notes#November_28_2025<br>
Google Cloudのインフラエンジニアとして、GKEのリリースノートから既存サービス（特にGoogle Cloud Composer）への影響を調査し、以下の通り回答します。

---

# Google Kubernetes Engine

## Security
原文:
 This release includes new GKE versions that use updated
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
1.28.15-gke.3188000
cos-113-18244-521-23
cos-113-18244-521-23 release notes
1.29.15-gke.2505000
cos-113-18244-521-23
cos-113-18244-521-23 release notes
1.30.14-gke.1746000
cos-113-18244-521-23
cos-113-18244-521-23 release notes
1.31.14-gke.1033000
cos-117-18613-439-28
cos-117-18613-439-28 release notes
1.34.1-gke.1829001
cos-125-19216-0-94
cos-125-19216-0-94 release notes
1.34.1-gke.2541000
cos-125-19216-0-115
cos-125-19216-0-115 release notes
1.34.1-gke.3355000
cos-125-19216-104-32
cos-125-19216-104-32 release notes

説明：
このリリースには、Container-Optimized OS（COS）イメージの更新版を使用する新しいGKEバージョンが含まれています。これらの更新されたイメージは、前回のGKEリリース以降に公開されたすべてのCOSバージョンからのセキュリティ修正を累積的に取り込んでいます。各COSイメージで解決された特定の脆弱性の詳細については、対応するCOSリリースノートのリンクを参照してください。

影響有無：影響あり
既存のGKEクラスターのノードイメージにセキュリティ修正が適用されるため、クラスター全体のセキュリティ体制が向上します。特に脆弱性の修正が含まれているため、セキュリティリスクの軽減に繋がります。

対処方法：
GKEクラスターを、このリリースノートで言及されている新しいGKEバージョンにアップグレードすることを推奨します。自動アップグレードが有効になっている場合は、メンテナンスウィンドウ中に自動で適用されます。手動でアップグレードする場合は、計画的に実施してください。Google Cloud Composer2環境の基盤GKEも同様にアップグレード対象となるため、Composerのアップグレードスケジュールと合わせて検討してください。

用語説明：
*   **Container-Optimized OS (COS):** Google Cloudが提供する、コンテナの実行に特化したCompute Engineのオペレーティングシステム。GKEノードのOSとして使用されます。
*   **セキュリティ修正:** ソフトウェアの脆弱性（セキュリティホール）を修正するためのパッチ。システムのセキュリティを強化するために重要です。

---

## Changed
原文:
 GKE cluster versions have been updated.

 **New versions available for upgrades and new clusters.**

 The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

説明：
GKEクラスターのバージョンが更新されました。新しいGKEバージョンは、新規クラスターの作成、および既存クラスターのコントロールプレーンおよびノードの手動アップグレードに利用可能です。GKEのバージョン管理とアップグレードに関する詳細情報は、提供されているドキュメントリンクから参照できます。

影響有無：影響なし
新しいGKEバージョンが利用可能になったという情報であり、現在のGKEクラスターの運用に直接的な影響はありません。ただし、今後のアップグレード計画の検討に役立つ情報です。

対処方法：
特段の対処は不要です。既存クラスターのアップグレード計画や新規クラスターのデプロイ時に、これらの新しいバージョンを検討してください。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Extended channel:
- 1.28.15-gke.3188000
- 1.29.15-gke.2505000
- 1.30.14-gke.1746000

説明：
Extendedリリースチャネルにおいて、特定のGKEバージョン（1.28.15-gke.3188000、1.29.15-gke.2505000、1.30.14-gke.1746000）が利用可能になりました。これらのバージョンは、リリースノート公開時点で展開中であり、全Google Cloudゾーンで利用可能になるまでに数日かかる場合があります。

影響有無：影響なし
Extendedチャネルを利用しているクラスターに対して、アップグレードオプションが追加されたことを意味します。現在の運用に直接的な影響はありません。

対処方法：
Extendedチャネルを利用しているGKEクラスターがある場合、これらのバージョンへのアップグレードを検討できます。ただし、Google Cloud Composer2は通常Extendedチャネルを使用しないため、直接的な影響は限定的です。

用語説明：
*   **リリースチャネル (Release Channel):** GKEクラスターの自動アップグレードのタイミングとバージョン提供の安定性を定義する仕組み。`Extended`チャネルは、長期的なサポートと安定性を重視し、新機能の導入よりも既存機能の安定稼働を優先する本番環境に適しています。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available:
- 1.31.14-gke.1033000
- 1.32.9-gke.1575000
- 1.33.5-gke.1862000
- 1.34.1-gke.1829001
- 1.34.1-gke.2037001
- 1.34.1-gke.2037002
- 1.34.1-gke.2541000
- 1.34.1-gke.2909000
- 1.34.1-gke.2980000
- 1.34.1-gke.3084001
- 1.34.1-gke.3225000
- 1.34.1-gke.3355000

- The following node versions are now available:
- 1.28.15-gke.3188000
- 1.29.15-gke.2505000
- 1.30.14-gke.1746000
- 1.31.14-gke.1033000
- 1.32.9-gke.1575000
- 1.33.5-gke.1862000
- 1.34.1-gke.1829001
- 1.34.1-gke.2037001
- 1.34.1-gke.2037002
- 1.34.1-gke.2541000
- 1.34.1-gke.2909000
- 1.34.1-gke.2980000
- 1.34.1-gke.3084001
- 1.34.1-gke.3225000
- 1.34.1-gke.3355000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.34 to 1.34.1-gke.2909000

説明：
GKEの様々なバージョン（コントロールプレーンおよびノード用）が一般的に利用可能になりました。これらのバージョンはリリースノート公開時点で展開中であり、全Google Cloudゾーンで利用可能になるまでに数日かかる場合があります。また、対象のマイナーバージョンを実行しているクラスターの一般的な自動アップグレードターゲットが更新されました。マイナーバージョンアップグレードが利用できない場合や、メンテナンス除外期間などの要因がある場合、GKEはクラスターを特定の新しいパッチバージョン（例: 1.34から1.34.1-gke.2909000）にアップグレードする可能性があります。

影響有無：影響あり
自動アップグレードを有効にしているGKEクラスターは、これらの新しいバージョンに自動的にアップグレードされる可能性があります。これにより、一時的なダウンタイム（ローリングアップデートによる許容範囲内）が発生したり、アプリケーションの互換性確認が必要になる場合があります。Google Cloud Composer2の基盤GKEも同様に、自動アップグレードの対象となる可能性があります。

対処方法：
*   既存のGKEクラスターで自動アップグレードが有効になっている場合、メンテナンスウィンドウの設定を確認し、アップグレードのタイミングを把握してください。
*   クラスターのバージョンが自動アップグレードのターゲットとなるGKEバージョン（例：1.34系）である場合、アプリケーションが新しいGKEバージョンで問題なく動作するか、事前にテスト環境で検証することを推奨します。
*   Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)をご利用の場合、Composer環境の基盤GKEも自動アップグレードの対象となる可能性があります。Composerのアップグレードプロセスや互換性に関するドキュメントを確認し、必要に応じてメンテナンス期間を設けるなどの対策を検討してください。

用語説明：
*   **オートアップグレードターゲット (Auto-upgrade targets):** GKEが自動アップグレードを行う際に目標とするGKEのバージョン。
*   **メンテナンス除外期間 (Maintenance Exclusions):** GKEクラスターの自動メンテナンス（例：自動アップグレード）が実行されないように設定できる期間。特定の期間にクラスターの変更を避けたい場合に利用します。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Rapid channel:
- 1.31.14-gke.1033000
- 1.32.9-gke.1575000
- 1.33.5-gke.1862000
- 1.34.1-gke.3225000
- 1.34.1-gke.3355000

説明：
Rapidリリースチャネルにおいて、特定のGKEバージョン（1.31.14-gke.1033000、1.32.9-gke.1575000、1.33.5-gke.1862000、1.34.1-gke.3225000、1.34.1-gke.3355000）が利用可能になりました。これらのバージョンはリリースノート公開時点で展開中であり、全Google Cloudゾーンで利用可能になるまでに数日かかる場合があります。

影響有無：影響なし
Rapidチャネルを利用しているクラスターに対して、アップグレードオプションが追加されたことを意味します。現在の運用に直接的な影響はありません。

対処方法：
Rapidチャネルを利用しているGKEクラスターがある場合、これらのバージョンへのアップグレードを検討できます。

用語説明：
*   **Rapidチャネル (Rapid Channel):** GKEのリリースチャネルの一つで、最も早く新しいGKEバージョンが提供されます。最新機能や改善を早期に利用したい場合に適していますが、他のチャネルよりも安定性が低い可能性があります。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Regular channel:
- 1.31.13-gke.1377000
- 1.32.9-gke.1462000
- 1.33.5-gke.1697000
- 1.34.1-gke.2909000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.34 to 1.34.1-gke.2909000

説明：
Regularリリースチャネルにおいて、特定のGKEバージョン（1.31.13-gke.1377000、1.32.9-gke.1462000、1.33.5-gke.1697000、1.34.1-gke.2909000）が利用可能になりました。これらのバージョンはリリースノート公開時点で展開中であり、全Google Cloudゾーンで利用可能になるまでに数日かかる場合があります。また、対象のマイナーバージョンを実行しているクラスターの一般的な自動アップグレードターゲットが更新されました。マイナーバージョンアップグレードが利用できない場合や、メンテナンス除外期間などの要因がある場合、GKEはクラスターを特定の新しいパッチバージョン（例: 1.34から1.34.1-gke.2909000）にアップグレードする可能性があります。

影響有無：影響あり
Regularチャネルを利用し、自動アップグレードを有効にしているGKEクラスターは、これらの新しいバージョンに自動的にアップグレードされる可能性があります。これにより、一時的なダウンタイム（ローリングアップデートによる許容範囲内）が発生したり、アプリケーションの互換性確認が必要になる場合があります。Google Cloud Composer2は、このRegularチャネルに設定されている場合、基盤GKEも自動アップグレードの対象となる可能性があります。

対処方法：
*   既存のGKEクラスターで自動アップグレードが有効になっている場合、メンテナンスウィンドウの設定を確認し、アップグレードのタイミングを把握してください。
*   クラスターのバージョンが自動アップグレードのターゲットとなるGKEバージョン（例：1.34系）である場合、アプリケーションが新しいGKEバージョンで問題なく動作するか、事前にテスト環境で検証することを推奨します。
*   Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)をご利用の場合、Composer環境の基盤GKEも自動アップグレードの対象となる可能性があります。Composerのアップグレードプロセスや互換性に関するドキュメントを確認し、必要に応じてメンテナンス期間を設けるなどの対策を検討してください。

用語説明：
*   **Regularチャネル (Regular Channel):** GKEのリリースチャネルの一つで、Rapidチャネルよりも安定性が高く、Stableチャネルよりも早く新機能が提供されます。多くの本番環境で推奨されるチャネルです。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

 There are no new releases in the Stable channel.

説明：
Stableリリースチャネルには、今回の新しいリリースはありません。新しいGKEバージョンは提供されていません。

影響有無：影響なし
Stableチャネルを利用しているGKEクラスターは、今回のリリースノートで言及されている新しいGKEバージョンには影響されません。現在の運用に直接的な変更はありません。

対処方法：
特段の対処は不要です。

用語説明：
*   **Stableチャネル (Stable Channel):** GKEのリリースチャネルの一つで、最も安定したバージョンが提供されます。新機能の導入は最も遅れますが、本番環境での長期運用で高い安定性を求める場合に適しています。
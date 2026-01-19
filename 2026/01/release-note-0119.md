
# Title: January 15, 2026 
Link: https://docs.cloud.google.com/release-notes#January_15_2026<br>
インフラエンジニアとして、Google Cloudのリリースノートに基づき、構築済みのサービスへの影響有無を調査し、以下の通りご報告いたします。

現在稼働中のサービスとして、Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) があることを前提に、影響を評価しています。

---

# AlloyDB for PostgreSQL

## Fixed

原文: Memory usage estimation is more accurate for high-dimensional vector indexes. This fix prevents out of memory (OOM) errors by enforcing defined memory constraints throughout the index build process. You might need to increase your `maintenance_work_mem settings` to align with the real usage estimates.

説明：高次元ベクトルインデックスのメモリ使用量見積もりの精度が向上しました。この修正により、インデックス構築プロセス全体で定義されたメモリ制約が適用され、メモリ不足（OOM）エラーの発生が抑制されます。ただし、実際のメモリ使用量の見積もりに合わせて、`maintenance_work_mem settings` の値を増やす必要がある場合があります。

影響有無：影響あり。AlloyDB for PostgreSQLを使用しており、特に高次元ベクトルインデックスを利用している場合に影響します。OOMエラーの発生頻度が減少する可能性はありますが、メモリ使用量の見積もりが厳密になった結果、既存の `maintenance_work_mem settings` が不足し、インデックス構築に時間がかかったり、失敗したりする可能性があります。

対処方法：
AlloyDB for PostgreSQLで高次元ベクトルインデックスを使用している場合、本修正適用後（または自動更新後）にインデックス構築プロセスの監視を強化し、性能低下やOOMエラーが発生しないか確認してください。
状況に応じて `maintenance_work_mem settings` の値を見直し、必要であれば増量することを検討してください。設定変更前にテスト環境での検証を強く推奨します。

用語説明：
*   **高次元ベクトルインデックス (High-dimensional vector indexes)**: 画像認識、自然言語処理、推薦システムなどで使用される、多数の数値で構成されるベクトルデータ（例：埋め込みベクトル）を効率的に検索・比較するためのインデックスです。
*   **Out Of Memory (OOM) エラー**: プログラムやプロセスが利用可能なメモリを使い果たし、これ以上メモリを割り当てることができない場合に発生するエラーです。
*   **`maintenance_work_mem settings`**: PostgreSQLの構成パラメータの一つで、インデックスの作成、VACUUM、ALTER TABLEなどのメンテナンス操作中に一時的に使用されるメモリの最大量を定義します。

---

# Cloud Service Mesh

## Announcement

原文: The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.6-asm.8 is rolling out to the rapid release channel.
- 1.20.8-asm.60 is rolling out to the regular release channel.
- 1.19.10-asm.55 is rolling out to the stable release channel.
These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:
| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| CVE-2025-61729 | Yes | Yes | - | Yes |
| CVE-2025-61727 | Yes | Yes | - | Yes |
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)
[CVE-2025-61727](https://security-tracker.debian.org/tracker/CVE-2025-61727)

説明：マネージドCloud Service Mesh向けに、以下の新しいイメージ（1.21.6-asm.8、1.20.8-asm.60、1.19.10-asm.55）が各リリースチャンネルで順次展開されています。これらのパッチリリースには、CVE-2025-61729とCVE-2025-61727という2つのセキュリティ脆弱性に対する修正が含まれています。

影響有無：影響なし。これはマネージドCloud Service Meshの内部的なイメージ更新とセキュリティ修正のアナウンスであるため、ユーザーが直接何かを操作する必要はありません。利用中のCloud Service Meshのセキュリティが自動的に向上します。

対処方法：なし。マネージドサービスであるため、Google Cloudが自動的に更新を適用します。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供する、Istioベースのフルマネージドサービスメッシュプラットフォームです。サービス間のトラフィック管理、セキュリティポリシーの適用、可観測性の向上などを実現します。
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に公開されているサイバーセキュリティの脆弱性や露出を識別するための標準的な識別子です。

---

# Google Kubernetes Engine (GKE)

## Security

原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image.

説明：このリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたイメージには、前回のGKEリリース以降にリリースされた全てのCOSバージョンからのセキュリティ修正が累積的に含まれています。

影響有無：直接的な操作は不要ですが、Composer 2の基盤であるGKEノードのOSイメージが更新されることで、セキュリティが向上します。既存のComposer環境のGKEノードは、自動アップグレードポリシーに従って更新されるため、明示的な対処は不要です。ただし、更新時に一時的なノードの再起動が発生する可能性があります。

対処方法：なし。GKEの自動アップグレードに任せる運用となります。アップグレードスケジュールを把握し、設定しているメンテナンス期間内に実施されることを確認してください。

用語説明：
*   **Container-Optimized OS (COS)**: Googleによってコンテナの実行に特化して最適化されたオペレーティングシステムです。GKEのノードイメージとして主に使用されます。

## Change

原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

説明：GKEクラスターバージョンが更新され、新しいバージョンが利用可能になりました。これらの新しいバージョンは、新規GKEクラスターの作成、および既存クラスターのコントロールプレーンとノードの手動アップグレードで利用できます。

影響有無：直接的な影響はありません。これは利用可能なGKEバージョンのリストの更新であり、現在のComposer環境のGKEバージョンにすぐに変更が生じるわけではありません。Composer 2は特定のGKEバージョン範囲をサポートしており、GKEクラスターの自動アップグレードが行われる場合も、Composerの互換性のあるGKEバージョンにアップグレードされます。

対処方法：なし。Composerは基盤となるGKEのバージョン管理を自動で行うため、手動でのGKEアップグレードは通常行いません。Composerの将来のバージョンアップグレード計画に合わせて、GKEのバージョン互換性を継続的に確認してください。

用語説明：
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスターを管理するコンポーネント群（APIサーバー、スケジューラ、コントローラマネージャーなど）の総称です。
*   **ノード (Node)**: コンテナ化されたアプリケーション（Pod）を実行するワーカーマシンです。

## Change (Extended Channel)

原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2072000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.29.15-gke.2617000
    - 1.29.15-gke.2660000
    - 1.30.14-gke.1861000
    - 1.30.14-gke.1901000
    - 1.31.14-gke.1166000
    - 1.32.9-gke.1728000
    - 1.33.5-gke.2100000
    - 1.34.1-gke.3947000
- The following versions are no longer available in the Extended channel:
    - 1.28.15-gke.3251000
    - 1.28.15-gke.3280000
    - 1.28.15-gke.3290000
    - 1.29.15-gke.2585000
    - 1.29.15-gke.2629000
    - 1.30.14-gke.1820000
    - 1.30.14-gke.1870000
    - 1.31.14-gke.1114000
    - 1.32.9-gke.1675000
    - 1.33.5-gke.2019000
    - 1.34.1-gke.3355004
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.28 to 1.29.15-gke.2613000
        - 1.29 to 1.30.14-gke.1855000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.29 to 1.29.15-gke.2613000
        - 1.30 to 1.30.14-gke.1855000
        - 1.31 to 1.31.14-gke.1156000
        - 1.32 to 1.32.9-gke.1711000
        - 1.33 to 1.33.5-gke.2072000
        - 1.34 to 1.34.1-gke.3899001

説明：GKEのExtendedリリースチャンネルにおいて、新規クラスター作成のデフォルトバージョンが1.33.5-gke.2072000になりました。また、このチャンネルで利用可能になったバージョンと利用不可になったバージョンがリストアップされています。このチャンネルのクラスターは、新しい自動アップグレードターゲットが設定され、GKEはコントロールプレーンとノードをリストされた新しいバージョンにアップグレードできるようになります。

影響有無：軽微な影響あり。Composer 2環境は通常、StandardまたはRegularリリースチャンネルを使用するため、Extendedチャンネルの変更が直接影響することは稀です。ただし、もしComposer環境のGKEクラスターがExtendedチャンネルを利用している場合は、自動アップグレードターゲットが変更されるため、GKEバージョンが更新される可能性があります。Composer 2.7.1 (Airflow 2.7.3)はGKE 1.27.xまたは1.28.xをサポートしているため、それより新しいバージョンへの自動アップグレードはComposerの動作保証外となり、潜在的な問題を引き起こす可能性があります。

対処方法：
現在のComposer環境がどのGKEリリースチャンネルを使用しているかを確認してください。
もしExtendedチャンネルを使用している場合、Composerの公式ドキュメント（[Composer Version and Airflow Version support](https://cloud.google.com/composer/docs/composer-2/composer-version-support)）でサポートされているGKEバージョンを確認し、自動アップグレードがサポート外のバージョンにならないよう、メンテナンスウィンドウやメンテナンス除外設定を適切に検討するか、GKEクラスターのチャンネル変更、またはComposerのバージョンアップを計画してください。

用語説明：
*   **リリースチャンネル (Release Channel)**: GKEクラスターのリリースと更新のペースを制御する設定です。Stable, Regular, Rapid, Extendedなどのチャンネルがあり、新しい機能やバグ修正がどのくらいの速さで提供されるかが異なります。Extendedは長期サポートを目的としています。
*   **自動アップグレードターゲット (Auto-upgrade targets)**: GKEがクラスターを自動的にアップグレードする際の目標となるバージョンです。

## Change (Regular Channel)

原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2072000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
    - 1.31.14-gke.1166000
    - 1.32.9-gke.1728000
    - 1.33.5-gke.2100000
    - 1.34.1-gke.3947000
- The following versions are no longer available in the Regular channel:
    - 1.31.14-gke.1114000
    - 1.32.9-gke.1675000
    - 1.33.5-gke.2019000
    - 1.34.1-gke.3355004
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.30 to 1.31.14-gke.1156000
        - 1.31 to 1.32.9-gke.1711000
        - 1.32 to 1.33.5-gke.2072000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.31 to 1.31.14-gke.1156000
        - 1.32 to 1.32.9-gke.1711000
        - 1.33 to 1.33.5-gke.2072000
        - 1.34 to 1.34.1-gke.38990
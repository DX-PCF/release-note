
# Title: March 05, 2026 
Link: https://docs.cloud.google.com/release-notes#March_05_2026<br>
Google Cloud のインフラエンジニアとして、ご依頼のリリースノートについて製品ごとの影響有無、対処方法を調査しました。

---

# BigQuery
## Change
原文: An updated version of the Simba ODBC driver for BigQuery is now available.

説明：
BigQuery に接続するための Simba ODBC ドライバーの新しいバージョンがリリースされました。この更新には、パフォーマンスの改善、バグ修正、または新機能のサポートが含まれる可能性があります。

影響有無：
BigQuery に対して Simba ODBC ドライバーを利用した接続（例えば、BIツールや他のアプリケーションからのデータ連携）を行っている場合に影響があります。既存のドライバーが直ちに動作しなくなる可能性は低いですが、最新の機能を利用したい場合や、既存の課題がこのアップデートで解決される場合は、更新を検討する必要があります。

対処方法：
現在BigQueryにSimba ODBCドライバーを使用して接続しているシステムがある場合、以下の対応を推奨します。
1.  リリースノートまたは公式ドキュメントで、今回のアップデートに含まれる変更点や改善点を確認してください。
2.  テスト環境で新しいドライバーを導入し、既存のデータ連携やクエリが問題なく動作するかを十分に検証してください。
3.  パフォーマンスやセキュリティの改善が見込まれる場合、本番環境への適用を計画してください。

用語説明：
*   **ODBC (Open Database Connectivity)**: データベースにアクセスするための標準的なAPI（Application Programming Interface）。アプリケーションが特定のデータベースシステムに依存することなく、様々なデータベースと対話できるようにするための共通インターフェースを提供します。
*   **Simba ODBC driver for BigQuery**: Simba Technologies社が開発・提供している、BigQueryへのODBC接続を可能にするドライバーソフトウェアです。Microsoft Excel、Tableau、Power BIなどのODBC互換のBIツールやアプリケーションからBigQueryに接続する際に使用されます。

---

# Compute Engine
## Issue
原文: For Red Hat Enterprise Linux (RHEL) operating system, VM Manager provides vulnerability scanning results based on the latest minor version for each major version released. If your VM runs an earlier minor version of RHEL, you might get inaccurate results in the vulnerability reports. For more information about supported operating systems for vulnerability reports, see supported operating systems.

説明：
Compute Engine の VM Manager が提供する脆弱性スキャン機能において、Red Hat Enterprise Linux (RHEL) の脆弱性レポートは、各メジャーバージョンの**最新のマイナーバージョン**に基づいて結果を生成するようになりました。このため、もしあなたのVMが最新ではない古いRHELマイナーバージョンを実行している場合、脆弱性レポートの結果が不正確になる可能性があります。

影響有無：
RHEL VMを運用しており、かつVM Managerの脆弱性レポート機能を利用して脆弱性管理を行っている場合に影響があります。RHELのマイナーバージョンが最新ではないVMでは、レポートの精度が低下し、セキュリティリスクの見落としや誤検知が発生する可能性があります。これはセキュリティ体制に直接的な影響を及ぼすため、重要な情報です。

対処方法：
1.  VM Managerの脆弱性レポートを利用しているRHEL VMがあるかを確認します。
2.  該当するRHEL VMのマイナーバージョンが最新であるかを確認します。
3.  もし古いマイナーバージョンのRHELを実行しているVMがある場合、それらのVMのRHELマイナーバージョンを最新に保つことを検討してください。RHELのアップデートはセキュリティ修正や安定性向上も含まれるため、定期的な適用が推奨されます。
4.  VM Managerの[サポートされているオペレーティングシステム](https://cloud.google.com/compute/docs/images/os-details#vm-manager)のリストを確認し、自身の環境が推奨構成と一致しているかを確認してください。

用語説明：
*   **VM Manager**: Compute EngineのVMインスタンスを一元的に管理・自動化するためのサービス。パッチの適用、設定の管理、脆弱性スキャン、インベントリ収集などの機能を提供し、VMの運用を効率化します。
*   **脆弱性レポート (Vulnerability Reports)**: VM Managerの機能の一つで、VMインスタンスに存在する既知のセキュリティ脆弱性（OSやソフトウェアの欠陥）を検出・報告する機能。これにより、セキュリティリスクを特定し、対策を講じることができます。
*   **RHEL (Red Hat Enterprise Linux)**: Red Hat社が提供する商用Linuxディストリビューション。企業向けの安定性、セキュリティ、サポートが特徴で、Google Cloud上でも広く利用されています。
*   **メジャーバージョン/マイナーバージョン**: ソフトウェアのバージョン管理における区分です。例として「RHEL 8.7」の場合、「8」がメジャーバージョン、「7」がマイナーバージョンに当たります。マイナーバージョンアップには、バグ修正やセキュリティパッチ、小規模な機能改善が含まれることが一般的です。

---

# Google Kubernetes Engine
## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.3-gke.1444000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.30.14-gke.2071000, 1.30.14-gke.2154000, 1.31.14-gke.1423000, 1.31.14-gke.1526000, 1.32.12-gke.1026000, 1.33.8-gke.1026000, 1.34.4-gke.1047000, 1.35.0-gke.2745005, 1.35.0-gke.3047001, 1.35.0-gke.3047002
- The following versions are no longer available in the Extended channel:
    - 1.30.14-gke.1991000, 1.30.14-gke.2117000, 1.31.14-gke.1336000, 1.31.14-gke.1476000, 1.32.11-gke.1211000, 1.33.5-gke.2392000, 1.34.3-gke.1318000, 1.35.0-gke.2398002, 1.35.0-gke.2745004
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.29 to 1.30.14-gke.2026000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.30 to 1.30.14-gke.2026000, 1.31 to 1.31.14-gke.1376000, 1.32 to 1.32.11-gke.1264000, 1.33 to 1.33.5-gke.2469000, 1.34 to 1.34.3-gke.1444000, 1.35 to 1.35.0-gke.2745005

## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.3-gke.1444000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.32.12-gke.1127000, 1.33.8-gke.1169000, 1.34.4-gke.1193000, 1.35.0-gke.2745005, 1.35.0-gke.3047002, 1.35.1-gke.1396001, 1.35.1-gke.1616000
- The following node versions are now available:
    - 1.30.14-gke.2154000, 1.31.14-gke.1526000, 1.32.12-gke.1127000, 1.33.8-gke.1169000, 1.34.4-gke.1193000, 1.35.0-gke.2745005, 1.35.0-gke.3047002, 1.35.1-gke.1396001, 1.35.1-gke.1616000
- The following versions are no longer available:
    - 1.32.11-gke.1038000, 1.33.5-gke.2172001, 1.34.3-gke.1051003, 1.35.0-gke.2398002, 1.35.0-gke.2745003, 1.35.0-gke.2745004, 1.35.1-gke.1396000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.31 to 1.32.11-gke.1264000, 1.32 to 1.33.5-gke.2326000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.32 to 1.32.11-gke.1264000, 1.33 to 1.33.5-gke.2326000, 1.34 to 1.34.3-gke.1444000, 1.35 to 1.35.0-gke.2745005

## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.1-gke.1396001 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
    - 1.32.12-gke.1127000, 1.33.8-gke.1169000, 1.34.4-gke.1193000, 1.35.1-gke.1396001, 1.35.1-gke.1616000
- The following versions are no longer available in the Rapid channel:
    - 1.32.12-gke.1026000, 1.33.8-gke.1026000, 1.34.4-gke.1047000, 1.35.0-gke.3047001, 1.35.1-gke.1396000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.31 to 1.32.12-gke.1076000, 1.32 to 1.33.8-gke.1112000, 1.33 to 1.34.4-gke.1130000, 1.34 to 1.35.1-gke.1396001
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.32 to 1.32.12-gke.1076000, 1.33 to 1.33.8-gke.1112000, 1.34 to 1.34.4-gke.1130000, 1.35 to 1.35.1-gke.1396001

## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.3-gke.1444000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
    - 1.32.12-gke.1026000, 1.33.8-gke.1026000, 1.34.4-gke.1047000, 1.35.0-gke.2745005, 1.35.0-gke.3047002
- The following versions are no longer available in the Regular channel:
    - 1.32.11-gke.1211000, 1.33.5-gke.2392000, 1.34.3-gke.1318000, 1.35.0-gke.2398002, 1.35.0-gke.2745004
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.31 to 1.32.11-gke.1264000, 1.32 to 1.33.5-gke.2469000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.32 to 1.32.11-gke.1264000, 1.33 to 1.33.5-gke.2469000, 1.34 to 1.34.3-gke.1444000, 1.35 to 1.35.0-gke.2745005

## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2326000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
    - 1.32.11-gke.1211000, 1.33.5-gke.2392000, 1.34.3-gke.1318000
- The following versions are no longer available in the Stable channel:
    - 1.32.11-gke.1038000, 1.33.5-gke.2228001, 1.34.3-gke.1051003
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.31 to 1.32.11-gke.1174000, 1.32 to 1.33.5-gke.2326000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.32 to 1.32.11-gke.1174000, 1.33 to 1.33.5-gke.2326000, 1.34 to 1.34.3-gke.1245000

## Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

説明：
Google Kubernetes Engine (GKE) の各リリースチャネル（Extended, Regular, Rapid, Stable）において、利用可能なGKEバージョンが更新されました。
具体的には、各チャネルでクラスタ作成時のデフォルトバージョンが新しいものに変更され、新たなGKEバージョン（コントロールプレーンおよびノード）が利用可能になり、同時に古いバージョンは利用不可になりました。
また、クラスタの自動アップグレードのターゲットとなるバージョンも更新されました。これにより、GKEは設定に基づき、自動的にクラスタをこれらの新しいバージョンにアップグレードする可能性があります。

影響有無：
GKEクラスタを運用している場合、利用しているリリースチャネルと現在のGKEバージョンに応じて影響があります。

*   **自動アップグレードの対象となるクラスタ**:
    *   自動アップグレードが有効なGKEクラスタは、新しいターゲットバージョン（パッチバージョンまたはマイナーバージョン）へ自動的にアップグレードされる可能性があります。
    *   マイナーバージョンアップの場合、Kubernetesの非推奨APIの削除、機能変更、動作変更などが発生する可能性があり、これらがアプリケーションやデプロイメントに影響を与える場合があります。特に、現在利用しているKubernetes APIが新しいバージョンで非推奨または削除される場合、アプリケーションが動作しなくなる可能性があります。
    *   セキュリティ修正やバグ修正が含まれるため、セキュリティ態勢の向上や安定性の確保には貢献しますが、事前の互換性検証が重要です。
*   **新規クラスタの作成**:
    *   新規クラスタを作成する際に、デフォルトで新しいGKEバージョンが適用されます。特定のバージョンを指定している場合は影響ありませんが、デフォルト設定を利用している場合は意図しないバージョンで作成される可能性があります。
*   **手動アップグレードの計画**:
    *   手動でGKEバージョンをアップグレードしている場合、利用可能なバージョンリストが更新されたため、アップグレード計画を見直す必要があります。利用不可になったバージョンに現在固定されている場合は、早急にアップグレード計画を立てる必要があります。
*   **Google Cloud Composer環境**:
    *   お客様の環境ではGoogle Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) を利用されていますが、Composerは内部的にGKEクラスタを使用しています。通常、ComposerのGKEバージョンはComposerの特定のバージョンに紐づいており、GKEの単独のリリースノートによるGKEバージョンの自動アップグレードは発生しません。
    *   しかし、Composerの将来的なバージョンアップで、今回アナウンスされたGKEバージョンへの移行が推奨または必須となる可能性があります。現在のComposer環境が利用しているGKEバージョンと、今回のアナウンスされたGKEバージョンの関係性（特に非推奨APIの有無など）を確認しておくことが重要です。

対処方法：
1.  **GKEクラスタのバージョンとチャネルの確認**: 運用中のGKEクラスタの現在のバージョンと、設定されているリリースチャネル（Extended, Regular, Rapid, Stable）を確認します。
2.  **自動アップグレード設定の確認**:
    *   メンテナンスウィンドウと除外期間が適切に設定されているかを確認し、予期しない時間帯のアップグレードを避けるようにします。
    *   本番環境のクラスタに対しては、マイナーバージョンアップの自動アップグレードを無効にするか、慎重に計画し、アップグレード前に十分なテストを実施することを強く推奨します。
3.  **互換性テストとアプリケーションの改修**:
    *   GKEのマイナーバージョンアップには、Kubernetesの非推奨APIの削除や機能変更が含まれることがあります。アップグレードを検討しているGKEバージョンの[Kubernetes Changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/)やGKEのドキュメントを確認し、非推奨となるAPIや重要な変更点がないか確認してください。
    *   必要に応じて、アプリケーションのDeploymentマニフェストやコードを修正し、新しいKubernetes APIバージョンに対応させるテストを開発環境やステージング環境で実行してください。
4.  **Google Cloud Composer環境の確認**:
    *   Google Cloud Composerの公式ドキュメントやリリースノートを参照し、Composer 2.7.1 (Airflow 2.7.3) がサポートするGKEバージョン、および将来のComposerバージョンで利用されるGKEバージョンについて確認します。
    *   現時点でのGKEバージョン更新がComposer環境に直接影響を与えることは少ないですが、Composerのバージョンアップを計画する際に、そのComposerバージョンが使用するGKEバージョンが今回の変更で影響を受ける可能性があるため、注意してください。

用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **リリースチャネル (Release Channel)**: GKEクラスタの自動アップグレードの頻度と安定性を制御するための設定。`Extended` (長期サポート), `Stable`, `Regular`, `Rapid` などのチャネルがあり、新しいGKEバージョンはこれらのチャネルに順次ロールアウトされます。
*   **自動アップグレード (Auto-upgrade)**: GKEクラスタのコントロールプレーンおよびノードが、Google Cloudによって自動的に最新のパッチバージョンまたはマイナーバージョンに更新される機能。
*   **メンテナンス除外期間 (Maintenance Exclusions)**: GKEクラスタの自動アップグレードや他のメンテナンス作業が行われるのを一時的に停止させる期間。特定の時間帯にクラスタの可用性を確保したい場合に設定します。
*   **非推奨API (Deprecated APIs)**: Kubernetesのバージョンアップに伴い、利用が推奨されなくなり、将来的に削除される予定のAPI。これらのAPIを使用しているアプリケーションは、互換性のある新しいAPIに移行する必要があります。
*   **Google Cloud Composer**: Apache AirflowをGoogle Cloud上で実行するためのマネージドサービス。ワークフローのオーケストレーションに使用され、内部でGKEクラスタを利用してAirflow環境を構築します。

# Title: February 25, 2026 
Link: https://docs.cloud.google.com/release-notes#February_25_2026<br>
Google Cloud のリリースノート調査結果をご報告いたします。

---

# BigQuery
## Change
原文: Effective *June 1, 2026*, BigQuery will limit legacy SQL use. This depends on whether your organization or project uses it from November 1, 2025, to June 1, 2026. If you don't use legacy SQL during this time, you won't be able to use it after June 1, 2026. If you do use it, your existing workloads will keep running, but new ones might not. For more information, see Legacy SQL feature availability.

[Legacy SQL feature availability](https://docs.cloud.google.com/bigquery/docs/legacy-sql-feature-availability)

説明：
BigQueryにおけるレガシーSQLの使用が2026年6月1日をもって制限されます。この制限は、2025年11月1日から2026年6月1日までの期間に、組織またはプロジェクトがレガシーSQLを使用したかどうかに基づきます。この期間にレガシーSQLを使用しなかった場合、2026年6月1日以降はレガシーSQLを使用できなくなります。もしこの期間に使用した場合、既存のワークロードは引き続き実行されますが、新しいワークロードについては実行できない可能性があります。

影響有無：
**影響あり（潜在的）**

*   **理由:** 貴社環境のGoogle Cloud Composer 2 (Airflow) は、BigQueryとの連携にBigQuery Operatorを使用する可能性があります。BigQuery OperatorはデフォルトでStandard SQLを使用しますが、もしカスタムのAirflow DAGs内で明示的にレガシーSQLを使用している場合は、将来的にそのワークロードが動作しなくなる可能性があります。特に、2025年11月1日から2026年6月1日の間にレガシーSQLの使用実績がない場合、2026年6月1日以降は完全にレガシーSQLが利用不可になります。

対処方法：
1.  **レガシーSQL使用状況の棚卸し:** 貴社環境のBigQueryプロジェクト内で、現在レガシーSQLを使用しているクエリやView、スクリプト（特にAirflow DAGs経由のクエリ）がないかを確認してください。BigQueryの監査ログ（Audit Logs）や `INFORMATION_SCHEMA.JOBS` テーブルを使って、 `query_type` が `LEGACY_SQL` であるジョブを特定できます。
2.  **Standard SQLへの移行:** レガシーSQLを使用している箇所が特定された場合、期限までにStandard SQLへの移行を計画・実行してください。Standard SQLはより高いパフォーマンスと柔軟性を提供します。
3.  **新規開発でのStandard SQLの徹底:** 今後のBigQueryを使用する開発においては、必ずStandard SQLを使用するように開発標準を徹底してください。

用語説明：
*   **レガシーSQL (Legacy SQL):** BigQueryが初期にサポートしていたSQL構文。`#legacySQL` というプレフィックスを付けることで使用できました。
*   **Standard SQL (標準SQL):** BigQueryの推奨されるSQL構文。ANSI SQL 2011に準拠しており、より多くの機能と最適化が提供されます。`#standardSQL` またはプレフィックスなしでデフォルトでStandard SQLが使用されます。
*   **ワークロード (Workload):** コンピューティングリソースを消費するタスクや処理の集合。BigQueryにおけるクエリ実行などがこれにあたります。

---

# Google Kubernetes Engine
## Change (Extended channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.3-gke.1318000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
- 1.30.14-gke.2026000
- 1.30.14-gke.2117000
- 1.31.14-gke.1376000
- 1.31.14-gke.1476000
- 1.32.11-gke.1264000
- 1.33.5-gke.2469000
- 1.34.3-gke.1444000
- 1.35.0-gke.2745004
- The following versions are no longer available in the Extended channel:
- 1.30.14-gke.1973000
- 1.30.14-gke.2071000
- 1.31.14-gke.1319000
- 1.31.14-gke.1423000
- 1.32.11-gke.1174000
- 1.33.5-gke.2326000
- 1.34.3-gke.1245000
- 1.35.0-gke.2232003
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.29 to 1.30.14-gke.1991000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.30 to 1.30.14-gke.1991000
- 1.31 to 1.31.14-gke.1336000
- 1.32 to 1.32.11-gke.1211000
- 1.33 to 1.33.5-gke.2392000
- 1.34 to 1.34.3-gke.1318000
- 1.35 to 1.35.0-gke.2398002

説明：
GKEのExtendedチャネルにおいて、新しいクラスター作成時のデフォルトバージョンが1.34.3-gke.1318000に変更されました。また、このチャネルで利用可能なGKEバージョンと利用不可になったGKEバージョンが更新されました。さらに、GKEの自動アップグレード（コントロールプレーンとノードの両方）のターゲットバージョンが更新され、特定の条件下でクラスターがこれらの新しいマイナーバージョンまたはパッチバージョンにアップグレードされる可能性があります。

影響有無：
**影響なし（直接的）**

*   **理由:** Google Cloud Composer 2 は通常、Standard または Regular チャネルの GKE クラスターを使用します。Extended チャネルは特定のワークロード向けであり、既存のComposer環境がこのチャネルを利用している可能性は低いと判断できます。ただし、GKEクラスターを手動で作成し、Composer以外のワークロードをExtendedチャネルで運用している場合は影響があります。

対処方法：
*   もしExtendedチャネルを利用しているGKEクラスターが存在する場合は、当該クラスターのバージョンと自動アップグレードのスケジュールを確認してください。メンテナンス期間の考慮や、非推奨APIの使用有無の確認が必要です。

用語説明：
*   **GKE Extended チャネル (GKE Extended Channel):** GKEのリリースチャネルの一つで、長期間のサポートが必要な本番環境のワークロードに適しています。新しいバージョンへの更新頻度は比較的低いですが、重要なセキュリティパッチやバグ修正は提供されます。
*   **自動アップグレード (Auto-upgrade):** GKEがクラスターのコントロールプレーンとノードを自動的に最新のバージョンに更新する機能。
*   **コントロールプレーン (Control Plane):** Kubernetesクラスターを管理するコンポーネント群（APIサーバー、スケジューラーなど）。
*   **ノード (Node):** Kubernetesクラスター内でコンテナ化されたワークロードを実行する仮想マシンまたは物理マシン。
*   **マイナーバージョンアップグレード (Minor Version Upgrade):** Kubernetesのマイナーバージョン番号（例: 1.29から1.30）が変更されるアップグレード。APIの変更や非互換性が含まれる可能性があります。
*   **パッチバージョンアップグレード (Patch Version Upgrade):** Kubernetesのパッチバージョン番号（例: 1.30.14から1.30.15）が変更されるアップグレード。通常、バグ修正やセキュリティパッチが含まれ、互換性の問題は少ないです。

---

# Google Kubernetes Engine
## Change (General Channel / Unspecified)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.3-gke.1318000 is now the default version for cluster creation.
- The following versions are now available:
- 1.32.12-gke.1076000
- 1.33.8-gke.1112000
- 1.34.4-gke.1130000
- 1.35.0-gke.2745004
- 1.35.0-gke.3047001
- 1.35.1-gke.1396000
- The following node versions are now available:
- 1.30.14-gke.2117000
- 1.31.14-gke.1476000
- 1.32.12-gke.1076000
- 1.33.8-gke.1112000
- 1.34.4-gke.1130000
- 1.35.0-gke.2745004
- 1.35.0-gke.3047001
- 1.35.1-gke.1396000
- The following versions are no longer available:
- 1.33.5-gke.2118001
- 1.35.0-gke.2232003
- 1.35.0-gke.2398000
- 1.35.0-gke.3047000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.31 to 1.32.11-gke.1211000
- 1.32 to 1.33.5-gke.2228001
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.32 to 1.32.11-gke.1211000
- 1.33 to 1.33.5-gke.2228001
- 1.34 to 1.34.3-gke.1318000
- 1.35 to 1.35.0-gke.2398002

説明：
GKEのデフォルトクラスター作成バージョンが1.34.3-gke.1318000に変更され、利用可能なGKEバージョンとノードバージョンが更新されました。また、利用不可になったバージョンもリストされています。この変更は、GKEの自動アップグレードのターゲットバージョンにも影響を与え、特定の条件下でクラスターが新しいマイナーバージョンまたはパッチバージョンにアップグレードされる可能性があります。このセクションは特定のリリースチャネルを明記していませんが、一般的に最新バージョンの提供状況を示唆しています。

影響有無：
**影響なし（直接的）**

*   **理由:** Composer 2.7.1は通常、GKE 1.25.xまたは1.26.xを使用しており、このリリースノートで言及されている1.30以降のGKEバージョンとは異なります。ただし、将来的にComposerをアップグレードする際には、GKEのバージョン互換性を確認する必要があります。

対処方法：
*   GKEクラスターを新規作成する場合や、既存クラスターのアップグレードを計画する際には、最新の利用可能なバージョンと自動アップグレードの振る舞いを考慮に入れてください。Composer環境のGKEバージョンは、Composerのバージョンに紐付いているため、Composerのアップグレードガイドを参照してください。

用語説明：
*   **GKE リリースチャネル (GKE Release Channel):** GKEのバージョン管理ポリシーで、Stable, Regular, Rapid, Extendedの4つのチャネルがあります。それぞれ新機能の導入頻度、安定性、サポート期間が異なります。

---

# Google Kubernetes Engine
## Change (Rapid channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.0-gke.3047001 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
- 1.32.12-gke.1076000
- 1.33.8-gke.1112000
- 1.34.4-gke.1130000
- 1.35.0-gke.3047001
- 1.35.1-gke.1396000
- The following versions are no longer available in the Rapid channel:
- 1.32.11-gke.1264000
- 1.33.5-gke.2469000
- 1.34.3-gke.1444000
- 1.35.0-gke.2745003
- 1.35.0-gke.3047000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.31 to 1.32.12-gke.1026000
- 1.32 to 1.33.8-gke.1026000
- 1.33 to 1.34.4-gke.1047000
- 1.34 to 1.35.0-gke.3047001
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.32 to 1.32.12-gke.1026000
- 1.33 to 1.33.8-gke.1026000
- 1.34 to 1.34.4-gke.1047000
- 1.35 to 1.35.0-gke.3047001

説明：
GKEのRapidチャネルにおいて、新しいクラスター作成時のデフォルトバージョンが1.35.0-gke.3047001に変更されました。また、このチャネルで利用可能なGKEバージョンと利用不可になったGKEバージョンが更新されました。GKEの自動アップグレードのターゲットバージョンも更新され、特定の条件下でクラスターがこれらの新しいマイナーバージョンまたはパッチバージョンにアップグレードされる可能性があります。

影響有無：
**影響なし（直接的）**

*   **理由:** Google Cloud Composer 2 は通常、Standard または Regular チャネルの GKE クラスターを使用します。Rapid チャネルは最速で新機能を提供するチャネルであり、Composer環境がこのチャネルを利用している可能性は低いと判断できます。

対処方法：
*   もしRapidチャネルを利用しているGKEクラスターが存在する場合は、当該クラスターのバージョンと自動アップグレードのスケジュールを確認してください。Rapidチャネルは更新頻度が高いため、継続的な監視と検証体制が必要です。

用語説明：
*   **GKE Rapid チャネル (GKE Rapid Channel):** GKEのリリースチャネルの一つで、最新の機能とセキュリティアップデートを最速で提供します。開発・検証環境や、新しい機能をいち早く利用したい場合に適しています。

---

# Google Kubernetes Engine
## Change (Regular channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.3-gke.1318000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
- 1.32.11-gke.1264000
- 1.33.5-gke.2469000
- 1.34.3-gke.1444000
- 1.35.0-gke.2745004
- The following versions are no longer available in the Regular channel:
- 1.32.11-gke.1174000
- 1.33.5-gke.2326000
- 1.34.3-gke.1245000
- 1.35.0-gke.2232003
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.31 to 1.32.11-gke.1211000
- 1.32 to 1.33.5-gke.2392000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.32 to 1.32.11-gke.1211000
- 1.33 to 1.33.5-gke.2392000
- 1.34 to 1.34.3-gke.1318000
- 1.35 to 1.35.0-gke.2398002

説明：
GKEのRegularチャネルにおいて、新しいクラスター作成時のデフォルトバージョンが1.34.3-gke.1318000に変更されました。また、このチャネルで利用可能なGKEバージョンと利用不可になったGKEバージョンが更新されました。GKEの自動アップグレードのターゲットバージョンも更新され、特定の条件下でクラスターがこれらの新しいマイナーバージョンまたはパッチバージョンにアップグレードされる可能性があります。

影響有無：
**影響なし（直接的）**

*   **理由:** Google Cloud Composer 2.7.1 は、基盤となる GKE バージョンとして通常は GKE 1.25.x または 1.26.x を使用します。このリリースノートで言及されているのはGKE 1.32以降のバージョンであり、既存のComposer環境のGKEバージョンとは異なるため、直接的な影響はありません。ただし、GKEの自動アップグレードパスに含まれるバージョンであり、将来的なComposerのアップグレード時に間接的に影響する可能性があります。

対処方法：
*   GKEクラスターを新規作成する場合や、既存クラスターのアップグレードを計画する際には、最新の利用可能なバージョンと自動アップグレードの振る舞いを考慮に入れてください。ComposerのGKEバージョンはComposerのバージョンに強く紐付いているため、Composerのアップグレードガイドラインに従うことが推奨されます。

用語説明：
*   **GKE Regular チャネル (GKE Regular Channel):** GKEのリリースチャネルの一つで、GKEクラスターのデフォルトチャネルです。新機能と安定性のバランスが取れており、多くの本番環境に適しています。
*   **メンテナンス除外 (Maintenance Exclusions):** GKEの自動アップグレードを一時的に停止する期間を設定する機能。特定の期間にクラスターのアップグレードを避けたい場合に使用します。
*   **非推奨API (Deprecated APIs):** Kubernetesの将来のバージョンで削除される予定のAPI。これらのAPIを使用しているアプリケーションは、互換性のある新しいAPIに移行する必要があります。

---

# Google Kubernetes Engine
## Change (Stable channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2228001 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
- 1.32.11-gke.1174000
- 1.33.5-gke.2326000
- 1.34.3-gke.1245000
- Version 1.33.5-gke.2172001 is no longer available in the Stable channel.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.5-gke.2228001
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.5-gke.2228001

説明：
GKEのStableチャネルにおいて、新しいクラスター作成時のデフォルトバージョンが1.33.5-gke.2228001に変更されました。また、このチャネルで利用可能なGKEバージョンと利用不可になったGKEバージョンが更新されました。GKEの自動アップグレードのターゲットバージョンも更新され、特定の条件下でクラスターが新しいマイナーバージョンまたはパッチバージョンにアップグレードされる可能性があります。

影響有無：
**影響なし（直接的）**

*   **理由:** Google Cloud Composer 2.7.1 は、基盤となる GKE バージョンとして通常は GKE 1.25.x または 1.26.x を使用します。このリリースノートで言及されているのはGKE 1.32以降のバージョンであり、既存のComposer環境のGKEバージョンとは異なるため、直接的な影響はありません。

対処方法：
*   GKEクラスターを新規作成する場合や、既存クラスターのアップグレードを計画する際には、最新の利用可能なバージョンと自動アップグレードの振る舞いを考慮に入れてください。特にStableチャネルは最も安定性が重視されるため、アップグレード前に十分なテストを実施することが推奨されます。

用語説明：
*   **GKE Stable チャネル (GKE Stable Channel):** GKEのリリースチャネルの一つで、最も安定性が高いと評価されたバージョンを提供します。新しい機能の導入は遅いですが、本番環境での使用に最も適しています。

---

# Google Kubernetes Engine
## Change (General announcement)
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明：
GKEクラスターのバージョンが更新され、新しいクラスター作成時や既存クラスターの手動アップグレード時に利用可能なバージョン
# Title: February 24, 2026 
Link: https://docs.cloud.google.com/release-notes#February_24_2026<br>
Google Cloud インフラエンジニアとして、ご依頼のリリースノートに基づき、構築済みのサービスへの影響有無を調査しました。以下に製品ごとの調査結果をまとめます。

---

# Apigee X

## Announcement
原文: On February 24th, 2026, we released an updated version of Apigee (1-17-0-apigee-3).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明： Apigeeの新しいバージョン (1-17-0-apigee-3) が2026年2月24日にリリースされました。この更新はGoogle Cloudの全ゾーンへの展開に4営業日以上かかる場合があります。ロールアウトが完了するまで、新しい機能や修正がインスタンスで利用できない可能性があります。

影響有無： **あり**
新しいApigeeバージョンが自動的に適用されるため、新しい機能の利用やパフォーマンス、安定性の向上が期待されます。ただし、ロールアウト期間中は、一部のGoogle Cloudゾーンで更新が遅れる可能性があります。

対処方法： 特になし。
本アップデートは自動的に適用されるため、お客様側で特別な操作は不要です。リリースノートの内容を把握し、今後の変更点や修正点にご留意ください。

用語説明：
*   **Apigee X**: Google Cloudが提供するエンタープライズグレードのAPI管理プラットフォームです。APIの設計、セキュリティ、デプロイ、監視、分析などを一元的に行います。
*   **ロールアウト (Rollout)**: ソフトウェアや機能が段階的に導入または展開されるプロセスを指します。これにより、変更による影響を最小限に抑えながら、大規模なシステムに更新を適用できます。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **481735779, 457138941, 471232237** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:  - CVE-2025-61730- CVE-2025-68156- CVE-2025-54388- CVE-2025-61727- CVE-2025-61729 |
This addresses the following vulnerabilities:  - CVE-2025-61730- CVE-2025-68156- CVE-2025-54388- CVE-2025-61727- CVE-2025-61729
[CVE-2025-61730](https://nvd.nist.gov/vuln/detail/CVE-2025-61730)
[CVE-2025-68156](https://nvd.nist.gov/vuln/detail/CVE-2025-68156)
[CVE-2025-54388](https://nvd.nist.gov/vuln/detail/CVE-2025-54388)
[CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)

説明： Apigeeのインフラストラクチャにおける複数のセキュリティ脆弱性（CVE-2025-61730、CVE-2025-68156、CVE-2025-54388、CVE-2025-61727、CVE-2025-61729）が修正されました。

影響有無： **なし（ポジティブな影響）**
本修正により、Apigee環境のセキュリティが強化され、潜在的な脆弱性が解消されます。システムへの直接的な悪影響はありません。

対処方法： 特になし。
セキュリティ修正は自動的に適用されます。お客様側での操作は不要です。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 既知のサイバーセキュリティの脆弱性および露出に一意の識別子を付与するためのシステムです。これにより、セキュリティ関連情報の共有と理解が容易になります。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **470375542** | Fixed a memory leak which could result in a spike in 503 responses with `no_healthy_upstream` messages. |
| **480997525** | Applied a fix for proxy calls failing with `The URI contains illegal characters` error after Netty upgrade. |
| **485595627** | Fixed an issue resulting in TLS handshake errors. |

説明：
*   メモリリークが原因で「`no_healthy_upstream`」メッセージを伴う503エラーが増加する問題が修正されました。
*   Nettyアップグレード後に「`The URI contains illegal characters`」エラーでプロキシ呼び出しが失敗する問題が修正されました。
*   TLSハンドシェイクエラーを引き起こす問題が修正されました。

影響有無： **なし（ポジティブな影響）**
これらの修正により、Apigeeの安定性と信頼性が向上します。もしこれらの事象に遭遇していた場合、問題が解消され、サービス品質が改善されます。

対処方法： 特になし。
これらのバグ修正は自動的に適用されます。お客様側での操作は不要です。

用語説明：
*   **503 Service Unavailable**: HTTPステータスコードの一つで、サーバーが一時的にリクエストを処理できない状態であることを示します。
*   **`no_healthy_upstream`**: ロードバランサーやプロキシが、トラフィックを転送すべきバックエンド（アップストリーム）に正常なインスタンスを見つけられない場合に発生するエラーメッセージです。
*   **メモリリーク (Memory Leak)**: プログラムが確保したメモリ領域を適切に解放せず、結果として利用可能なメモリが徐々に減少していく現象です。長期的にはシステムのパフォーマンス低下やクラッシュにつながる可能性があります。
*   **Netty**: 高パフォーマンスでスケーラブルなネットワークアプリケーションを開発するための非同期イベント駆動型ネットワークアプリケーションフレームワークです。
*   **TLSハンドシェイク (TLS Handshake)**: クライアントとサーバー間でTLS（Transport Layer Security）プロトコルに基づく暗号化された通信セッションを確立する際に、最初に行われる一連のネゴシエーションプロセスです。

---

# Cloud Load Balancing

## Other
原文: Backend Cloud Storage buckets are available for
regional external Application Load Balancers, regional internal Application Load Balancers, and
cross-region internal Application Load Balancers in a Shared VPC environment.
Support for this feature is available in **Preview** for
regional external Application Load Balancers and regional internal Application Load Balancers and in
**General availability** for cross-region internal Application Load Balancers. For more information,
see:
- Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment
- Set up a regional internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment
- Set up a cross-region internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment
[Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc-backend-buckets)
[Set up a regional internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-shared-vpc-buckets)
[Set up a cross-region internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-crilb-shared-vpc-backend-buckets)

説明： Shared VPC環境において、Cloud Storageバケットをバックエンドとして利用できるロードバランサーの種類が拡充されました。具体的には、地域外部アプリケーションロードバランサーと地域内部アプリケーションロードバランサーでプレビュー版として、クロスリージョン内部アプリケーションロードバランサーで一般提供（GA）版としてサポートされます。

影響有無： **なし（機能追加）**
既存のロードバランサー構成に直接的な影響はありません。Shared VPC環境でCloud Storageをバックエンドとするロードバランサーを検討している場合、より柔軟な選択肢が提供されます。

対処方法： 特になし。
この新機能を利用する場合は、記載されているドキュメントを参照して設定を行ってください。

用語説明：
*   **Cloud Load Balancing**: Google Cloudが提供する、アプリケーションへのトラフィックを複数のバックエンドサービスに効率的に分散させるためのサービス群です。
*   **Cloud Storage**: Google Cloudが提供する、スケーラブルで耐久性の高いオブジェクトストレージサービスです。静的コンテンツのホスティングやデータアーカイブに利用されます。
*   **Shared VPC (共有VPC)**: 組織内の複数のGoogle Cloudプロジェクトが、共通のVirtual Private Cloud (VPC) ネットワークを使用できるようにする機能です。これにより、ネットワークの一元管理とポリシーの適用が可能になります。
*   **Application Load Balancer**: HTTP(S) トラフィックを処理するレイヤー7のロードバランサーで、URLパスやヘッダーに基づいてトラフィックをルーティングできます。
*   **Preview (プレビュー)**: Google Cloudのサービスや機能が、一般提供（GA）される前の段階で公開されることを指します。通常、SLAやサポート体制はGA版とは異なる場合があります。
*   **General Availability (GA, 一般提供)**: Google Cloudのサービスや機能が、安定しており、本番環境での使用が推奨される段階に達したことを示します。

---

# Google Kubernetes Engine

## Change
原文: Expanded coverage for compute flexible committed use discounts (CUDs) is
available to all Cloud Billing accounts. All Cloud Billing accounts have
been automatically migrated to the new spend-based CUD model and you no longer need to opt
in to benefit from the expanded coverage. For the full list of eligible SKUs
across Compute Engine, GKE, and Cloud Run,
see SKU Groups - Compute Flexible CUD Eligible SKUs.
[new spend-based CUD model](https://docs.cloud.google.com/docs/cuds-multiprice)
[SKU Groups - Compute Flexible CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/compute-flexible-cud-eligible-skus)
To learn more about compute flexible CUDs and how they apply to your GKE usage, see
the GKE CUDs documentation.
[GKE CUDs documentation](https://docs.cloud.google.com/kubernetes-engine/cud)

説明： コンピュートフレキシブルコミット済み利用割引 (CUDs) の適用範囲が全てのCloud Billingアカウントに拡大されました。これにより、全てのCloud Billingアカウントは新しい利用額ベースのCUDモデルに自動的に移行され、お客様が明示的にオプトインすることなく、Compute Engine、GKE、Cloud Runを含む対象SKUに対して割引が適用されるようになります。

影響有無： **なし（ポジティブな影響）**
GKEを利用している場合、Compute EngineやCloud Runの利用を含め、対象となるComputeリソースの利用に対して自動的にCUDsが適用され、全体的なクラウド費用が削減される可能性があります。既存の課金設定が変更されるものではなく、割引が自動適用されるため、ユーザー側での追加の対応は不要です。

対処方法： 特になし。
お客様側で特別な操作は不要です。費用削減の効果を確認するために、Cloud Billingレポートを定期的に確認することをお勧めします。

用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するマネージドKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Committed Use Discounts (CUDs, コミット済み利用割引)**: Google Cloudが提供する料金割引モデルです。特定のGoogle Cloudリソースに対して1年または3年間の利用をコミットすることで、大幅な割引が適用されます。
*   **Compute flexible committed use discounts**: 特定のVMタイプやリージョンに限定されず、利用額に基づいて割引が適用される柔軟なCUDです。様々な種類のCompute Engine、GKE、Cloud Runの利用に適用されます。
*   **Cloud Billing accounts**: Google Cloudサービスの利用料金を追跡し、支払いを行うための管理単位です。
*   **Spend-based CUD model (利用額ベースのCUDモデル)**: リソースの具体的なインスタンスやタイプではなく、コミットされた利用料金に基づいて割引が適用されるCUDの方式です。
*   **SKU (Stock Keeping Unit)**: Google Cloudのサービスやリソースの課金対象となる最小単位を表します。
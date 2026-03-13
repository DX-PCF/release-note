
# Title: March 12, 2026 
Link: https://docs.cloud.google.com/release-notes#March_12_2026<br>
Google Cloud インフラエンジニアとして、リリースノートの調査結果を以下に報告します。

---

# BigQuery
## Change
原文: BigQuery advanced runtime is now enabled as the default runtime for all projects.
[BigQuery advanced runtime](https://docs.cloud.google.com/bigquery/docs/advanced-runtime)

説明: BigQueryのクエリ実行エンジンである「BigQuery advanced runtime（高度なランタイム）」が、すべてのプロジェクトにおいてデフォルトで有効になりました。これは、以前は特定の構成やOpt-inで利用可能だった新しいクエリエンジンが、明示的な設定なしに自動的に適用されることを意味します。

影響有無: 影響はありません。むしろ、BigQueryのクエリパフォーマンスが向上する可能性があります。既存のクエリやワークロードに対して、設定変更やコード修正は不要であり、透過的に適用されます。この変更は、BigQueryの安定性や互換性を損なうものではありません。

対処方法: 特に対処は不要です。BigQueryのクエリパフォーマンスの向上が期待できるため、継続的にクエリの実行時間やコストをモニタリングすることをお勧めします。

用語説明:
*   **BigQuery advanced runtime**: BigQueryがクエリを実行する際に使用する、最新かつ最適化された実行エンジンです。従来のエンジンと比較して、パフォーマンスの向上、より複雑なSQL機能のサポート、新しい機能の迅速な導入などが特徴です。BigQueryの機能拡張や最適化は、このランタイムを基盤として行われています。

---

# Cloud Logging
## Issue
原文: The automatic backfill operation performed on a log bucket that has been upgraded to use Log Analytics has been temporarily paused. To manually initiate the backfill operation, contact Cloud Customer Care.
[Cloud Customer Care](https://docs.cloud.google.com/stackdriver/docs/getting-support)

説明: Cloud Loggingにおいて、Log Analyticsを利用するようにアップグレードされたログバケットに対して、過去ログの自動バックフィル（既存データの取り込み）操作が一時的に停止されています。もし過去のログデータをLog Analyticsで分析する必要がある場合は、手動でバックフィル操作を開始するためにCloud Customer Careに問い合わせる必要があります。

影響有無: Log Analyticsを使用しているログバケットを最近アップグレードし、かつ、アップグレード前の過去のログデータをLog Analyticsで分析したい場合に影響があります。既存のログの取り込み、リアルタイムのログ分析、またはLog Analyticsを使用していないログバケットには影響しません。

対処方法:
1.  現在ご利用のCloud Loggingバケットのうち、Log Analyticsを有効にしているもの、または今後有効化を検討しているものがあるかを確認します。
2.  Log Analyticsを有効化したログバケットで、過去のログデータがBigQueryテーブルにバックフィルされていないことに起因する分析上の問題がある場合、または今後過去データの分析を計画している場合は、Cloud Customer Careに連絡し、手動バックフィルの依頼を行ってください。
3.  過去データのバックフィルが不要な場合は、特に対処は不要です。

用語説明:
*   **Log Analytics**: Cloud Loggingの機能の一つで、ログバケットに保存されているログデータを、BigQueryのSQL構文を用いて直接クエリ・分析できるようにする機能です。大量のログデータを効率的に集計・分析する際に有用です。
*   **Log bucket**: Cloud Loggingでログを保存するための論理的なコンテナです。ログの保持期間、保存リージョン、アクセス制御などを設定できます。
*   **Backfill operation**: 既存のデータソース（この場合は、Log Analytics有効化前のログバケットに保存されていたデータ）から、新しいデータ形式や場所に、過去のデータをまとめて取り込む操作を指します。

---

# Cloud Storage
## Change
原文: Object uploads that use customer-managed encryption keys (CMEK) now fail if the Cloud Storage service agent lacks the necessary IAM role to decrypt the object. For steps to grant the required role, see Assign a Cloud KMS key to a service agent.
[Assign a Cloud KMS key to a service agent](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access)

説明: 顧客管理の暗号鍵（CMEK）を使用してCloud Storageにオブジェクトをアップロードする際、Cloud Storageのサービスエージェントが、そのオブジェクトを復号するために必要なIAMロール（Cloud KMS CryptoKey Decrypter）を持っていない場合、アップロードが失敗するようになりました。以前は異なる挙動を示すことがありましたが、今後は明示的に失敗します。必要なロールを付与する手順は、提供されたドキュメントリンクに記載されています。

影響有無: 既存のシステムでCMEKを使用しているCloud Storageバケットに対して、ファイルのアップロードを行っている場合に影響があります。Cloud Storageサービスエージェント (`service-[PROJECT_NUMBER]@gs-project-accounts.iam.gserviceaccount.com`) に、関連するCloud KMSキーに対する `Cloud KMS CryptoKey Decrypter` (roles/cloudkms.cryptoKeyDecrypter) ロールが付与されていない場合、オブジェクトのアップロードが失敗する可能性があります。これは既存のワークフローに影響を与えるBreaking Changeです。

特に、以下の環境でCMEKを使用している場合は注意が必要です。
*   Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) を利用されており、AirflowのDAGファイル、プラグイン、ログなどが保存されるGCSバケットがCMEKで暗号化されている場合。
*   CMEKで暗号化されたGCSバケットに、アプリケーションやサービスアカウントからファイルを書き込んでいる場合。

対処方法:
1.  CMEKを使用しているCloud Storageバケットを特定します。
2.  特定した各バケットに関連付けられているCloud KMSキーを確認します。
3.  そのCloud KMSキーに対して、Cloud Storageサービスエージェント (`service-[PROJECT_NUMBER]@gs-project-accounts.iam.gserviceaccount.com`) が `Cloud KMS CryptoKey Decrypter` (roles/cloudkms.cryptoKeyDecrypter) ロールを保持しているか確認します。
4.  もしロールが付与されていない場合は、IAMポリシーを更新し、上記のロールを付与してください。
    *   具体的な手順は、リンク先のドキュメント「[Assign a Cloud KMS key to a service agent](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access)」を参照してください。
5.  変更後、CMEKを使用するアップロード処理が正常に完了するかをテスト環境で検証することを強く推奨します。

用語説明:
*   **Customer-managed encryption keys (CMEK)**: Google Cloud Storageに保存されるデータを、Googleが管理する鍵ではなく、ユーザー自身が管理する暗号鍵（Cloud Key Management Service (Cloud KMS) で管理）で暗号化する機能です。これにより、鍵のライフサイクル管理やアクセス制御をより細かく行うことが可能になります。
*   **Cloud Storage service agent**: Cloud Storageサービスがプロジェクト内で動作するために使用する特別なサービスアカウントです。通常、`service-[PROJECT_NUMBER]@gs-project-accounts.iam.gserviceaccount.com` の形式で識別されます。このサービスエージェントは、ストレージ操作やCloud KMSとの連携など、様々なタスクを実行する権限が必要です。
*   **IAM role**: Identity and Access Management (IAM) における、特定のGoogle Cloudリソースに対する権限の集合体です。ユーザーやサービスアカウントにIAMロールを付与することで、そのリソースに対する操作を許可します。
*   **Cloud KMS CryptoKey Decrypter (roles/cloudkms.cryptoKeyDecrypter)**: Cloud KMSの暗号鍵を使用してデータを復号するための権限を提供するIAMロールです。このロールがないと、CMEKで暗号化されたオブジェクトを読み取ったり、上書きしたりする際に問題が発生する可能性があります。
# Title: March 11, 2026 
Link: https://docs.cloud.google.com/release-notes#March_11_2026<br>
# Cloud Service Mesh

## Fixed (Security Update)

原文:
**1.28.5-asm.9 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the security vulnerabilities listed in
GCP-2026-013
as well as fixes for the following platform CVEs:
[GCP-2026-013](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-013)
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2025-13151 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2025-14831 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2025-15281 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2025-15467 | Yes | Yes | No | Yes | Medium (9.8) |
| CVE-2025-15558 | Yes | Yes | Yes | - | High (8.0) |
| CVE-2025-61726 | Yes | Yes | Yes | Yes | High (7.5) |
| CVE-2025-61728 | Yes | Yes | Yes | Yes | Medium (6.5) |
| CVE-2025-61730 | Yes | Yes | Yes | Yes | Medium (5.3) |
| CVE-2025-61731 | Yes | Yes | Yes | Yes | High (7.8) |
| CVE-2025-61732 | Yes | Yes | Yes | Yes | High (8.6) |
| CVE-2025-68121 | Yes | Yes | Yes | Yes | Critical (10) |
| CVE-2025-68160 | Yes | Yes | No | Yes | Low (4.7) |
| CVE-2025-69418 | Yes | Yes | No | Yes | Low (4.0) |
| CVE-2025-69419 | Yes | Yes | No | Yes | Low (7.4) |
| CVE-2025-69420 | Yes | Yes | Yes | Yes | Low (7.5) |
| CVE-2025-69421 | Yes | Yes | Yes | Yes | Low (7.5) |
| CVE-2025-8277 | Yes | Yes | No | Yes | Low (0) |
| CVE-2025-9820 | Yes | Yes | No | Yes | Low (4) |
| CVE-2026-0861 | Yes | Yes | No | Yes | Medium (8.4) |
| CVE-2026-0915 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-0964 | Yes | Yes | No | Yes | Medium |
| CVE-2026-0965 | Yes | Yes | No | Yes | Low |
| CVE-2026-0966 | Yes | Yes | No | Yes | Low |
| CVE-2026-0967 | Yes | Yes | No | Yes | Medium |
| CVE-2026-0968 | Yes | Yes | No | Yes | Medium |
| CVE-2026-22795 | Yes | Yes | No | Yes | Low (5.5) |
| CVE-2026-22796 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-24051 | Yes | Yes | Yes | Yes | High (7.0) |
| CVE-2026-25679 | Yes | Yes | Yes | Yes | High (7.5) |
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151)
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831)
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281)
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467)
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558)
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726)
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728)
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730)
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731)
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732)
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121)
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160)
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418)
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419)
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420)
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421)
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277)
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820)
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861)
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915)
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964)
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965)
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966)
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967)
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968)
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795)
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796)
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051)
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.28.5-asm.9 uses Envoy 1.36.5.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
Cloud Service Mesh (in-cluster版) のバージョン1.28.5-asm.9がリリースされました。このパッチリリースには、GCP-2026-013に記載されているセキュリティ脆弱性の修正に加え、多数のプラットフォームCVE（共通脆弱性識別子）に対する修正が含まれています。特に、SeverityがCritical (10) のCVE-2025-68121をはじめ、HighおよびMediumの多数の脆弱性が修正されています。このバージョンではEnvoy 1.36.5が使用されます。

影響有無：
**影響あり（セキュリティ強化と対応作業発生）**
Cloud Service Meshのin-cluster版を現在利用している場合、これらのセキュリティ修正はシステムのセキュリティ態勢を強化するために非常に重要です。特にCriticalレベルの脆弱性修正が含まれているため、アップグレードを強く推奨します。ただし、Composerはマネージドサービスであり通常はCloud Service Meshを直接利用しません。もし、Composerが稼働するGKEクラスタに別途Cloud Service Meshを導入している環境であれば、この更新は該当します。

対処方法：
現在in-cluster Cloud Service Meshを使用している場合、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)のドキュメントに従い、速やかにバージョン1.28.5-asm.9へのアップグレードを検討してください。アップグレード作業前に、既存環境との互換性確認およびテストを十分に行ってください。

用語説明：
*   **Cloud Service Mesh (ASM: Anthos Service Mesh)**: Google Cloudにおけるサービスメッシュの実装であり、マイクロサービス間のトラフィック管理、セキュリティ、可観測性などを提供します。
*   **In-cluster Cloud Service Mesh**: ユーザーがGoogle Kubernetes Engine (GKE) クラスタ内にコントロールプレーンをデプロイし、自身で管理するデプロイモデルです。
*   **パッチリリース (Patch Release)**: 主にバグ修正やセキュリティ修正に特化した小規模なソフトウェアリリースです。
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアの脆弱性を識別するための共通的な識別子です。
*   **Severity**: 脆弱性の深刻度を示す指標で、Critical (最も深刻) からLow (低い) まであります。
*   **Envoy Proxy**: Istio/ASMのデータプレーンでサイドカープロキシとして利用される高性能なオープンソースエッジ/サービスプロキシです。

---

## Fixed (Security Update)

原文:
**1.27.8-asm.7 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the security vulnerabilities listed in
GCP-2026-013
as well as fixes for the following platform CVEs:
[GCP-2026-013](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-013)
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2025-13151 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2025-14831 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2025-15281 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2025-15467 | Yes | Yes | Yes | Yes | Medium (9.8) |
| CVE-2025-15558 | Yes | Yes | Yes | - | High (8.0) |
| CVE-2025-61726 | Yes | Yes | Yes | Yes | High (7.5) |
| CVE-2025-61728 | Yes | Yes | Yes | Yes | Medium (6.5) |
| CVE-2025-61730 | Yes | Yes | Yes | Yes | Medium (5.3) |
| CVE-2025-61731 | Yes | Yes | Yes | Yes | High (7.8) |
| CVE-2025-61732 | Yes | Yes | Yes | Yes | High (8.6) |
| CVE-2025-68121 | Yes | Yes | Yes | Yes | Critical (10) |
| CVE-2025-68160 | Yes | Yes | No | Yes | Low (4.7) |
| CVE-2025-69418 | Yes | Yes | No | Yes | Low (4.0) |
| CVE-2025-69419 | Yes | Yes | No | Yes | Low (7.4) |
| CVE-2025-69420 | Yes | Yes | Yes | Yes | Low (7.5) |
| CVE-2025-69421 | Yes | Yes | Yes | Yes | Low (7.5) |
| CVE-2025-8277 | Yes | Yes | No | Yes | Low (0) |
| CVE-2025-9820 | Yes | Yes | No | Yes | Low (4) |
| CVE-2026-0861 | Yes | Yes | No | Yes | Medium (8.4) |
| CVE-2026-0915 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-0964 | Yes | Yes | No | Yes | Medium |
| CVE-2026-0965 | Yes | Yes | No | Yes | Low |
| CVE-2026-0966 | Yes | Yes | No | Yes | Low |
| CVE-2026-0967 | Yes | Yes | No | Yes | Medium |
| CVE-2026-0968 | Yes | Yes | No | Yes | Medium |
| CVE-2026-22795 | Yes | Yes | No | Yes | Low (5.5) |
| CVE-2026-22796 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-24051 | Yes | Yes | Yes | Yes | High (7.0) |
| CVE-2026-25679 | Yes | Yes | Yes | Yes | High (7.5) |
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151)
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831)
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281)
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467)
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558)
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726)
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728)
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730)
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731)
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732)
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121)
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160)
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418)
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419)
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420)
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421)
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277)
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820)
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861)
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915)
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964)
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965)
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966)
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967)
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968)
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795)
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796)
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051)
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.27.8-asm.7 uses Envoy 1.35.9.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)

説明：
Cloud Service Mesh (in-cluster版) のバージョン1.27.8-asm.7がリリースされました。このパッチリリースには、GCP-2026-013に記載されているセキュリティ脆弱性の修正に加え、多数のプラットフォームCVEに対する修正が含まれています。特に、SeverityがCritical (10) のCVE-2025-68121をはじめ、HighおよびMediumの多数の脆弱性が修正されています。このバージョンではEnvoy 1.35.9が使用されます。

影響有無：
**影響あり（セキュリティ強化と対応作業発生）**
Cloud Service Meshのin-cluster版を現在バージョン1.27.xで利用している場合、これらのセキュリティ修正はシステムのセキュリティ態勢を強化するために非常に重要です。特にCriticalレベルの脆弱性修正が含まれているため、アップグレードを強く推奨します。

対処方法：
現在in-cluster Cloud Service Meshを使用している場合、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)のドキュメントに従い、速やかにバージョン1.27.8-asm.7へのアップグレードを検討してください。アップグレード作業前に、既存環境との互換性確認およびテストを十分に行ってください。

用語説明：
*   **Cloud Service Mesh (ASM: Anthos Service Mesh)**: Google Cloudにおけるサービスメッシュの実装であり、マイクロサービス間のトラフィック管理、セキュリティ、可観測性などを提供します。
*   **In-cluster Cloud Service Mesh**: ユーザーがGoogle Kubernetes Engine (GKE) クラスタ内にコントロールプレーンをデプロイし、自身で管理するデプロイモデルです。
*   **パッチリリース (Patch Release)**: 主にバグ修正やセキュリティ修正に特化した小規模なソフトウェアリリースです。
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアの脆弱性を識別するための共通的な識別子です。
*   **Severity**: 脆弱性の深刻度を示す指標で、Critical (最も深刻) からLow (低い) まであります。
*   **Envoy Proxy**: Istio/ASMのデータプレーンでサイドカープロキシとして利用される高性能なオープンソースエッジ/サービスプロキシです。

---

## Fixed (Security Update)

原文:
**The following images are now rolling out for managed Cloud Service Mesh:**

- Sidecar version 1.21.6-asm.16 is rolling out to the rapid release channel.
- Sidecar version 1.20.8-asm.68 is rolling out to the regular release channel.
- Sidecar version 1.19.10-asm.61 is rolling out to the stable release channel.
- CNI and managed data plane controller version 1.23.6-asm.31 is rolling out to
all release channels.

These rollouts will preempt those previously announced on February 9, 2026.

[previously announced on February 9, 2026](#February_09_2026)
Managed Cloud Service Mesh will start using proxy version csm_mesh_proxy.20260304_RC00 for Gateway API on GKE clusters for all channels. This proxy version maps closest to Envoy version 1.37.

These patch releases contain the fixes for the vulnerabilities listed in
GCP-2026-013
as well as fixes for the following platform CVEs:

[GCP-2026-013](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-013)
| CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| CVE-2025-61726 | Yes | Yes | Yes | - | - | High (7.5) |
| CVE-2025-61728 | Yes | Yes | Yes | - | - | Medium (6.5) |
| CVE-2025-61730 | Yes | Yes | Yes | - | - | Medium (5.3) |
| CVE-2025-61731 | Yes | Yes | Yes | - | - | High (7.8) |
| CVE-2025-61732 | Yes | Yes | Yes | - | - | High (8.6) |
| CVE-2025-68121 | Yes | Yes | Yes | - | - | Critical (10) |
| CVE-2025-68160 | Yes | Yes | No | - | - | Low (4.7) |
| CVE-2025-69418 | Yes | Yes | No | - | - | Low (4.0) |
| CVE-2025-69419 | Yes | Yes | No | - | - | Low (7.4) |
| CVE-2025-69420 | Yes | Yes | No | - | - | Low (7.5) |
| CVE-2025-69421 | Yes | Yes | No | - | - | Low (7.5) |
| CVE-2025-8277 | - | - | - | Yes | Yes | Low (0) |
| CVE-2025-9820 | - | - | - | Yes | Yes | Low (4.0) |
| CVE-2025-14831 | - | - | - | Yes | Yes | Medium (5.3) |
| CVE-2025-15281 | Yes | Yes | Yes | - | - | Medium (7.5) |
| CVE-2025-15467 | Yes | Yes | No | - | - | Medium (9.8) |
| CVE-2026-0861 | Yes | Yes | No | - | - | Medium (8.4) |
| CVE-2026-0915 | Yes | Yes | No | - | - | Medium (7.5) |
| CVE-2026-0964 | - | - | - | Yes | Yes | Medium |
| CVE-2026-0965 | - | - | - | Yes | Yes | Low |
| CVE-2026-0966 | - | - | - | Yes | Yes | Low |
| CVE-2026-0967 | - | - | - | Yes | Yes | Medium |
| CVE-2026-0968 | - | - | - | Yes | Yes | Medium |
| CVE
# Title: March 10, 2026 
Link: https://docs.cloud.google.com/release-notes#March_10_2026<br>
# Cloud Composer
## Announcement
原文: Cloud Composer 2 environments can no longer be created in Turin (europe-west12). We're switching this region to supporting only Cloud Composer 3 environments.

説明：
Google Cloud Composer 2環境について、Turinリージョン（europe-west12）での新規作成が不可能になりました。このリージョンは、今後はCloud Composer 3環境のみをサポートするよう変更されます。

影響有無：
影響なし。
理由：
この変更はTurin (europe-west12) リージョンにおけるCloud Composer 2環境の「新規作成」に限定されるものであり、現在運用中のCloud Composer 2環境（Composer version 2.7.1, Airflow version 2.7.3）には直接的な影響はありません。

対処方法：
なし。
現在運用中のCloud Composer 2環境への影響はありませんので、特別な対処は不要です。
将来的にTurin (europe-west12) リージョンでCloud Composer 2環境を新規作成する計画がある場合は、他のリージョンを選択するか、Cloud Composer 3環境への移行を検討する必要があります。

用語説明：
*   **Google Cloud Composer**: Google Cloud上でApache Airflowをフルマネージドサービスとして実行するための環境です。ワークフローの定義、スケジューリング、監視、実行を容易に行うことができます。
*   **Apache Airflow**: プログラマティックにワークフローをオーサリング、スケジューリング、監視するためのオープンソースプラットフォームです。複雑なデータパイプラインのオーケストレーションによく用いられます。
*   **Turin (europe-west12)**: イタリアのトリノに位置するGoogle Cloudのリージョン名です。リージョンは、Google Cloudリソースが物理的にデプロイされる特定の地理的エリアを示します。
*   **Cloud Composer 2 / Cloud Composer 3**: Cloud Composerの異なるメジャーバージョンです。Cloud Composer 3は、Composer 2と比較して、より新しいAirflowバージョンをサポートし、パフォーマンス、スケーラビリティ、コスト効率の面で改善が加えられています。
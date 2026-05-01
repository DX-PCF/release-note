
# Title: April 30, 2026 
Link: https://docs.cloud.google.com/release-notes#April_30_2026<br>
はい、承知いたしました。Google Cloudのインフラエンジニアとして、提供されたリリースノートに基づき、既存のサービスへの影響と必要な対応を調査し、簡潔に回答いたします。

---

# BigQuery

## Breaking

**原文:**
Starting May 7, 2026, new transfer configurations that transfer data from Google Ads using the BigQuery Data Transfer Service will require Multi-factor authentication (MFA) for individual user authentication.
For more information, see May 7, 2026.

[Multi-factor authentication (MFA) for individual user authentication](https://ads-developers.googleblog.com/2026/04/multi-factor-authentication-requirement.html)
[May 7, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#May7-google-ads)

**説明:**
2026年5月7日より、BigQuery Data Transfer Service を使用してGoogle広告からデータを転送する**新しい転送設定**において、個々のユーザー認証に多要素認証（MFA）が必須となります。これはセキュリティ強化を目的とした変更です。

**影響有無:**
*   **影響あり（将来的な新規設定に限定）**
*   現在稼働中の既存のGoogle広告からのデータ転送設定には直接的な影響はありません。
*   2026年5月7日以降に新規でGoogle広告からのデータ転送設定を作成する際には、MFAが有効なユーザーアカウントを使用する必要があります。この期限はまだ先ですが、今後の計画に含める必要があります。

**対処方法:**
1.  **現状確認:** BigQuery Data Transfer Service を利用してGoogle広告からのデータ転送を現在行っているかを確認してください。
2.  **MFA有効化の計画:** 2026年5月7日以降にGoogle広告からのデータ転送を新規に設定する可能性がある場合、その際に使用するGoogle Cloudのユーザーアカウント（またはGoogle広告連携用のサービスアカウントと関連付けられたユーザー）がMFAを有効にしていることを確認、または有効化を計画してください。
3.  **情報共有:** この将来の変更について、BigQueryおよびGoogle広告のデータ連携に関わるチームメンバーと情報を共有し、認識を合わせてください。

**用語説明:**
*   **BigQuery Data Transfer Service:** Google Cloudの様々なデータソース（Google広告、Googleアナリティクス、YouTubeなど）からBigQueryへデータを自動的に転送・ロードするサービスです。
*   **Multi-factor authentication (MFA) / 多要素認証:** ユーザー認証のセキュリティを強化するための方法で、パスワードに加え、スマートフォンアプリのコードやセキュリティキーなど、複数の種類の認証情報（要素）を要求します。

---

# Cloud SQL for PostgreSQL

## Fixed

**原文:**
Cloud SQL has made the following enhancements to expand the list of eligible Cloud SQL Enterprise Plus edition instances that support planned operations with near-zero downtime.

[near-zero downtime](https://docs.cloud.google.com/sql/docs/postgres/availability#near-zero-downtime)
- Instances with connector enforcement enabled are eligible for planned operations with near-zero downtime.
- Instances that use private services access with a non-RFC 1918 IP address are eligible for planned operations with near-zero downtime.

[connector enforcement enabled](https://docs.cloud.com/sql/docs/postgres/connect-connectors#enforce)
[private services access](https://docs.cloud.com/sql/docs/postgres/configure-private-services-access)

**説明:**
Cloud SQL for PostgreSQLのEnterprise Plusエディションにおいて、「ほぼゼロダウンタイム（near-zero downtime）」での計画メンテナンスが適用されるインスタンスの対象範囲が拡大されました。具体的には、以下の条件を満たすインスタンスも、この機能の恩恵を受けられるようになりました。
*   コネクタ強制が有効になっているインスタンス。
*   非RFC 1918 IPアドレスを持つプライベートサービスアクセスを使用するインスタンス。

**影響有無:**
*   **影響なし（ポジティブな改善）**
*   これは機能の改善であり、既存の構成にマイナスの影響を与えるものではありません。
*   むしろ、上記に該当する設定のCloud SQL Enterprise Plusインスタンスを利用している場合、計画メンテナンス時のダウンタイムが大幅に短縮されるため、サービスの高可用性向上に貢献します。

**対処方法:**
*   **特段の対処は不要です。**
*   もし現在、Cloud SQL Enterprise Plusエディションで「コネクタ強制」を有効にしている、または「非RFC 1918 IPアドレスを含むプライベートサービスアクセス」を使用しているインスタンスがある場合、今後の計画メンテナンスにおいて、より短いダウンタイムで運用が継続できることを認識してください。

**用語説明:**
*   **Cloud SQL Enterprise Plus edition:** Cloud SQLの最上位エディションで、高可用性、パフォーマンス、セキュリティ機能が強化されています。
*   **Planned operations with near-zero downtime / ほぼゼロダウンタイムでの計画メンテナンス:** Cloud SQLが提供する機能で、インスタンスのメンテナンス（バージョンアップグレード、パッチ適用など）を、アプリケーションへの影響を最小限に抑えつつ（通常数秒のダウンタイム）実行できるようにするものです。
*   **Connector enforcement / コネクタ強制:** Cloud SQLインスタンスへの接続をCloud SQL Auth Proxyなどのセキュアなコネクタの使用に強制するセキュリティ機能です。これにより、平文での接続が禁止され、認証と暗号化が強化されます。
*   **Private services access / プライベートサービスアクセス:** Google Cloudのサービス（Cloud SQLなど）とVPCネットワーク間のプライベートな接続を可能にする機能です。インターネットを経由せず、内部IPアドレスで接続できるため、セキュリティとネットワークパフォーマンスが向上します。
*   **RFC 1918 IP address:** プライベートネットワークで使用するためにIANAによって予約されているIPアドレス範囲（例: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16）を指します。非RFC 1918 IPアドレスは、これらの範囲外のIPアドレスで、通常はパブリックIPアドレスや特定のサービスプロバイダーの割り当て範囲などを意味します。
# Title: April 29, 2026 
Link: https://docs.cloud.google.com/release-notes#April_29_2026<br>
Google Cloud インフラエンジニアとして、ご提示いただいたリリースノートに基づき、構築済みのサービスへの影響有無を調査し、以下の通りご報告いたします。

---

# Apigee X

## Announcement

原文: `On April 29th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows. If you set a preferred window for maintenance for your instance, and your instance version is below 1-17-0-apigee-4, your instance will be updated to 1-17-0-apigee-4 within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days. Note: Instances that meet either of the following two criteria will not be updated: - Your instance has a DNS misconfiguration, as described in Known Issue 445936920. - Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025. For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.`

説明: Apigee Xインスタンスのメンテナンスアップデートが2026年4月29日から開始されました。メンテナンスウィンドウを設定しており、かつインスタンスのバージョンが`1-17-0-apigee-4`未満の場合、今後7〜21日以内に`1-17-0-apigee-4`へ自動的に更新されます。アップグレード予定日を含む通知が2営業日以内に送信されます。ただし、DNS設定ミスがあるインスタンスや、2025年10月16日のリリースノートで説明されている廃止されたApigee Javaライブラリを使用しているインスタンスは更新されません。

影響有無: **影響の可能性あり**
当組織でApigee Xインスタンスを運用しており、メンテナンスウィンドウを設定している場合、今回のアップデートの対象となる可能性があります。特に、インスタンスのバージョンが`1-17-0-apigee-4`未満である場合は自動更新の対象となります。既存の連携やAPIの挙動に影響がないか、事前に確認が必要です。

対処方法:
1.  Apigee Xインスタンスが運用されているか確認してください。
2.  運用している場合は、インスタンスのバージョンを確認し、`1-17-0-apigee-4`未満であるかを確認してください。
3.  メンテナンスウィンドウを設定しているか確認してください。
4.  Apigeeからのアップグレード通知を確実に受信できるよう、連絡先メールアドレスが正しく設定されているか確認してください。
5.  対象となる場合は、アップグレード前に、DNS設定ミスや廃止されたJavaライブラリの使用がないことを確認してください。

用語説明:
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォーム。APIの設計、セキュリティ、デプロイ、監視、分析などを一元的に行います。
*   **メンテナンスウィンドウ**: クラウドサービスが定期的なメンテナンスを実行する際に、ユーザーが希望する時間帯を指定する機能。これにより、業務への影響を最小限に抑えることができます。
*   **Apigee Java Library**: Apigeeでカスタムポリシーなどを開発する際に使用されるJavaライブラリ。廃止されたライブラリを使用していると、インスタンスが更新されない場合があります。

---

# BigQuery

## Breaking

原文: `Strict act-as mode is enforced globally for all Dataform repositories, requiring the use of a custom service account or user credentials for running Dataform workflows, BigQuery pipelines, notebooks, and data preparations.`

説明: Dataformの全リポジトリに対し、厳格な「act-asモード」がグローバルに適用されます。これにより、Dataformのワークフロー、BigQueryパイプライン、ノートブック、データ準備を実行する際には、カスタムサービスアカウントまたはユーザー認証情報の使用が必須となります。

影響有無: **影響の可能性あり（Breaking Change）**
当組織でBigQueryを利用しており、特にDataformを使用してデータパイプラインを構築・運用している場合、この変更は直接的な影響を及ぼします。既存のDataformジョブやワークフローが、カスタムサービスアカウントやユーザー認証情報を使用せず、デフォルトのDataformサービスアカウントなどで実行されている場合、ジョブの実行が失敗する可能性があります。

対処方法:
1.  当組織でDataformを使用しているか確認してください。
2.  Dataformを使用している場合、既存のワークフローがジョブ実行時にどのような認証情報を使用しているかを確認してください。
3.  カスタムサービスアカウントやユーザー認証情報を使用していない場合、ワークフローを修正し、適切な認証情報を設定するようにしてください。
4.  [Strict act-as modeのドキュメント](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) を参照し、詳細な移行手順を確認してください。

用語説明:
*   **Dataform**: BigQuery上でデータ変換パイプラインを構築・管理するためのサービス。SQLワークフローのバージョン管理、テスト、デプロイなどを行います。
*   **act-as mode (act-as モード)**: ある主体（この場合Dataform）が別の主体（指定されたサービスアカウントやユーザー）の権限を借用して操作を実行する機能。厳格化されたことにより、権限借用の設定がより明確かつ限定的になる必要があります。
*   **カスタムサービスアカウント**: Google Cloudプロジェクト内で作成し、特定の権限を付与できるサービスアカウント。デフォルトで作成されるサービスアカウント（例: Dataformサービスアカウント）とは異なり、より細かく権限を制御できます。
*   **Breaking Change**: 既存のシステムやアプリケーションの動作に非互換性のある変更をもたらす変更。通常、上位バージョンへの移行時に既存のコードや設定の修正が必要となります。

---

# Google Kubernetes Engine

当組織はGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) を利用しており、ComposerはGKEを基盤としているため、以下のGKEに関するリリースノートは直接的な関連があります。

## Change

原文: `GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.`

説明: GKEクラスタのバージョンが更新され、新規クラスタ作成および既存クラスタの手動アップグレード、ノードアップグレードに利用可能な新しいバージョンが提供されました。Stable、Regular、Rapid、Extendedの各チャネルにおいて、利用可能なバージョン、デフォルトバージョン、非推奨バージョンが更新されています。また、自動アップグレードのターゲットバージョンも変更されました。

影響有無: **影響なし（ただし、情報として重要）**
Google Cloud Composer 2はフルマネージドサービスであり、基盤となるGKEクラスタのバージョンアップグレードはGoogle Cloudによって自動的に管理されます。したがって、当組織が直接GKEクラスタのバージョンアップグレードを行う必要はありません。しかし、利用可能な最新バージョンや非推奨バージョンに関する情報は、今後のComposerのバージョンアップグレード戦略を理解する上で重要です。

対処方法:
*   特段の対処は不要です。Google Cloud Composerのメンテナンスサイクルに従い、基盤となるGKEバージョンはGoogleによって適切に管理されます。
*   ただし、Composerの特定のマイナーバージョンが、今後非推奨となるGKEバージョンに依存している場合は、Google Cloudからバージョンアップグレードの推奨や通知がある可能性があるので、それらには注意を払ってください。

用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **GKEチャネル**: GKEクラスタのバージョンアップグレードの頻度と安定性を示す設定（Release Channel）。Stable, Regular, Rapid, Extendedなどがあり、安定性や新機能の導入速度が異なります。Composerは通常、安定性の高いチャネルを使用します。
*   **コントロールプレーン**: Kubernetesクラスタの脳となる部分で、APIサーバー、スケジューラ、コントローラマネージャー、etcdなどで構成されます。
*   **ノード**: コンテナ化されたアプリケーションを実行するワーカーマシン。

## Security

原文: `This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image: GKE version Container-Optimized OS version Details 1.31.14-gke.1823000 cos-117-18613-534-80 cos-117-18613-534-80 release notes 1.36.0-gke.1379000 cos-125-19216-220-130 cos-125-19216-220-130 release notes`

説明: 今回のGKEリリースには、更新されたContainer-Optimized OS（COS）イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたイメージは累積的なものであり、前回のGKEリリース以降に公開されたすべてのCOSバージョンからのセキュリティ修正が組み込まれています。

影響有無: **影響なし（セキュリティ強化）**
Google Cloud Composerの基盤となるGKEノードのOSイメージにセキュリティ修正が適用されることを示しています。これは、当組織のComposer環境のセキュリティ体制を強化するものであり、ポジティブな変更です。ユーザーが直接対処する必要はありません。

対処方法:
*   特段の対処は不要です。Composerの基盤セキュリティが向上します。

用語説明:
*   **Container-Optimized OS (COS)**: Google CloudがGKEノードのために最適化した、コンテナ実行に特化したLinuxディストリビューション。セキュリティ、信頼性、パフォーマンスが最適化されています。
*   **累積的なセキュリティ修正**: これまでの全ての修正を含む形で提供されるセキュリティアップデート。

## Fixed

原文: `In GKE versions earlier than 1.34.6-gke.1154000 and 1.35.2-gke.1691000, mounting Cloud Storage buckets by using the Cloud Storage FUSE CSI driver can experience significant delays. This issue typically manifests as a CreateContainer error that states the following message: failed to reserve container name. This error is self-healing and resolves automatically after the underlying mount operation completes and the container runtime releases the reservation. The delay is caused by an inefficient bucket access check performed by the CSI driver sidecar by using the ListObjects API method, which can take several hours to complete on buckets that contain millions of empty folders. The error occurs because the kubelet enforces a strict two-minute timeout for the container creation request. If the FUSE mount process exceeds this time limit while the sidecar is performing the initial bucket access check, then the kubelet cancels the operation and retries. However, the container runtime remains blocked on the first attempt and retains the reservation for the container name. The new GKE releases fix this issue by replacing the ListObjects check with the GetStorageLayout API method, which performs the same validation but returns almost instantly in most cases. To resolve this issue, upgrade your cluster to one of the following versions: - 1.34.6-gke.1154000 or later - 1.35.2-gke.1691000 or later For GKE version 1.33 clusters running version 1.33.5-gke.2435000 or later, you can mitigate this issue by setting the skipCSIBucketAccessCheck: "true" volume attribute to bypass the check. There is no supported fix for this issue in cluster versions 1.33.5-gke.2435000 and earlier.`

説明: GKEバージョン1.34.6-gke.1154000および1.35.2-gke.1691000より前のバージョンにおいて、Cloud Storage FUSE CSIドライバーを使用してCloud Storageバケットをマウントする際に、著しい遅延が発生する問題が修正されました。この問題は通常、`failed to reserve container name`という`CreateContainer error`として現れ、数百万個の空のフォルダを含むバケットで発生しやすかったものです。新しいGKEリリースでは、`ListObjects` API呼び出しをより効率的な`GetStorageLayout` APIメソッドに置き換えることでこの問題が解決されました。

影響有無: **影響の可能性あり（パフォーマンス改善・エラー回避）**
当組織が利用しているGoogle Cloud Composer 2.7.1（Airflow 2.7.3）環境の基盤GKEバージョンが、この問題の影響を受けるバージョン（1.34.6-gke.1154000および1.35.2-gke.1691000より前）に該当し、かつCloud Storage FUSE CSIドライバー経由で大量のファイルを含むCloud Storageバケットをマウントするようなワークロードを実行している場合、この修正によってパフォーマンスの向上やエラーの回避が期待できます。
Composerは通常、Cloud Storageと密接に連携するため、このCSIドライバーが内部的に使用されている可能性があります。

対処方法:
1.  現在のGoogle Cloud Composer 2.7.1環境の基盤GKEバージョンを確認してください。これはComposerの環境詳細ページや`gcloud composer environments describe`コマンドで確認できます。
2.  もし現在のGKEバージョンが影響を受けるバージョン範囲（1.34.6-gke.1154000より前、または1.35.2-gke.1691000より前）に該当する場合、Google Cloud Composerのバージョンアップグレードを検討してください。Composerのバージョンアップグレードにより、基盤となるGKEバージョンも自動的に更新され、この修正が適用されます。
3.  もしGKEバージョンが1.33.5-gke.2435000以降の1.33系クラスタで、すぐにComposerをアップグレードできない場合は、一時的な緩和策として`skipCSIBucketAccessCheck: "true"`ボリューム属性を設定することでこのチェックをバイパスできる可能性があります。ただし、Composerでの設定変更可否を確認する必要があります。
4.  この問題が既に発生している場合（`CreateContainer error`やマウント遅延など）、Composer環境のGKEバージョンが修正バージョン以降に更新されるのを待つか、手動でのアップグレードを検討してください（Composerは自動アップグレードが基本ですが、メジャー・マイナーバージョンアップは手動トリガーが必要な場合が多い）。

用語説明:
*   **Cloud Storage FUSE CSI driver**: Kubernetesクラスタ内でCloud StorageバケットをファイルシステムのようにマウントするためのCSI（Container Storage Interface）ドライバー。これにより、PodがCloud Storage上のデータに直接アクセスできるようになります。
*   **CSI (Container Storage Interface)**: Kubernetesなどのコンテナオーケストレーションシステムが、様々なストレージシステムと連携するための標準インターフェース。
*   **ListObjects API method**: Cloud Storageバケット内のオブジェクト（ファイルやフォルダ）の一覧を取得するためのAPIメソッド。大量の空のフォルダがある場合に時間がかかることがあります。
*   **GetStorageLayout API method**: Cloud Storageのストレージレイアウトに関する情報を取得するAPIメソッド。`ListObjects`よりも効率的な検証が可能です。
*   **kubelet**: Kubernetesクラスタ内の各ノードで実行されるエージェント。コンテナの作成、Podの起動・停止、ヘルスチェックなど、ノード上のコンテナを管理します。

## Change (Stable, Regular, Rapid, Extended Channels)

原文: (各チャネルのバージョン更新に関する詳細なリスト。省略して説明します。)
`GKE cluster versions have been updated.`
`New versions available for upgrades and new clusters.`
`The following versions are now available in the Stable channel: ...`
`The following versions are no longer available in the Stable channel: ...`
`Clusters in this channel running the listed minor version have new general auto-upgrade targets. ...`

説明: GKEの各リリースチャネル（Stable、Regular、Rapid、Extended）において、利用可能な新しいGKEバージョンが追加され、一部の古いバージョンが非推奨または利用不可になりました。また、自動アップグレードのターゲットバージョンも各チャネルで更新されています。非推奨になったバージョンは、90日以内またはサポート終了の早い方で削除されます。

影響有無: **影響なし（ただし、情報として重要）**
Google Cloud Composer 2はGKEの特定のバージョン範囲で動作し、その基盤となるGKEクラスタはGoogle Cloudによって自動的に管理・アップグレードされます。そのため、当組織が直接これらのGKEバージョン選択やアップグレードを行う必要はありません。しかし、当組織のComposer環境が現在使用しているGKEバージョンが非推奨リストに含まれていないかを確認することは重要です。もし含まれている場合、Google CloudがComposer環境のGKEバージョンを自動的にアップグレードする予定があることを意味します。

対処方法:
*   特段の対処は不要です。ComposerのGKEバージョンはGoogleによって自動的に管理されます。
*   現在のComposer 2.7.1の基盤GKEバージョンを把握し、それが今回のリリースノートで「deprecated（非推奨）」とされているバージョンに含まれていないか確認してください。非推奨バージョンに含まれている場合、自動アップグレードのスケジュールに注意を払う必要があります。
*   Composerのリリースノートや通知を定期的に確認し、基盤GKEバージョンの更新に関する情報を把握してください。

用語説明:
*   **GKEリリースチャネル**: GKEクラスタのバージョン管理方法。新機能の適用速度と安定性のバランスに応じて、Static, Regular, Stable, Rapid, Extendedなどのチャネルを選択できます。Composer 2は通常、自動アップグレードを前提としたチャネルを使用します。
*   **非推奨 (deprecated)**: 将来的にサポートが終了し、利用できなくなる予定の機能やバージョン。通常、代替手段が提供され、移行期間が設けられます。
# Title: April 28, 2026 
Link: https://docs.cloud.google.com/release-notes#April_28_2026<br>
# AlloyDB for PostgreSQL
## Change
原文: When the initial user or password is unspecified during cluster creation, a locked `postgres` role with `null` password is created.
[`postgres` role](https://docs.cloud.google.com/alloydb/docs/database-users/overview#postgres-user)

説明：
AlloyDB for PostgreSQLのクラスターを作成する際、初期ユーザー（通常は `postgres` ロール）またはそのパスワードを明示的に指定しなかった場合、これまではシステムのデフォルト動作に依存していましたが、この変更により、ユーザーがアクセスできないように「ロックされた」状態の `postgres` ロールが、パスワードなし（`null` パスワード）で作成されるようになりました。これは、セキュリティを強化し、意図しないデフォルトパスワードやアクセス可能な状態でのスーパーユーザーロールの作成を防ぐための変更です。

影響有無：
**限定的ですが、間接的に影響あり。**
*   **影響がないケース:** クラスター作成時に初期ユーザー（`postgres` ロール）のパスワードを常に明示的に指定している場合、この変更による直接的な影響はありません。これはセキュリティベストプラクティスに沿った運用であり、推奨される方法です。
*   **影響があるケース:** クラスター作成時に意図的に、または誤って初期ユーザーやパスワードを指定しなかった場合、これまでであれば何らかのデフォルトの動作で `postgres` ロールが作成された可能性がありましたが、今後はその `postgres` ロールはロックされた状態となり、直接ログインして使用することができなくなります。これにより、後から `postgres` ロールでの操作が必要になった際に、ログインできない問題が発生する可能性があります。

対処方法：
AlloyDB for PostgreSQLクラスターを作成する際は、セキュリティのベストプラクティスとして、必ず初期ユーザー（`postgres` ロール）のパスワードを明示的に指定してください。これにより、この変更の影響を受けずに、意図した通りのクラスター設定で運用を開始できます。
万が一、パスワード未指定でクラスターを作成してしまい、`postgres` ロールがロックされた状態で作成された場合は、AlloyDBの管理ツール（`gcloud` CLIやGoogle Cloud Console）を使用して、後から新しいユーザーを作成するか、既存のユーザー（`postgres` ロールを含む）のパスワードを設定し直すことを検討してください。

用語説明：
*   **`postgres` role**: PostgreSQLデータベースにおけるスーパーユーザーロールです。データベース内のすべての権限を持ち、データベース管理操作（ユーザー作成、権限付与、データベース設定変更など）を実行できます。セキュリティ上の理由から、このロールは慎重に扱う必要があります。
*   **Locked `postgres` role**: このリリースノートにおける「ロックされた `postgres` ロール」とは、パスワードが設定されていない（`null` パスワード）状態であり、ユーザーがそのロールを使用してデータベースにログインできないように、システムによってアクセスが制限されている状態を指します。直接ログインして使用することができません。
*   **`null` password**: パスワードが設定されていない状態を指します。通常、パスワードが設定されていないユーザーは、特定の認証方法（例: `trust` 認証）が許可されていない限り、ログインすることはできません。この変更により、`postgres` ロールに対して `null` パスワードが設定され、ログインが困難になります。
# Title: April 27, 2026 
Link: https://docs.cloud.google.com/release-notes#April_27_2026<br>
はい、Google Cloudのリリースノートを元に、構築済みのサービスへの影響調査と回答を行います。

---

# API Gateway

## Change

原文:
**New validations on paths in API configurations**

API Gateway now enforces stricter syntax validations on templated paths when you create new API configurations and gateways.

See [path templating syntax rules](https://docs.cloud.google.com/api-gateway/docs/path-templating#syntax_rules) and [limits](https://docs.cloud.google.com/api-gateway/docs/path-templating#limits) for more information.

説明:
API Gatewayにおいて、API構成（API configurations）およびゲートウェイを新規作成または更新する際に、テンプレート化されたパス（templated paths）に対する構文検証がより厳格になりました。これにより、従来のルールでは許可されていた一部のパス定義が、新しいルールでは無効と判断される可能性があります。具体的な構文ルールと制限については、提供された公式ドキュメントを参照する必要があります。

影響有無:
**影響あり**
既存のAPI Gatewayインスタンスがただちに動作停止することはありません。しかし、今後API GatewayのAPI構成やゲートウェイを**新規作成**したり、**既存のものを更新**したりする際に、パスの定義方法が新しい厳格な構文ルールに準拠していない場合、デプロイ時にバリデーションエラーが発生し、設定が適用できなくなる可能性があります。特にワイルドカード（`*`）やパス変数（`{}`）を使用している定義で、これまで許容されていたものが影響を受ける可能性があります。

対処方法:
今後API GatewayのAPI構成やゲートウェイを新規作成・更新する際は、そのパス定義がGoogle Cloudの公式ドキュメントに記載されている[パスのテンプレート化に関する構文ルール](https://docs.cloud.google.com/api-gateway/docs/path-templating#syntax_rules)および[制限](https://docs.cloud.com/api-gateway/docs/path-templating#limits)に準拠していることを確認してください。もし既存のAPI設定で今後変更を予定しているものがある場合は、事前に新しいルールに適合するかどうかを検証し、必要に応じてパス定義を修正することを推奨します。

用語説明:
*   **API Gateway**: Google Cloudが提供する、マイクロサービスやサーバーレスバックエンドへのアクセスを管理、保護、監視するためのフルマネージドサービスです。HTTP(S)エンドポイントを提供し、トラフィックルーティング、認証、レート制限などを一元的に制御します。
*   **API configuration (API構成)**: API GatewayにデプロイされるAPIの定義情報です。通常、OpenAPI Specification (OAS) 形式で記述され、APIのパス、メソッド、バックエンドサービスへのルーティング、認証情報などが含まれます。
*   **Templated paths (テンプレート化されたパス)**: URLパスの一部を変数として定義する機能です。例えば、`/users/{user_id}` の `{user_id}` の部分はテンプレート化されたパス変数であり、これにより `/users/123` や `/users/abc` といった異なる具体的なパスを単一の定義で処理できます。
*   **Syntax validations (構文検証)**: 定義された設定やコードが、特定の言語やシステムが定める文法ルールに従っているかを自動的にチェックするプロセスです。厳格な構文検証は、設定ミスによる予期せぬ動作を防ぎ、システムの安定性を高めます。

---

# Cloud Service Mesh

## Announcement

原文:
Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the regular channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility). To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility).

説明:
Google CloudのマネージドCloud Service Mesh（Traffic Directorを基盤とする実装）のレギュラーチャネルにおいて、`EnvoyFilter` APIの限定的なサポートが開始されました。`EnvoyFilter`は、Envoyプロキシのデータプレーンの動作を細かくカスタマイズ・拡張するための高度な機能であり、例えばローカルでのレートリミットといった独自のポリシーを適用することが可能になります。サポートされるフィールド、拡張機能、および設定方法は、提供されたドキュメントに詳しく記載されています。

影響有無:
**影響なし（機能追加によるポジティブな影響）**
このアナウンスは、既存のサービスの動作に悪影響を与えるものではありません。むしろ、Cloud Service Meshの機能が拡張され、Envoyプロキシの動作をより細かく制御できるようになるため、**機能面でのメリット**があります。既存のデプロイメントが自動的にこの新機能の影響を受けることはなく、既存の構成が変更されることもありません。

対処方法:
**特別な対処は不要**です。
この機能は、データプレーンのより高度な制御を必要とする場合に、任意で利用できるものです。`EnvoyFilter`の利用を検討する場合は、提供された公式ドキュメント([Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility))を熟読し、サポートされるフィールドや制限事項、利用方法を十分に理解した上で、慎重に導入を計画してください。

用語説明:
*   **Cloud Service Mesh**: Google Cloudが提供するフルマネージドのサービスメッシュソリューションです。サービスの検出、トラフィック管理、セキュリティ、オブザーバビリティといった機能を提供し、マイクロサービスアプリケーションの運用を簡素化します。
*   **Traffic Director**: Google Cloudのマネージドサービスメッシュのコントロールプレーンです。EnvoyプロキシやgRPCサービスプロキシに動的に設定を提供し、グローバルなロードバランシング、トラフィックルーティング、ヘルスチェックなどを実現します。
*   **Regular channel (レギュラーチャネル)**: Google Cloud製品のリリースチャネルの一つで、広範な利用と安定性を重視した、一般的に推奨されるバージョンです。
*   **Envoy proxy**: クラウドネイティブアプリケーション向けに設計された高性能なオープンソースのエッジ/サービスプロキシです。サービスメッシュのデータプレーンとして広く採用されており、トラフィックのルーティング、負荷分散、プロトコル変換、セキュリティポリシー適用などを行います。
*   **EnvoyFilter API**: IstioやCloud Service Meshにおいて、Envoyプロキシの動作をカスタムルールで直接変更・拡張するためのAPIリソースです。Envoyの低レベルな設定（リスナー、ルート、クラスタなど）にアクセスし、標準のサービスメッシュ機能では実現できない、よりきめ細かいトラフィック制御やポリシー適用を可能にします。
*   **Data plane extensibility (データプレーンの拡張性)**: サービスメッシュにおいて、実際のデータトラフィックを処理するコンポーネント（Envoyプロキシ）の機能を、ユーザーがカスタムコードや設定によって拡張できる能力を指します。これにより、特定のビジネス要件や高度なネットワーク制御ロジックを組み込むことができます。
*   **Local rate limiting (ローカルレートリミット)**: 特定のサービスインスタンスやプロキシのレベルで、受信するリクエストの数を制限する機能です。これにより、サービスが過負荷になるのを防いだり、悪意のあるトラフィックから保護したりすることが可能です。
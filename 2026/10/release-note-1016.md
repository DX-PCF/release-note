
# Title: October 15, 2026 
Link: https://docs.cloud.google.com/release-notes#October_15_2026<br>
# Compute Engine
## Change
原文: If you try to create an on-demand reservation or increase the number of reserved Compute Engine instances in a reservation when the zone has reached its reservation capacity limit for your requested machine family, then the request fails with a `RESERVATION_CAPACITY_LIMIT_EXCEEDED` error. For more information, see Reservation capacity limit exceeded.

説明：
Compute Engineにおいて、特定のゾーンで要求されたマシンファミリーの予約容量制限に達している状態で、オンデマンド予約の新規作成または既存の予約インスタンス数の増加を試みた場合、リクエストが `RESERVATION_CAPACITY_LIMIT_EXCEEDED` エラーで失敗することが明確にされました。これは、以前から存在していた容量制限に関する挙動をより明確化したものです。

影響有無：
**なし**
この変更は、新しい制限が導入されたわけではなく、既存の容量制限に達した場合に発生するエラー挙動が明確にアナウンスされたものです。既存のサービス運用に直接的な影響はありません。ただし、将来的に予約の作成や更新を行う際に、容量不足でリクエストが失敗した場合にこのエラーコードが返されることを認識しておく必要があります。

対処方法：
直接的な対処は不要です。
将来、予約の作成または更新時に `RESERVATION_CAPACITY_LIMIT_EXCEEDED` エラーが発生した場合は、以下の対処が考えられます。
*   異なるゾーンでの予約を検討する。
*   異なるマシンファミリーでの予約を検討する。
*   容量が解放されるまで待機する。
*   Google Cloudのサポートに連絡して、追加容量の可能性を問い合わせる。
詳細については、[Reservation capacity limit exceeded](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-creation#reservation-capacity-limit-exceeded) のドキュメントを参照してください。

用語説明：
*   **オンデマンド予約 (On-demand Reservation)**: Google Cloud上で特定のVMインスタンス（マシンタイプ、ゾーン、GPUなど）を事前に確保しておく機能です。これにより、VMインスタンスを起動する際に、必要なリソースが確実に利用可能であることを保証します。これは、急なリソース需要や、確実にVMを起動させたい場合に有効です。
*   **予約容量制限 (Reservation capacity limit)**: 特定のGoogle Cloudゾーンにおいて、指定されたマシンファミリーや構成を持つVMインスタンスの予約が可能な総数の上限です。この制限は、Google Cloud全体のインフラ容量に基づいています。
*   **マシンファミリー (Machine family)**: Compute Engineで提供されるVMインスタンスのタイプを分類するグループです。各ファミリーは、特定のワークロードやパフォーマンス特性に最適化されています（例: 汎用性のN2、高CPU性能のC2、メモリ最適化のM2など）。これにより、ユーザーは目的のワークロードに最適なVMタイプを選択できます。
# Title: October 14, 2026 
Link: https://docs.cloud.google.com/release-notes#October_14_2026<br>
# Cloud Load Balancing
## Change
原文: Google-managed public SSL certificates signed by Public Certificate Authority (`pki.goog`) are gradually transitioning from a 90-day validity period to a 45-day validity period to improve security. To align with modern industry-wide security standards and promote shorter certificate lifespans, Google-managed public certificates signed by Public Certificate Authority now rotate more frequently. This proactive rotation enhances the overall security posture of load balancers. Transition requires no manual intervention or configuration changes as Google Cloud automatically manages issuance and renewal for both Certificate Manager and Compute Engine SSL certificates. For more information, see Renew a Google-managed SSL certificate.
説明：Google Cloud管理の公開SSL証明書（`pki.goog`によって署名されたもの）の有効期間が、セキュリティ強化のため段階的に90日から45日に短縮されます。これは、業界全体のセキュリティ基準に合わせ、証明書のライフスパンを短くすることで、ロードバランサー全体のセキュリティ体制を強化することを目的としています。この変更に伴い、Google CloudがCertificate ManagerおよびCompute Engine SSL証明書の発行と更新を自動的に管理するため、ユーザー側での手動による介入や設定変更は一切不要です。
影響有無：影響なし。
理由：Google CloudがSSL証明書の発行と更新を完全に自動管理するため、ユーザー側の手動作業や設定変更は発生しません。証明書の有効期間が短くなることで、セキュリティが向上するというメリットがあります。既存のロードバランサーの機能やパフォーマンスに直接的な悪影響はありません。
対処方法：なし。Google Cloudによって自動的に管理されます。
用語説明：
*   **Google-managed public SSL certificates**: Google Cloudが自動的に発行、更新、管理を行うSSL/TLS証明書。
*   **Public Certificate Authority (`pki.goog`)**: Googleが運営する公開認証局。Google管理の証明書は通常、この認証局によって署名される。
*   **Certificate Manager**: Google Cloudの証明書管理サービス。複数の負荷分散製品やWorkload Identityと統合し、証明書の発行、プロビジョニング、デプロイメント、更新を一元的に管理する。

# Cloud SQL for PostgreSQL
## Issue
原文: When you enable the Knowledge Catalog (formerly Dataplex Universal Catalog) integration on a Cloud SQL for PostgreSQL instance created before April 18, 2026, the integration defaults to once a day instead of near real-time. Near real-time updates upon Knowledge Catalog enablement aren't yet available for all existing instances. A new announcement will be published when this feature becomes available.
説明：2026年4月18日より前に作成されたCloud SQL for PostgreSQLインスタンスでKnowledge Catalog（旧Dataplex Universal Catalog）連携を有効にした場合、連携の更新頻度がニアリアルタイムではなく1日1回になります。既存の全てのインスタンスでは、Knowledge Catalogを有効にした際のニアリアルタイム更新はまだ利用できません。この機能が利用可能になった際には、新たなアナウンスが公開される予定です。
影響有無：軽微な影響あり（もしKnowledge Catalog連携を利用している場合）。
理由：2026年4月18日以前に作成されたCloud SQL for PostgreSQLインスタンスでKnowledge Catalog連携を利用している、または将来的に利用する計画がある場合、データ同期の頻度がニアリアルタイムではなく日次となるため、Knowledge Catalog内のメタデータの鮮度が最大24時間遅れる可能性があります。
対処方法：
*   Cloud SQL for PostgreSQLとKnowledge Catalogの連携を利用しており、ニアリアルタイムなメタデータ更新を必要とする場合、この問題が解消されるまで待つ必要があります。
*   この機能のニアリアルタイム更新が必要な場合は、今後の
# Title: October 13, 2026 
Link: https://docs.cloud.google.com/release-notes#October_13_2026<br>
Cloud SDKのリリースノート調査をご依頼いただきありがとうございます。
ご提示いただいた情報では、`Cloud SDK` の `Breaking` カテゴリであることが示されていますが、具体的なリリースノートの本文が不足しております。

そのため、ここではCloud SDKのBreaking Changeに一般的に想定される影響と対処方法について、回答のフレームワークを提供します。実際のリリースノートが提供された際に、以下のフレームワークに具体的な内容を追記・修正してご活用ください。

---

# Cloud SDK
## Breaking
原文: (※ここに、提供されたCloud SDKのBreaking Changeに関する具体的なリリースノートの原文を記載してください。)

説明：
(※ここに、上記の原文を元に、変更内容を日本語で分かりやすく説明します。)

**【説明の例】**
通常、Cloud SDKのBreaking Changeは、`gcloud` コマンドの構文変更、オプションの削除/変更、デフォルト値の変更、出力フォーマットの変更、または特定のAPI動作の非互換な変更を指します。
例えば、「`gcloud compute instances create` コマンドにおいて、以前はオプションであった `--zone` フラグが必須になった。」や、「`gcloud logging read` コマンドのJSON出力形式が変更され、特定のフィールドのネスト構造が変わった。」、あるいは「古いPythonバージョン（例: Python 2.x）のサポートが完全に終了し、Cloud SDKの特定のバージョン以降ではPython 3.xが必須となった。」といった内容が考えられます。

影響有無：
**【影響有無の判断ポイントと理由の例】**

*   **影響あり（高）:**
    *   社内で利用している自動化スクリプト、CI/CDパイプライン、またはアプリケーションが、当該Breaking Changeの対象となる`gcloud`コマンドやオプション、あるいは出力フォーマットに依存している場合。
    *   特定のPythonバージョンやOS環境でCloud SDKを利用しており、新しいバージョンのSDKがこれらの環境との非互換性を持つ場合。
    *   Google Cloud Composer 2 (Airflow) 環境内で、GCPリソース操作のためにAirflowオペレーターが間接的に`gcloud`コマンドを利用している、またはComposer環境の管理に`gcloud`コマンドが使用されており、そのコマンドの動作に影響がある場合。

    **理由例:** 「社内のCI/CDパイプラインで利用しているデプロイスクリプトが、今回のBreaking Changeで変更される`gcloud functions deploy`コマンドの特定のオプションに依存しており、そのままCloud SDKをアップデートするとデプロイが失敗する可能性があります。特に、弊社で利用しているGoogle Cloud Composer 2 (Airflow 2.7.3) 環境のデプロイや管理スクリプトが影響を受ける可能性があります。」

*   **影響なし（低）:**
    *   当該Breaking Changeが影響する`gcloud`コマンドや機能が、社内で全く利用されていない場合。
    *   Cloud SDKのバージョンアップを定期的に行っており、既に該当の変更に対応済みの環境である場合。

    **理由例:** 「今回のBreaking Changeは、弊社では利用していない特定のリソースタイプ（例: `gcloud alpha container` 系の実験的な機能）に関する変更であり、既存のワークロードへの直接的な影響は確認されません。」

対処方法：
**【具体的な対処方法の例】**

1.  **リリースノートの詳細確認:** まず、Cloud SDKの公式リリースノートを参照し、変更された`gcloud`コマンド、オプション、API、および影響を受けるバージョンについて正確に把握します。
    *   [Cloud SDK リリースノート](https://cloud.google.com/sdk/docs/release-notes)
2.  **利用箇所の特定:** 社内で`gcloud`コマンドを利用している全てのスクリプト、CI/CDパイプライン、開発環境、およびGoogle Cloud Composer 2のような管理対象環境の自動化ジョブなどを洗い出します。
3.  **互換性テスト:**
    *   非本番環境（開発、ステージング）に、リリースノートで示されたバージョンのCloud SDKをインストールし、既存の自動化スクリプトやCI/CDパイプラインを実際に実行して動作検証を行います。
    *   特にGoogle Cloud Composer 2環境の場合、Composer環境の更新やAirflow DAGsからのGCPリソース操作に関連する`gcloud`コマンドの呼び出しが影響を受けないか、十分な検証が必要です。
4.  **スクリプト/コードの修正:** 動作検証で問題が確認された場合は、リリースノートの指示に従い、`gcloud`コマンドの構文やオプション、または出力フォーマットのパースロジックを修正します。
5.  **段階的なバージョンアップ:** 可能であれば、Cloud SDKのバージョンアップを段階的に（開発 -> ステージング -> 本番）適用し、各フェーズで十分なテスト期間を設けます。
6.  **ロールバック計画:** 万が一の不具合に備え、Cloud SDKの旧バージョンに戻す、または影響を受けるシステムのロールバック手順を準備します。
7.  **依存関係の確認:** Pythonの`google-cloud-sdk`パッケージなどを利用している場合、そのパッケージのバージョンも確認し、互換性を担保します。

用語説明：
*   **Cloud SDK:** Google Cloudリソースの管理に使用されるコマンドラインツール、ライブラリ、およびツールセットのコレクションです。主に`gcloud`コマンドラインツールが含まれます。
*   **`gcloud` CLI (Command Line Interface):** Cloud SDKの主要なコマンドラインツールで、Google Cloudの様々なサービスやリソースを管理・操作するために使用されます。
*   **Breaking Change:** ソフトウェアの新しいバージョンにおいて、以前のバージョンとの後方互換性が失われる変更のことです。これにより、以前のバージョンで動作していたコードや設定が、新しいバージョンでは動作しなくなる可能性があります。
*   **CI/CDパイプライン (Continuous Integration/Continuous Delivery Pipeline):** ソフトウェア開発プロセスを自動化するための一連のワークフローです。コードのコミットからテスト、ビルド、デプロイまでを自動で行います。`gcloud`コマンドは、このパイプライン内でGCPリソースのプロビジョニングやデプロイによく利用されます。
*   **Google Cloud Composer 2:** Google Cloud上でマネージドなApache Airflowサービスを提供するプラットフォームです。Airflowは、ワークフローをプログラムによってオーサリング、スケジュール、モニタリングするためのプラットフォームであり、GCPリソースと連携するオペレーター（例: `GoogleCloudStorageOperator`）などを通じて`gcloud`コマンドと間接的に関連する可能性があります。
# Title: October 12, 2026 
Link: https://docs.cloud.google.com/release-notes#October_12_2026<br>
以下は、ご提供いただいたGoogle Cloudリリースノートに基づき、構築済みのサービスへの影響有無を調査し、簡潔にまとめたものです。

---

# Cloud Service Mesh

## Announcement

原文: **1.31.1-asm.16 is now available for in-cluster Cloud Service Mesh.**
You can now download 1.31.1-asm.16 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.31.1 subject to the list of supported features.
[Istio 1.31.1](https://istio.io/latest/news/releases/1.31.x/announcing-1.31/) [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)
The following are not supported:
- `PILOT_NODE_UNTAINT_CONTROLLERS_TAINT_NAME`
- `prefix_rewrite` field in `HTTPRedirect`
- `ALLOW_ANY_DYNAMIC_DNS` in `outboundTrafficPolicy`
- `connectionSettings` in `ProxyConfig`
- `defaultTrafficPolicy` in `MeshConfig`
- `zoneAwareLbSetting` in `DestinationRule` and `MeshConfig`
- `trustDomains` and `notTrustDomains` fields in `source` field of `AuthorizationPolicy`
- `fips-140-3` for the `COMPLIANCE_POLICY`
- `PILOT_ENABLE_REMOTE_CREDENTIALS_CONTROLLER`
- External SDS provider for gateways
- `PILOT_AGENT_MERGE_ENVOY_STATS`
- `prometheus.istio.io/scrape-targets`
- `ENVOY_SECURE_METRICS_PORT` and `ENVOY_SECURE_MERGED_METRICS_PORT`
- `istioctl manifest generate` with `-o/--output`
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.31.1-asm.16 uses Envoy v1.39.3.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
in-cluster Cloud Service Mesh の新しいバージョン 1.31.1-asm.16 がリリースされ、ダウンロードおよび利用が可能になりました。このバージョンはIstio 1.31.1の機能を含んでいますが、記載されている一部の機能はサポート対象外となります。Envoyのバージョンは v1.39.3 を使用しています。

影響有無：
*   **なし（直接的）：** Cloud Service Mesh は明示的なアップグレードが必要なサービスであり、既存のデプロイメントが自動的にこのバージョンに更新されることはありません。
*   **あり（間接的）：** 将来的にこのバージョンへのアップグレードを検討する際、現在利用している機能が新しいバージョンで非サポートとなっていないか確認が必要です。非サポート機能を利用している場合は、機能利用の中止、代替策の検討、またはサポートされる別のバージョンへのアップグレード計画が必要になる可能性があります。

対処方法：
*   現在 1.31.1-asm.16 未満のバージョンを使用している場合、このバージョンへのアップグレードを計画する際には、リリースノートに記載されている非サポート機能のリストを確認し、既存のワークロードでこれらの機能が使用されていないことを検証してください。
*   アップグレード手順の詳細については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) のドキュメントを参照してください。

用語説明：
*   **in-cluster Cloud Service Mesh:** Google Cloud が提供するマネージドサービスメッシュソリューションである Cloud Service Mesh (ASM) のデプロイモードの一つ。ユーザーのGoogle Kubernetes Engine (GKE) クラスタ内にIstioコントロールプレーンをデプロイし、自身で管理する形式を指します。
*   **Istio 1.31.1:** オープンソースのサービスメッシュプラットフォームであるIstioのバージョン1.31.1。Cloud Service Mesh はIstioを基盤としています。
*   **Envoy v1.39.3:** Istioのデータプレーンとして動作する高性能なオープンソースプロキシEnvoyのバージョン。サービス間のトラフィック管理を担います。

---

## Announcement

原文: **1.30.5-asm.8 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.30.5-asm.8 uses Envoy v1.38.7-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)
This release resolves the security vulnerability listed in Security Bulletin GCP-2026-067.
[GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067)

説明：
in-cluster Cloud Service Mesh のバージョン 1.30.5-asm.8 が利用可能になりました。このリリースには、セキュリティ速報 GCP-2026-067 に記載されているセキュリティ脆弱性に対する修正が含まれています。Envoyのバージョンは v1.38.7-dev を使用しています。

影響有無：
*   **あり：** このバージョンには重要なセキュリティ脆弱性の修正が含まれているため、現在 1.30.5-asm.8 より前のバージョンを使用している場合、システムが該当の脆弱性にさらされている可能性があります。セキュリティリスク低減のため、アップグレードが推奨されます。

対処方法：
*   セキュリティ脆弱性への対応のため、現在 1.30.5-asm.8 未満のバージョンを使用している場合は、このバージョンへのアップグレードを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) を参照してください。

用語説明：
*   **GCP-2026-067:** Google Cloudが公開した特定のセキュリティ脆弱性を識別する速報番号。

---

## Fixed

原文: Patch 1.30.5-asm.8 contains the fix for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-18924 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-82474 | Yes | Yes | No | Yes | Medium (8.5) |
| CVE-2026-82209 | Yes | Yes | No | Yes | Medium (8.2) |
| CVE-2026-84782 | Yes | Yes | No | Yes | High (8.2) |
| CVE-2026-96512 | Yes | Yes | No | Yes | Medium (7.8) |
| CVE-2026-80230 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-13608 | Yes | Yes | No | Yes | Medium (7.4) |
| CVE-2026-15534 | Yes | Yes | No | Yes | Medium (5.7) |
| CVE-2026-19487 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2026-35189 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75805 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75806 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-54872 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-77696 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-0799 | Yes | Yes | No | Yes | Medium (0.0) |
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924) ... (他のCVEリンクも同様に続く)

説明：
Cloud Service Mesh のバージョン 1.30.5-asm.8 には、複数のプラットフォーム共通脆弱性識別子 (CVE) に対する修正が含まれています。これらの修正は、Proxy、Control Plane、CNI などのコンポーネントに影響を与え、High Severity の脆弱性（CVE-2026-84782）も含まれています。

影響有無：
*   **あり：** 現在 1.30.5-asm.8 より前のバージョンを使用している場合、リストされたCVEによってシステムが脆弱である可能性があります。特に、High Severity と評価された脆弱性（例: CVE-2026-84782）は、攻撃を受けるリスクが高く、早急な対応が求められます。

対処方法：
*   セキュリティリスクを軽減するため、バージョン 1.30.5-asm.8 へのアップグレードを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) を参照してください。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures):** 公開されている情報セキュリティの脆弱性および暴露を識別するための辞書項目。各CVEには固有の識別子（例: CVE-YYYY-NNNNN）が割り当てられます。
*   **Severity:** 脆弱性の深刻度を示す評価基準。High は深刻な影響をもたらす可能性があり、早急な対処が必要であることを示します。
*   **Proxy:** Istioにおけるサイドカープロキシ（主にEnvoy）を指し、アプリケーションのネットワーク通信を処理します。
*   **Control Plane:** Istioのコントロールプレーン。サービスメッシュの構成とポリシーを管理し、データプレーン（Proxy）に配布します。
*   **CNI (Container Network Interface):** Kubernetesなどのコンテナオーケストレーションシステムで、コンテナのネットワーク接続を設定するためのオープンソース仕様。
*   **Distroless:** アプリケーションとそのランタイム依存関係のみを含む最小限のコンテナベースイメージ。攻撃対象領域を減らし、セキュリティを向上させます。

---

## Announcement

原文: **1.29.8-asm.8 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.29.8-asm.8 uses Envoy v1.37.9-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade)
This release resolves the security vulnerability listed in Security Bulletin GCP-2026-067.
[GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067)

説明：
in-cluster Cloud Service Mesh のバージョン 1.29.8-asm.8 が利用可能になりました。このリリースには、セキュリティ速報 GCP-2026-067 に記載されているセキュリティ脆弱性に対する修正が含まれています。Envoyのバージョンは v1.37.9-dev を使用しています。

影響有無：
*   **あり：** このバージョンには重要なセキュリティ脆弱性の修正が含まれているため、現在 1.29.8-asm.8 より前のバージョンを使用している場合、システムが該当の脆弱性にさらされている可能性があります。セキュリティリスク低減のため、アップグレードが推奨されます。

対処方法：
*   セキュリティ脆弱性への対応のため、現在 1.29.8-asm.8 未満のバージョンを使用している場合は、このバージョンへのアップグレードを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade) を参照してください。

---

## Fixed

原文: Patch 1.29.8-asm.8 contains the fix for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-18924 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-82474 | Yes | Yes | No | Yes | Medium (8.5) |
| CVE-2026-82209 | Yes | Yes | No | Yes | Medium (8.2) |
| CVE-2026-84782 | Yes | Yes | No | Yes | High (8.2) |
| CVE-2026-96512 | Yes | Yes | No | Yes | Medium (7.8) |
| CVE-2026-80230 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-13608 | Yes | Yes | No | Yes | Medium (7.4) |
| CVE-2026-15534 | Yes | Yes | No | Yes | Medium (5.7) |
| CVE-2026-19487 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2026-35189 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75805 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75806 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-54872 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-77696 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-0799 | Yes | Yes | No | Yes | Medium (0.0) |
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924) ... (他のCVEリンクも同様に続く)

説明：
Cloud Service Mesh のバージョン 1.29.8-asm.8 には、複数のプラットフォーム共通脆弱性識別子 (CVE) に対する修正が含まれています。これらの修正は、Proxy、Control Plane、CNI などのコンポーネントに影響を与え、High Severity の脆弱性（CVE-2026-84782）も含まれています。

影響有無：
*   **あり：** 現在 1.29.8-asm.8 より前のバージョンを使用している場合、リストされたCVEによってシステムが脆弱である可能性があります。特に、High Severity と評価された脆弱性（例: CVE-2026-84782）は、攻撃を受けるリスクが高く、早急な対応が求められます。

対処方法：
*   セキュリティリスクを軽減するため、バージョン 1.29.8-asm.8 へのアップグレードを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade) を参照してください。

---

## Announcement

原文: **1.28.10-asm.49 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.10-asm.49 uses Envoy v1.36.10-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)

説明：
in-cluster Cloud Service Mesh のバージョン 1.28.10-asm.49 が利用可能になりました。Envoyのバージョンは v1.36.10-dev を使用しています。

影響有無：
*   **なし（直接的）：** Cloud Service Mesh は明示的なアップグレードが必要なサービスであり、既存のデプロイメントが自動的にこのバージョンに更新されることはありません。

対処方法：
*   現在 1.28.10-asm.49 未満のバージョンを使用しており、このバージョンへのアップグレードを検討する場合は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade) を参照してください。

---

## Fixed

原文: Patch 1.28.10-asm.49 contains the fix for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-18924 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-82474 | Yes | Yes | No | Yes | Medium (8.5) |
| CVE-2026-82209 | Yes | Yes | No | Yes | Medium (8.2) |
| CVE-2026-847
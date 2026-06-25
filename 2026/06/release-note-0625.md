
# Title: June 23, 2026 
Link: https://docs.cloud.google.com/release-notes#June_23_2026<br>
Google Cloudのインフラエンジニアとして、提供されたリリースノートに基づき、構築済みのサービス（特にGoogle Cloud Composer2）への影響有無を調査し、簡潔に回答します。

---

# Cloud SDK
## Change
原文: (情報なし)
説明: Cloud SDKの「Change」カテゴリに関するアナウンスですが、具体的な変更内容がリリースノートに記載されていません。
影響有無: 不明。提供された情報からは具体的な変更内容が特定できないため、利用中のCloud SDK（特にローカル開発環境やCI/CDパイプラインで使用している場合）への影響は判断できません。
対処方法: Cloud SDKのリリースノート全文を参照し、利用しているコマンドやライブラリに影響する変更がないか確認してください。
用語説明:
*   **Cloud SDK**: Google Cloud Platformのサービスをコマンドラインから操作するためのツールセットです。`gcloud`コマンドなどが含まれ、開発者や運用者がクラウドリソースを管理する際に使用します。

---

# Cloud Service Mesh
## Security
原文: **1.29.5-asm.3 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in
GCP-2026-040.
[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.29.5-asm.3 uses Envoy v1.37.5-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)
説明: インクラスター型Cloud Service Meshのバージョン1.29.5-asm.3がリリースされました。このバージョンには、セキュリティ脆弱性GCP-2026-040の修正が含まれています。アップグレード方法に関するドキュメントが提供されています。
影響有無: なし。お客様の環境でインクラスター型Cloud Service Meshを明示的に導入しているとの情報がないため、直接的な影響はありません。Google Cloud ComposerはService Meshを必須とはしていません。
対処方法: なし。もしインクラスター型Cloud Service Meshを導入している場合は、セキュリティ対策として速やかに該当バージョンへのアップグレードを検討してください。
用語説明:
*   **Cloud Service Mesh (ASM)**: Anthos Service Meshの名称が変更されたもので、Google Cloud上でマイクロサービス間のトラフィック管理、セキュリティ、可観測性などを提供するサービスメッシュプラットフォームです。
*   **in-cluster Cloud Service Mesh**: Service MeshのコントロールプレーンをGKEクラスタ内にデプロイし、お客様自身で管理するデプロイモデルです。
*   **GCP-2026-040**: Google Cloudが公開するセキュリティ脆弱性情報の識別子です。

## Fixed
原文: This patch release also contain the fixes for the following CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8) |
| CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1) |
| CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5) |
| CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5) |
| CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9) |
| CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9) |
| CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8) |
| CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0) |
説明: 上記のインクラスター型Cloud Service Meshバージョン1.29.5-asm.3には、複数のCVE（共通脆弱性識別子）に対する修正も含まれています。SeverityがHigh（8.8）のCVE-2026-45447を含む、多数の脆弱性が修正されています。
影響有無: なし。インクラスター型Cloud Service Meshを導入していないため、直接的な影響はありません。
対処方法: なし。もしインクラスター型Cloud Service Meshを導入している場合は、これらの脆弱性修正のため、速やかに該当バージョンへのアップグレードを検討してください。
用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に公開されている情報セキュリティの脆弱性や露出に一意の識別子を付与したリストです。
*   **Severity**: 脆弱性の深刻度を示す指標で、通常CVSS (Common Vulnerability Scoring System) スコアに基づいて評価されます。

## Security
原文: **1.28.9-asm.2 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in
GCP-2026-040.
[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.28.9-asm.2 uses Envoy v1.36.9-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)
説明: インクラスター型Cloud Service Meshのバージョン1.28.9-asm.2がリリースされました。このバージョンにもセキュリティ脆弱性GCP-2026-040の修正が含まれています。
影響有無: なし。インクラスター型Cloud Service Mesh
# Title: June 22, 2026 
Link: https://docs.cloud.google.com/release-notes#June_22_2026<br>
## Apigee X

### Announcement

原文: On June 22nd, 2026, we released an updated version of Apigee (1-17-0-apigee-10).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigeeの新しいバージョン (1-17-0-apigee-10) がリリースされたというアナウンスです。このリリースは本日より展開が開始されており、全てのGoogle Cloudゾーンへの適用が完了するまでに4営業日以上かかる場合があります。この期間中は、お客様のApigeeインスタンスで新しい機能や修正が利用できない可能性があります。

影響有無: 直接的な影響はありません。Apigeeサービス自体はGoogle Cloudによって管理されており、バージョンアップは透過的に適用されます。ただし、新しい機能や修正が反映されるまでに時間がかかる可能性があることを認識しておく必要があります。

対処方法: 特段の対処は不要です。リリースノートに記載されている「Security」および「Fixed」の項目を確認し、具体的な変更内容を把握してください。

### Security

原文:
| Bug ID | Description |
| --- | --- |
| **519996459** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway to patch the following vulnerabilities: - CVE-2026-27143- CVE-2019-14993- CVE-2021-39155- CVE-2021-39156- CVE-2022-23635- CVE-2026-27140- CVE-2026-27144- CVE-2026-29181- CVE-2026-32280- CVE-2026-32281- CVE-2026-32283- CVE-2026-33811- CVE-2026-33814- CVE-2026-34986- CVE-2026-35469- CVE-2026-39820- CVE-2026-39836- CVE-2026-39883- CVE-2026-4046- CVE-2026-42499- CVE-2026-42501- CVE-2026-42504- CVE-2022-31045- CVE-2026-27145- CVE-2026-32282- CVE-2026-32288- CVE-2026-32289- CVE-2026-39350- CVE-2026-39817- CVE-2026-39819- CVE-2026-39823- CVE-2026-39825- CVE-2026-39826- CVE-2026-41413- CVE-2026-42507- CVE-2026-4437- CVE-2026-4438 |
| **N/A** | **Security fix for Apigee infrastructure.** [上記CVEリストと同一]

説明: Apigeeのingress gatewayおよびApigeeのインフラストラクチャにおける多数の共通脆弱性識別子 (CVE) に関連するセキュリティ修正が適用されました。これにより、既知の複数の脆弱性がパッチされ、セキュリティ体制が強化されます。

影響有無: お客様のApigeeインスタンスへの直接的な影響（サービスの停止や設定変更など）はありません。Google Cloudがサービス側で透過的にパッチを適用するため、お客様側での作業は不要です。セキュリティが向上するため、ポジティブな影響となります。

対処方法: 特段の対処は不要です。Apigeeのセキュリティが強化されたことを認識し、引き続き安全にサービスをご利用いただけます。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアの脆弱性に関する公開された識別子。脆弱性ごとに一意の番号が割り当てられ、情報セキュリティコミュニティで共有されます。
*   **Ingress Gateway**: 外部からのトラフィックがサービスメッシュやAPI管理プラットフォームに入る際のエントリポイントとなるコンポーネントです。Apigeeにおいては、外部からのAPIリクエストを受け入れる役割を担います。

### Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **515788622** | Upgraded the default outbound TLS protocol from TLSv1.2 to TLSv1.3 on JVMs that support it. Per-proxy `<SSLInfo><Protocols>` settings continue to take precedence, and the new `HTTPClient.outbound.tls.protocol` override lets operators force a specific protocol. |
| **184266748** | Fixed an issue where ApigeeDatastore TLS certificate creation could fail in namespaces with longer names when the certificate common name exceeded the 64-byte limit. |
| **286069772** | Added a per-gateway `proxyProtocol.mode` property (strict, permissive, disable) on Apigee ingress gateway components to opt in to HAProxy PROXY-protocol parsing. The property defaults to disable. |
| **N/A** | Updates to infrastructure and libraries. |

#### Bug ID: 515788622

説明: デフォルトの送信TLSプロトコルが、TLSv1.3をサポートするJava仮想マシン (JVM) 上でTLSv1.2からTLSv1.3にアップグレードされました。既存のプロキシごとの `<SSLInfo><Protocols>` 設定は引き続き優先され、また、新しい `HTTPClient.outbound.tls.protocol` 設定を使用することで、特定のプロトコルを強制することが可能になりました。

影響有無: ほとんどの場合、影響はありません。TLSv1.3をサポートする宛先への通信は、より新しいプロトコルで自動的に行われ、セキュリティとパフォーマンスが向上します。TLSv1.3に対応していない古いシステムや、TLSv1.2を厳密に要求する特殊なシステムとの通信を行う場合、稀に接続に問題が生じる可能性があります。その場合でも、明示的なプロキシ設定または新しい `HTTPClient.outbound.tls.protocol` を用いてTLSv1.2に戻すことが可能です。

対処方法: 特段の対処は不要です。TLSv1.3への自動アップグレードによって問題が発生した場合（非常に稀）、`HTTPClient.outbound.tls.protocol` を使用してTLSv1.2に固定することを検討してください。

用語説明:
*   **TLSv1.2 / TLSv1.3**: Transport Layer Security（トランスポート層セキュリティ）プロトコルのバージョンです。TLSは、インターネット上の通信を暗号化するための標準的なプロトコルであり、TLSv1.3はTLSv1.2よりも新しいバージョンで、セキュリティとパフォーマンスが強化されています。
*   **JVM (Java Virtual Machine)**: Javaプログラムを実行するための仮想実行環境です。
*   **`HTTPClient.outbound.tls.protocol`**: Apigeeが外部サービスへHTTPリクエストを送信する際に使用するTLSプロトコルを制御するための設定です。

#### Bug ID: 184266748

説明: ApigeeDatastoreのTLS証明書作成が、名前空間の長さが原因で証明書のCommon Name (CN) が64バイトの制限を超過し、失敗することがあった問題が修正されました。

影響有無: 以前この問題に遭遇し、ApigeeDatastoreのTLS証明書作成に失敗していたお客様にとっては、この問題が解消され、ポジティブな影響があります。該当しないお客様には直接的な影響はありません。

対処方法: 特段の対処は不要です。

用語説明:
*   **ApigeeDatastore**: Apigeeが内部的に使用するデータストアです。
*   **TLS証明書**: Secure Sockets Layer/Transport Layer Security (SSL/TLS) プロトコルで使用されるデジタル証明書で、通信の暗号化とサーバの認証に使用されます。
*   **Common Name (CN)**: TLS/SSL証明書の一部であり、証明書が発行されたエンティティ（通常はドメイン名やサーバ名）を識別するために使用されるフィールドです。

#### Bug ID: 286069772

説明: Apigeeのingress gatewayコンポーネントに、ゲートウェイごとの `proxyProtocol.mode` プロパティ（`strict`, `permissive`, `disable`）が追加されました。これにより、HAProxy PROXYプロトコルの解析を有効にできるようになります。このプロパティのデフォルトは `disable` です。

影響有無: 既存の構成には影響ありません。この機能はデフォルトで無効であるため、PROXYプロトコルを使用しない限り、現状の動作に変化はありません。PROXYプロトコルを利用してクライアントのオリジナルIPアドレス情報を適切に転送したい場合に、この設定を有効にすることで利便性が向上します。

対処方法: PROXYプロトコルを使用する必要がある場合、またはHAProxyなどのロードバランサと連携してクライアントのオリジナルIPアドレスをApigeeで利用したい場合は、この `proxyProtocol.mode` を `strict` または `permissive` に設定することを検討してください。

用語説明:
*   **HAProxy PROXYプロトコル**: ロードバランサ（HAProxyなど）がバックエンドサーバに接続する際に、クライアントの実際のIPアドレスや接続情報などのプロトコル情報を伝達するためのプロトコルです。これにより、バックエンドサーバがロードバランサの後ろにいても、クライアントのオリジナル情報を取得できます。
*   **`proxyProtocol.mode`**: HAProxy PROXYプロトコルの動作モードを設定するプロパティです。
    *   `strict`: 厳密なPROXTYプロトコル解析を要求し、無効なヘッダーがあれば接続を切断します。
    *   `permissive`: PROXYプロトコルヘッダーが存在すれば解析しますが、存在しなくても接続を許可します。
    *   `disable`: PROXYプロトコル解析を行いません（デフォルト）。

#### Bug ID: N/A

原文: Updates to infrastructure and libraries.

説明: Apigeeの基盤となるインフラストラクチャおよび使用されているライブラリの一般的な更新が行われました。

影響有無: お客様のApigeeインスタンスへの直接的な影響はありません。通常、これらの更新はサービスの安定性、パフォーマンス、セキュリティの向上を目的としており、Google Cloud側で透過的に適用されます。

対処方法: 特段の対処は不要です。

## Cloud Logging

### Security

原文: If the parent project for a Cloud Storage bucket changes, a log sink stops routing log entries to that bucket. For more information about error messages and recovery options, see Errors routing to Cloud Storage.

説明: Cloud Storageバケットの「親プロジェクト」が変更された場合、そのバケットへログエントリをルーティングしているログシンクが機能しなくなり、ログのルーティングが停止します。詳細なエラーメッセージや復旧オプションについては、公式ドキュメント「Errors routing to Cloud Storage」を参照してください。

影響有無: これは新しい機能追加や変更ではなく、既存のCloud Loggingの挙動に関する重要な注意喚起です。Cloud Storageバケットの親プロジェクトを変更する操作を行う場合、既存のログシンクが意図せず停止する可能性があるため、運用上のリスクとして認識しておく必要があります。

対処方法:
1.  **事前確認**: Cloud Storageバケットの親プロジェクトを変更する前に、そのバケットを送信先としているログシンクが存在しないか、またはそのログシンクの構成に影響がないかを十分に確認してください。
2.  **復旧手順の把握**: もしログシンクが停止した場合は、[Errors routing to Cloud Storage](https://cloud.google.com/logging/docs/export/troubleshoot#errors_exporting_to_cloud_storage) の公式ドキュメントを参照し、エラーメッセージに応じた復旧手順（例: ログシンクの再作成、アクセス許可の更新など）を実行してください。

用語説明:
*   **ログシンク (Log Sink)**: Cloud Logging の機能の一つで、指定した条件に合致するログエントリを、Cloud Storage、BigQuery、Pub/Subなどの別の宛先にエクスポート（ルーティング）するための設定です。
*   **Cloud Storageバケット**: Google Cloud Storage におけるデータの論理的なコンテナです。ログエクスポートの一般的な宛先として使用されます。
*   **親プロジェクト (Parent Project)**: Google Cloudの組織階層において、特定のCloud Storageバケットが属するプロジェクトのことです。リソースのアクセス管理や課金に関連します。
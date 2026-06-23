
# Title: June 22, 2026 
Link: https://docs.cloud.google.com/release-notes#June_22_2026<br>
Google Cloudインフラエンジニアの立場で、提供されたリリースノートを基に、構築済みのサービス（Apigee X および Google Cloud Composer2）への影響調査結果を報告いたします。

---

# Apigee X

## Announcement

原文: On June 22nd, 2026, we released an updated version of Apigee (1-17-0-apigee-10).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
2026年6月22日にApigeeの最新バージョン(1-17-0-apigee-10)がリリースされました。このリリースは全てのGoogle Cloudゾーンに展開されるまでに4営業日以上かかる可能性があり、展開が完了するまで新機能や修正がお客様のインスタンスに適用されない場合があります。

影響有無：
影響あり。Google Cloud側で自動的にアップデートが適用されるため、お客様側での操作は不要です。ただし、このアップデートにはセキュリティフィックスやその他の修正が含まれるため、お客様のApigee環境のセキュリティ態勢が向上します。展開が完了するまでは、一部のインスタンスで新機能や修正が適用されない可能性があります。

対処方法：
お客様側での特別な対処は不要です。Google Cloudによるリリース展開が完了するまでお待ちください。新機能や修正が適用されるタイミングは、環境によって異なる場合があります。

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージドのAPI管理プラットフォームです。APIの設計、公開、セキュリティ、トラフィック管理、分析などを包括的に行い、ビジネスロジックとバックエンドサービス間のインターフェースを効率的に管理します。
*   **Rollout**: ソフトウェアの新しいバージョンや機能が、システム全体に段階的または並行的に展開されるプロセスを指します。これにより、大規模なサービスへの影響を最小限に抑えながらアップデートを進めることができます。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **519996459** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway to patch the following vulnerabilities: - CVE-2026-27143- CVE-2019-14993- CVE-2021-39155- CVE-2021-39156- CVE-2022-23635- CVE-2026-27140- CVE-2026-27144- CVE-2026-29181- CVE-2026-32280- CVE-2026-32281- CVE-2026-32283- CVE-2026-33811- CVE-2026-33814- CVE-2026-34986- CVE-2026-35469- CVE-2026-39820- CVE-2026-39836- CVE-2026-39883- CVE-2026-4046- CVE-2026-42499- CVE-2026-42501- CVE-2026-42504- CVE-2022-31045- CVE-2026-27145- CVE-2026-32282- CVE-2026-32288- CVE-2026-32289- CVE-2026-39350- CVE-2026-39817- CVE-2026-39819- CVE-2026-39823- CVE-2026-39825- CVE-2026-39826- CVE-2026-41413- CVE-2026-42507- CVE-2026-4437- CVE-2026-4438 |
| **N/A** | **Security fix for Apigee infrastructure.** |
- CVE-2026-27143- CVE-2019-14993- CVE-2021-39155- CVE-2021-39156- CVE-2022-23635- CVE-2026-27140- CVE-2026-27144- CVE-2026-29181- CVE-2026-32280- CVE-2026-32281- CVE-2026-32283- CVE-2026-33811- CVE-2026-33814- CVE-2026-34986- CVE-2026-35469- CVE-2026-39820- CVE-2026-39836- CVE-2026-39883- CVE-2026-4046- CVE-2026-42499- CVE-2026-42501- CVE-2026-42504- CVE-2022-31045- CVE-2026-27145- CVE-2026-32282- CVE-2026-32288- CVE-2026-32289- CVE-2026-39350- CVE-2026-39817- CVE-2026-39819- CVE-2026-39823- CVE-2026-39825- CVE-2026-39826- CVE-2026-41413- CVE-2026-42507- CVE-2026-4437- CVE-2026-4438

説明：
Apigeeのイングレスゲートウェイと、それを支える基盤インフラストラクチャに対して、多数のセキュリティ脆弱性（CVEs）の修正が適用されました。これにより、お客様のApigee環境全体のセキュリティ体制が強化されます。

影響有無：
影響あり（ポジティブな影響）。お客様側での直接的な操作は不要ですが、Apigee環境がより安全な状態に保たれます。これにより、潜在的なセキュリティリスクが軽減されます。

対処方法：
お客様側での特別な対処は不要です。Google Cloud側でこれらのセキュリティ修正は自動的に適用されます。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に知られている情報セキュリティ脆弱性とその識別子をまとめたリストです。脆弱性の特定と対処を共通の識別子で行うことで、情報共有とセキュリティ対策を効率化します。
*   **Ingress Gateway**: ネットワークの外部から内部へ入るトラフィックを制御・ルーティングするゲートウェイのことです。Apigeeにおいては、外部からのAPIリクエストを受け付けるエントリポイントとして機能し、セキュリティポリシーの適用やトラフィック管理を行います。

## Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **515788622** | Upgraded the default outbound TLS protocol from TLSv1.2 to TLSv1.3 on JVMs that support it. Per-proxy `<SSLInfo><Protocols>` settings continue to take precedence, and the new `HTTPClient.outbound.tls.protocol` override lets operators force a specific protocol. |

説明：
Apigeeから外部サービス（バックエンド）への通信におけるデフォルトのアウトバウンドTLSプロトコルが、サポートされるJVM上でTLSv1.2からTLSv1.3にアップグレードされました。各プロキシに個別に設定されている`<SSLInfo><Protocols>`設定は引き続き優先され、また、新しく追加された`HTTPClient.outbound.tls.protocol`設定を使用することで、特定のTLSプロトコルを強制することが可能になりました。

影響有無：
影響あり。TLSv1.3へのアップグレードにより、Apigeeから外部サービスへの通信のセキュリティとパフォーマンスが向上します。既存のプロキシで明示的にTLSv1.2が設定されている場合はその設定が優先されるため、動作に変化はありません。バックエンドサービスがTLSv1.3に対応していない場合でも、ネゴシエーションにより下位バージョンが選択されるため、互換性の問題は生じにくいですが、念のためバックエンドシステムのTLS対応状況を確認することを推奨します。

対処方法：
特にTLSプロトコルの設定を明示的に行っていない場合、お客様側での特別な対処は不要です。TLSv1.3の恩恵を自動的に受けられます。特定のTLSプロトコルを強制したい場合や、バックエンドの互換性テストが必要な場合は、新しく追加された`HTTPClient.outbound.tls.protocol`設定を確認し、必要に応じて適用を検討してください。

用語説明：
*   **TLS (Transport Layer Security)**: インターネット上で安全な通信を行うための暗号化プロトコルです。データの盗聴や改ざんを防ぐために使用され、HTTP通信のHTTPS化などで広く利用されています。
*   **TLSv1.2, TLSv1.3**: TLSプロトコルのバージョンです。TLSv1.3は最新かつ最も安全なバージョンであり、ハンドシェイクの高速化や暗号スイートの強化など、パフォーマンスとセキュリティの両面で改善が図られています。
*   **Outbound TLS**: Apigeeがバックエンドサービスなど外部のシステムへ接続を確立する際に使用するTLS接続のことです。APIプロキシが外部のAPIやデータベースにアクセスする際に利用されます。
*   **JVM (Java Virtual Machine)**: Javaで書かれたプログラムを実行するためのソフトウェア環境です。Apigee内部の一部のコンポーネントで利用されています。

---

原文:
| Bug ID | Description |
| --- | --- |
| **184266748** | Fixed an issue where ApigeeDatastore TLS certificate creation could fail in namespaces with longer names when the certificate common name exceeded the 64-byte limit. |

説明：
名前空間（Namespace）が長い場合に、TLS証明書のコモンネーム（Common Name）が64バイトの制限を超過し、ApigeeDatastoreのTLS証明書作成が失敗する問題を修正しました。

影響有無：
影響なし（ポジティブな影響）。特定の長い名前空間を使用している場合に発生していた既知の問題が修正されたため、Apigee環境のプロビジョニングや証明書管理の安定性が向上します。既存の運用には直接的な影響はありません。

対処方法：
お客様側での特別な対処は不要です。これまでこの問題に遭遇していたお客様にとっては、自動的に問題が解決されます。

---

原文:
| Bug ID | Description |
| --- | --- |
| **286069772** | Added a per-gateway `proxyProtocol.mode` property (strict, permissive, disable) on Apigee ingress gateway components to opt in to HAProxy PROXY-protocol parsing. The property defaults to disable. |

説明：
Apigeeイングレスゲートウェイコンポーネントに、ゲートウェイごとに`proxyProtocol.mode`プロパティが追加されました。このプロパティ（`strict`, `permissive`, `disable`のいずれか）を設定することで、HAProxy PROXYプロトコルの解析を有効にできるようになりました。このプロパティのデフォルト値は`disable`です。

影響有無：
影響なし。新しい設定項目が追加されただけで、デフォルト値は`disable`であるため、既存のApigee環境の動作には影響しません。PROXYプロトコルを利用してクライアントのIPアドレス情報を透過的に取得したい場合に、新たな設定オプションが提供されます。

対処方法：
PROXYプロトコルを利用してクライアントの真のIPアドレス情報をApigeeイングレスゲートウェイで適切に取得する必要がある場合、このプロパティを`strict`または`permissive`に設定することを検討してください。利用しない場合は、特に設定変更の必要はありません。

用語説明：
*   **PROXY Protocol**: TCPプロキシ（ロードバランサーなど）が、元のクライアントのIPアドレスやポート番号といった接続情報を、その後の接続先（バックエンドサーバー）に透過的に伝えるためのプロトコルです。これにより、バックエンドサーバーはプロキシ経由の接続であっても、クライアントのオリジナルIPアドレスを認識できます。
*   **HAProxy**: 高可用性、ロードバランシング、TCP/HTTPプロキシ機能を提供する、広く利用されているオープンソースソフトウェアです。

---

原文:
| Bug ID | Description |
| --- | --- |
| **N/A** | Updates to infrastructure and libraries. |

説明：
Apigeeを構成する基盤インフラストラクチャと使用されている各種ライブラリが更新されました。

影響有無：
影響あり（ポジティブな影響）。お客様側での直接的な操作は不要ですが、基盤の安定性、セキュリティ、パフォーマンスが向上する可能性があります。

対処方法：
お客様側での特別な対処は不要です。Google Cloud側で自動的に適用されます。

---

# Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)

今回のリリースノートはApigee Xに関するものであり、Google Cloud Composer2に関する更新情報は含まれておりません。
したがって、本リリースノートによるGoogle Cloud Composer2への直接的な影響はありません。
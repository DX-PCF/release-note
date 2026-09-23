
# Title: September 22, 2026 
Link: https://docs.cloud.google.com/release-notes#September_22_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、構築済みのサービスへの影響有無を調査し、指定されたフォーマットで回答いたします。

---

# Cloud SDK
## Breaking
原文: (情報なし)
説明：Cloud SDKのリリースノートにおいて「Breaking」カテゴリが示されていますが、具体的な変更内容に関する情報が記載されていません。
影響有無：内容が不明なため、現時点での既存システムへの影響は評価できません。
対処方法：今後のリリースノートで詳細情報が公開された際に、内容を確認し、必要に応じて対応を検討する必要があります。
用語説明：なし（具体的な変更内容がないため）

---

# Compute Engine
## Deprecated
原文:
```
As of September 15, 2026, NVIDIA P100 (`nvidia-tesla-p100` and
`nvidia-tesla-p100-vws`) GPUs have reached end of support (EOS) and are shut
down. You can no longer create, launch, or access Compute Engine
instances or other Google Cloud resources that use NVIDIA P100 GPUs.

For information about migrating your workloads to supported GPU alternatives
such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series, see
NVIDIA P100 end of support.

[NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)
```
説明：NVIDIA P100 GPU (`nvidia-tesla-p100` および `nvidia-tesla-p100-vws`) は、2026年9月15日をもってサポート終了 (EOS) となり、シャットダウンされました。この日付以降、NVIDIA P100 GPUを使用するCompute Engineインスタンスやその他のGoogle Cloudリソースの作成、起動、アクセスはできなくなります。ワークロードをG2 (NVIDIA L4) または G4 (NVIDIA RTX PRO 6000) マシンシリーズのようなサポート対象のGPU代替モデルへ移行することが推奨されています。
影響有無：**影響あり**
*   **既存システムへの影響:** 構築済みのシステムで現在NVIDIA P100 GPUを使用している場合、2026年9月15日以降はこれらのリソースにアクセスできなくなっているため、サービス停止または性能低下が発生している可能性があります。
*   **新規構築への影響:** 新規にP100 GPUを使用するインスタンスを作成することはできません。
対処方法：
*   現在P100 GPUを使用しているCompute Engineインスタンス、またはP100 GPUをアタッチしたGKEノードプールやその他のGoogle Cloudリソースがないか、環境全体を緊急に確認してください。
*   P100 GPUを使用している場合は、直ちにサポート対象のGPU（例: G2 (NVIDIA L4) または G4 (NVIDIA RTX PRO 6000) マシンシリーズ）への移行を計画し、実行してください。
*   移行に関する詳細は、[NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos) を参照してください。
用語説明：
*   **End of Support (EOS):** 製品やサービスがベンダーによって公式にサポートされなくなる期限。EOS日以降は、セキュリティアップデート、バグ修正、技術サポートが提供されなくなり、最終的にサービスが利用できなくなる場合があります。
*   **GPU (Graphics Processing Unit):** グラフィックス処理に特化したプロセッサですが、AI/機械学習、HPC（高性能計算）など、大量の並列計算を必要とするワークロードで一般的に利用されます。

## Deprecated
原文:
```
NVIDIA T4 (`nvidia-tesla-t4` and `nvidia-tesla-t4-vws`) and NVIDIA P4
(`nvidia-tesla-p4` and `nvidia-tesla-p4-vws`) GPUs are deprecated and will reach
end of support (EOS) on August 1, 2027. After August 1, 2027, you won't be able
to create, launch, or access Compute Engine instances or other
Google Cloud resources that run NVIDIA T4 or P4 GPUs. In addition, you can no
longer purchase or renew 3-year committed use discounts (CUDs) for NVIDIA T4 or
P4 GPUs.

To transition your workloads to supported GPU models such as the G2 (NVIDIA L4)
or G4 (NVIDIA RTX PRO 6000) machine series before the EOS date, see
NVIDIA T4 end of support and
NVIDIA P4 end of support.

[NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos)
[NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos)
```
説明：NVIDIA T4 GPU (`nvidia-tesla-t4` および `nvidia-tesla-t4-vws`) と NVIDIA P4 GPU (`nvidia-tesla-p4` および `nvidia-tesla-p4-vws`) が非推奨 (deprecated) となり、2027年8月1日にサポート終了 (EOS) となります。この期日以降は、T4またはP4 GPUを使用するCompute Engineインスタンスやその他のGoogle Cloudリソースの作成、起動、アクセスができなくなります。また、NVIDIA T4またはP4 GPUに対する3年間のコミット済み使用割引 (CUDs) の新規購入や更新はできなくなりました。EOS期日までに、ワークロードをサポート対象のGPUモデル（G2 (NVIDIA L4) または G4 (NVIDIA RTX PRO 6000) など）へ移行することが推奨されています。
影響有無：**影響あり (将来的な計画が必要)**
*   **既存システムへの影響:** 現在、構築済みのシステムでNVIDIA T4またはP4 GPUを使用している場合、2027年8月1日以降はこれらのリソースが利用できなくなります。これにより、将来的なサービス停止または性能低下のリスクがあります。
*   **コストへの影響:** 3年間のコミット済み使用割引 (CUD) をT4またはP4 GPUで利用している場合、新規購入や更新ができないため、コスト計画に影響が出る可能性があります。
対処方法：
*   現在T4またはP4 GPUを使用しているCompute Engineインスタンス、またはこれらのGPUをアタッチしたGKEノードプールやその他のGoogle Cloudリソースがないか、環境全体を確認してください。
*   T4またはP4 GPUを使用している場合は、2027年8月1日のEOS期日までにサポート対象のGPU（例: G2 (NVIDIA L4) または G4 (NVIDIA RTX PRO 6000) マシンシリーズ）への移行計画を立て、実行してください。
*   コミット済み使用割引 (CUD) を利用している場合は、次のCUD更新時または契約期間終了までに、T4/P4以外のGPUを選択できるようワークロード移行を検討してください。
*   移行に関する詳細は、[NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) および [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos) を参照してください。
用語説明：
*   **Deprecated (非推奨):** ある機能、製品、またはサービスが、新しい代替機能や改善されたバージョンによって置き換えられ、将来的にサポートが終了する予定であることを示すステータス。既存の機能は引き続き動作するが、新規での利用は推奨されず、代替手段への移行が強く推奨されます。
*   **Committed Use Discounts (CUDs):** Google Cloudリソースを一定期間（1年または3年）にわたって継続的に使用することをコミットすることで適用される割引。これにより、オンデマンド料金よりも大幅に低い料金でリソースを利用できます。

---
# Title: September 21, 2026 
Link: https://docs.cloud.google.com/release-notes#September_21_2026<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響について調査結果を報告いたします。

---

# Apigee X

## Announcement

**原文:**
On September 21st, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-4**, your instance will be updated to **1-18-0-apigee-4** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.
Note: Instances that meet either of the following two criteria will not be updated:
- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.
For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.

**説明:**
2026年9月21日より、メンテナンスウィンドウを設定しているApigeeインスタンスに対するメンテナンスアップデートが開始されました。もしお客様のインスタンスがメンテナンスの推奨ウィンドウを設定しており、かつバージョンが **1-18-0-apigee-4** 未満の場合、今後7日から21日以内に自動的に **1-18-0-apigee-4** へ更新されます。アップグレード予定日に関する通知は、今後2営業日以内に送信されます。
ただし、以下の条件に該当するインスタンスは更新されません。
*   既知の課題 445936920 に記載されているDNS設定の誤りがあるインスタンス。
*   2025年10月16日のApigeeリリースノートに記載されている、既に削除されたApigee Java Libraryを使用しているインスタンス。
詳細については、Apigeeのメンテナンスに関する公式ドキュメントを参照してください。

**影響有無:**
**影響あり。**
お客様が管理するApigeeインスタンスがメンテナンスウィンドウを設定しており、かつ現在のバージョンが **1-18-0-apigee-4** 未満である場合、今回のメンテナンスアップデートによりインスタンスが自動的に指定バージョンへ更新されます。これにより、サービス停止は伴わない計画メンテナンスではありますが、環境のバージョンが変更されるため、機能の動作変更や互換性への影響がないか、事前に確認することが推奨されます。
ただし、前述のDNS設定ミスや削除されたJavaライブラリを使用している場合は更新の対象外となりますが、これらはサービス運用上の問題となるため、別途対応が必要です。

**対処方法:**
1.  **インスタンスバージョンの確認:** 現在ご利用中のApigeeインスタンスのバージョンを確認し、**1-18-0-apigee-4** 未満であるかどうかを特定してください。
2.  **アップグレード通知の確認:** 今後2営業日以内に送信されるアップグレード予定日の通知に注意し、メンテナンスウィンドウが適切に設定されているかを確認してください。
3.  **互換性テストの実施:** 可能であれば、テスト環境にて **1-18-0-apigee-4** へのアップグレードがお客様の既存のAPIプロキシやカスタムロジックに影響を与えないか、互換性テストを実施することを推奨します。
4.  **問題インスタンスの修正:** もしDNS設定ミス (Known Issue 445936920) や削除されたApigee Java Library (Apigee release notes dated October 16, 2025) を使用している場合は、インスタンスが自動更新されないため、速やかにこれらの問題を修正してください。

**用語説明:**
*   **Apigee X**: Google Cloud が提供する、API の設計、セキュリティ、分析、スケーリングを管理するための API 管理プラットフォームです。
*   **メンテナンスウィンドウ (Maintenance Window)**: クラウドサービスプロバイダーが計画的なメンテナンス作業を行うために事前に定義された時間帯です。ユーザーは自身のワークロードへの影響を最小限に抑えるため、メンテナンスが実施される望ましい時間帯を設定できます。
*   **インスタンス (Instance)**: Apigee X サービスが稼働する論理的な実行環境の単位です。
*   **DNS misconfiguration (DNS設定の誤り)**: Domain Name System (DNS) の設定に誤りがある状態を指します。これにより、Apigee インスタンスが正しくネットワーク通信を行えない場合があります。

---

## Announcement

**原文:**
On September 21st, 2026, we released an updated version of Apigee (1-18-0-apigee-5).
> **Note:** Rollouts of this release began today and can take four or more business days to be completed across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

**説明:**
2026年9月21日、Apigee の更新バージョンである **1-18-0-apigee-5** がリリースされました。このリリースのロールアウトは本日より開始されており、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。そのため、お客様のインスタンスで新機能や修正がすぐに利用可能にならない場合があります。

**影響有無:**
**影響なし（直接的な操作は不要）。**
このリリースはApigeeの新しいバージョン展開であり、ユーザー側で直接的な操作は必要ありません。ロールアウトが完了するまで新機能や修正が利用できない可能性がありますが、既存のサービス動作に悪影響を及ぼすものではありません。

**対処方法:**
特段の対処は不要です。ロールアウトが完了し、お客様のインスタンスに新バージョンが適用された後に、必要に応じて新機能の利用や修正点の確認を行ってください。

**用語説明:**
*   **ロールアウト (Rollout)**: ソフトウェアやサービスの新しいバージョンを、段階的または大規模に展開するプロセスを指します。これにより、影響を最小限に抑えつつ、新バージョンへの移行が行われます。

---

## Security

**原文:**
| Bug ID | Description |
|---|---|
| **560130499** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy. |
| **547681234** | **Security fix for Apigee.** Patched CVE-2026-69247 by upgrading a third-party library used by the Apigee model-security engine. |
| **556568593** | **Security fix for Apigee.** Patched CVE-2026-84304 by upgrading gRPC. |
| **N/A** | **Security fix for Apigee infrastructure.** |

**説明:**
Apigee のセキュリティに関する複数の修正が適用されました。具体的には、Java Callout ポリシーにおけるセキュリティ問題の修正、Apigee のモデルセキュリティエンジンで使用されているサードパーティライブラリのアップグレードによる CVE-2026-69247 のパッチ適用、gRPC のアップグレードによる CVE-2026-84304 のパッチ適用、および Apigee インフラストラクチャ全般のセキュリティ修正が含まれます。

**影響有無:**
**良い影響。**
これらのセキュリティ修正は、Apigee サービスの脆弱性を解消し、システム全体のセキュリティを向上させます。お客様の環境に自動的に適用されるため、セキュリティリスクの低減に寄与します。

**対処方法:**
特段の対処は不要です。これらの修正は自動的に適用されるため、お客様側での追加作業は必要ありません。

**用語説明:**
*   **Java Callout policy**: Apigee において、カスタムの Java コードを実行するために使用されるポリシーです。これにより、API プロキシの処理フロー中に複雑なロジックを組み込むことができます。
*   **CVE (Common Vulnerabilities and Exposures)**: 既知のサイバーセキュリティ脆弱性に対して国際的に採番される識別子です。これにより、特定の脆弱性を一意に識別し、情報共有を容易にします。
*   **gRPC**: Google が開発した、高性能でオープンソースのリモートプロシージャコール (RPC) フレームワークです。ネットワーク越しにサービス間で効率的に通信するために使用されます。
*   **Third-party library (サードパーティライブラリ)**: アプリケーションやサービスに機能を追加するために、開発元以外の組織や個人によって作成されたソフトウェアライブラリです。

---

## Fixed

**原文:**
| Bug ID | Description |
|---|---|
| **559009293** | Fixed elevated OAuth and VerifyAPIKey latency and Cassandra read load for AppGroup apps by caching the AppGroup entity in the Message Processor runtime, matching Developer-app behavior. |
| **558888960** | Fixed distributed tracing so that the target URL is included as a span attribute in all scenarios. |
| **556750755** | Fixed EventFlow (Server-Sent Events) dropping or truncating events that follow a large (greater than 16 KB) event under load on the http-adaptor data path. |
| **553931019** | The MCP tools/list method now aggregates tools across all approved API products. |
| **531783017** | Implemented the `<Enforce>true</Enforce>` element of SSLInfo for a Syslog endpoint, so that the syslog target's TLS server identity is verified. |
| **554114419** | Policies can now change request pseudo-headers (for example, :path and :authority) when HTTP/2 is in use. |
| **548763108** | Blocked outbound HTTP from the Message Processor to Kubernetes-internal targets. |
| **513032450** | Restored a 15-second TCP keep-alive on the Apigee Connect control-plane connection so that a silently dropped connection recovers in seconds rather than approximately two hours. |
| **N/A** | Updates to infrastructure and libraries. |

**説明:**
Apigee の複数のバグが修正され、機能性、パフォーマンス、信頼性が向上しました。主な修正点は以下の通りです。
*   AppGroup アプリケーションにおける OAuth および VerifyAPIKey のレイテンシと Cassandra の読み込み負荷が増大する問題が、AppGroup エンティティを Message Processor ランタイムにキャッシュすることで解決されました。
*   分散トレーシングにおいて、ターゲット URL が常にスパン属性として含まれるようになりました。
*   EventFlow (Server-Sent Events) において、http-adaptor データパスの負荷が高い状況で、16KB を超える大きなイベントの後に続くイベントが欠落または切り詰められる問題が修正されました。
*   MCP の `tools/list` メソッドが、すべての承認済み API プロダクトにわたるツールを集約するようになりました。
*   Syslog エンドポイントにおける `SSLInfo` の `<Enforce>true</Enforce>` 要素が実装され、Syslog ターゲットの TLS サーバー ID が検証されるようになりました。
*   HTTP/2 使用時に、ポリシーがリクエストの擬似ヘッダー（例: `:path`, `:authority`）を変更できるようになりました。
*   Message Processor から Kubernetes 内部ターゲットへのアウトバウンド HTTP 通信がブロックされました。
*   Apigee Connect のコントロールプレーン接続における 15 秒の TCP キープアライブが復元され、サイレントな接続切断時の復旧時間が大幅に短縮されました。
*   インフラストラクチャとライブラリの全般的な更新が行われました。

**影響有無:**
**良い影響。**
これらの修正は、Apigee の安定性、パフォーマンス、機能の正確性を向上させます。特に、AppGroup アプリケーションのレイテンシ問題、分散トレーシングの改善、EventFlow の信頼性向上、Syslog のセキュリティ強化、HTTP/2 ヘッダー操作の柔軟性向上、Apigee Connect の接続安定性など、多くの領域で恩恵が期待できます。
ただし、「Message Processor から Kubernetes 内部ターゲットへのアウトバウンド HTTP 通信のブロック」は、セキュリティ強化のためですが、もしお客様のカスタム実装で意図的にこの通信を利用していた場合は、影響がある可能性があります（通常はこのような通信は推奨されません）。

**対処方法:**
特段の対処は不要です。これらの修正は自動的に適用され、改善された機能の恩恵を受けることができます。
ただし、Message Processor から Kubernetes 内部ターゲットへのHTTPアウトバウンド通信を意図的に利用している稀なケースがあった場合、この変更によって通信がブロックされるため、既存のカスタム実装を確認し、必要であれば代替手段を検討してください。

**用語説明:**
*   **OAuth**: Open Authorization の略で、サードパーティアプリケーションがユーザーに代わって特定のサービスにアクセスするための標準プロトコルです。
*   **VerifyAPIKey**: Apigee のポリシーの一つで、API リクエストに含まれる API キーの有効性を検証するために使用されます。
*   **Cassandra**: Apache Cassandra は、高可用性とスケーラビリティに優れた分散型 NoSQL データベースシステムです。
*   **AppGroup**: Apigee におけるアプリケーションのグループ化機能で、複数の開発者アプリケーションを論理的にまとめることができます。
*   **Message Processor**: Apigee ランタイムの主要コンポーネントであり、API リクエストを処理し、Apigee ポリシーを実行する役割を担います。
*   **Distributed Tracing (分散トレーシング)**: マイクロサービスアーキテクチャなどの分散システムにおいて、単一のリクエストが複数のサービス間をどのように伝播するかを追跡し、パフォーマンス問題やエラーの原因を特定するための技術です。
*   **Span attribute (スパン属性)**: 分散トレーシングにおけるトレースの最小単位である「スパン」に関連付けられた追加情報です。例えば、URL、HTTP メソッド、ステータスコードなどが含まれます。
*   **EventFlow (Server-Sent Events, SSE)**: サーバーがクライアントに対してリアルタイムでイベントをプッシュするための Web テクノロジーです。ブラウザがサーバーからの更新を継続的に受け取ることができます。
*   **MCP tools/list method**: Apigee の管理プレーン (Management Plane) で使用されるツールリストを取得するメソッドです。
*   **SSLInfo**: Secure Sockets Layer (SSL、現在の Transport Layer Security: TLS) に関する情報を提供する要素です。
*   **Syslog endpoint**: システムログメッセージを送信する先のサーバーまたはサービスを指します。
*   **TLS server identity (TLSサーバーID)**: TLS 通信において、サーバーが自身を認証するために使用するデジタル証明書と秘密鍵によって確立される識別情報です。
*   **Pseudo-headers (擬似ヘッダー)**: HTTP/2 プロトコルにおける特別なヘッダーフィールドで、通常の HTTP ヘッダーとは異なり、リクエストのパスやオーソリティなど、プロトコルレベルの情報を表します。
*   **Kubernetes-internal targets (Kubernetes内部ターゲット)**: Kubernetes クラスタ内で実行されているサービスや Pod など、クラスタ内部でのみアクセス可能なネットワークエンドポイントを指します。
*   **Apigee Connect**: Apigee と、オンプレミスまたは他のクラウド環境にあるバックエンドサービスとの間に、セキュアな接続を確立するためのコンポーネントです。
*   **TCP keep-alive**: TCP 接続がアクティブであることを定期的に確認するために送信される小さなパケットです。これにより、ネットワークの切断を検出し、アイドル状態の接続がサイレントに終了するのを防ぎます。
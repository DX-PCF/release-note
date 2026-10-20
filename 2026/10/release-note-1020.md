
# Title: October 19, 2026 
Link: https://docs.cloud.google.com/release-notes#October_19_2026<br>
Google Cloud Armorに関するリリースノートの調査結果を報告します。
今回のリリースは、Google Cloud Armorの事前構成済みWAFルールセットのセキュリティ修正と機能強化に関するものです。通常、これらの更新は自動的に適用され、お客様のWAF防御能力を向上させるものですが、稀に誤検知（False Positive）が発生する可能性も考慮し、監視を継続することを推奨します。
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3)は今回のCloud Armorの更新と直接的な関連はありません。しかし、もしComposer環境のAirflow UIやAPIエンドポイントへのアクセスをCloud Armorで保護している場合、間接的に影響を受ける可能性がありますので、注意深く監視してください。

---

# Google Cloud Armor
## Changed (Security)

**原文:**
Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-stable` rulesets. For more information, see Tuning Google Cloud Armor WAF rules. The following rulesets have been updated:
- `sqli-v33-stable`
- `xss-v33-stable`
- `lfi-v33-stable`
- `rfi-v33-stable`
- `rce-v33-stable`
- `methodenforcement-v33-stable`
- `scannerdetection-v33-stable`
- `protocolattack-v33-stable`
- `php-v33-stable`
- `sessionfixation-v33-stable`
- `java-v33-stable`
- `nodejs-v33-stable`

**説明:**
Google Cloud Armorの事前構成済みWAFルールセットのうち、`v33-stable`バージョンにセキュリティ修正と機能強化が適用されました。この更新は、SQLインジェクション（SQLi）、クロスサイトスクリプティング（XSS）、ファイルインクルージョン（LFI/RFI）、リモートコード実行（RCE）など、様々なWeb攻撃に対する防御能力を向上させます。

**影響有無:**
*   **影響なし（ただしセキュリティは向上）**
    Cloud Armorの`v33-stable`ルールセットを利用している場合、バックエンドでこれらのセキュリティ修正と機能強化が自動的に適用されます。これにより、お客様のWebアプリケーションのセキュリティ対策が向上します。既存のWAFポリシー設定を変更する必要はありません。
    ただし、ごく稀に、ルールセットの変更によって正当なトラフィックが誤ってブロックされる（誤検知）可能性もゼロではありません。

**対処方法:**
1.  **監視の推奨:** WAFが有効になっているWebアプリケーションのログやCloud ArmorのWAFログ（拒否されたリクエストのログ）を継続的に監視し、予期せぬトラフィックのブロックや誤検知が発生していないか確認してください。
2.  **誤検知発生時の対応:** もし誤検知が確認された場合、[Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning)のドキュメントを参照し、特定のルールを無効化する、またはサプレッションルールを追加するなどの調整を検討してください。

**用語説明:**
*   **WAF (Web Application Firewall):** WebアプリケーションをSQLインジェクション、クロスサイトスクリプティングなどの様々なサイバー攻撃から保護するためのセキュリティシステムです。
*   **事前構成済みWAFルールセット (Preconfigured WAF rulesets):** Google Cloud Armorが提供する、OWASP ModSecurity Core Rule Set (CRS) に基づいて事前に定義されたWAFルール集です。ユーザーはこれらのルールセットを簡単にセキュリティポリシーに適用できます。
*   **`v33-stable`:** Cloud ArmorのWAFルールセットの特定のバージョンを示します。`stable`は安定版を意味し、`v33`はそのバージョン番号です。
*   **SQLi (SQL Injection):** データベースへの不正なSQLコマンドの挿入によって、データ漏洩や改ざんを行う攻撃手法です。
*   **XSS (Cross-Site Scripting):** Webサイトに悪意のあるスクリプトを埋め込み、訪問者のブラウザで実行させることで、セッションハイジャックなどを行う攻撃手法です。
*   **LFI (Local File Inclusion) / RFI (Remote File Inclusion):** 脆弱なWebアプリケーションを悪用し、サーバー上のローカルファイル（LFI）またはリモートのファイル（RFI）を不正に読み込み、実行させる攻撃手法です。
*   **RCE (Remote Code Execution):** 攻撃者がリモートからターゲットサーバー上で任意のコードを実行する攻撃手法です。

---

# Google Cloud Armor
## Changed (Security)

**原文:**
Security fixes and enhancements to Cloud Armor preconfigured WAF `stable` rulesets for v3.0. For more information, see Tuning Google Cloud Armor WAF rules. The following rulesets have been updated:
- `sqli-stable`
- `xss-stable`
- `lfi-stable`
- `rfi-stable`
- `rce-stable`
- `methodenforcement-stable`
- `scannerdetection-stable`
- `protocolattack-stable`
- `php-stable`
- `sessionfixation-stable`

**説明:**
Google Cloud Armorの事前構成済みWAFルールセットのうち、WAFルールバージョン3.0向けの`stable`ルールセットにセキュリティ修正と機能強化が適用されました。これにより、SQLインジェクション、クロスサイトスクリプティングなどの一般的なWeb攻撃に対する防御が強化されます。

**影響有無:**
*   **影響なし（ただしセキュリティは向上）**
    Cloud ArmorのWAFルールバージョン3.0の`stable`ルールセットを利用している場合、バックエンドでこれらのセキュリティ修正と機能強化が自動的に適用されます。これにより、お客様のWebアプリケーションのセキュリティ対策が向上します。既存のWAFポリシー設定を変更する必要はありません。
    上記`v33-stable`と同様に、ごく稀に、ルールセットの変更によって正当なトラフィックが誤ってブロックされる（誤検知）可能性もゼロではありません。

**対処方法:**
1.  **監視の推奨:** WAFが有効になっているWebアプリケーションのログやCloud ArmorのWAFログ（拒否されたリクエストのログ）を継続的に監視し、予期せぬトラフィックのブロックや誤検知が発生していないか確認してください。
2.  **誤検知発生時の対応:** もし誤検知が確認された場合、[Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning)のドキュメントを参照し、特定のルールを無効化する、またはサプレッションルールを追加するなどの調整を検討してください。

**用語説明:**
*   **WAFルールバージョン3.0:** Cloud ArmorのWAFルールセットには複数のバージョンが存在し、これはその中の一つで、より新しい機能や改善が含まれている可能性があります。
*   **`stable`:** 安定版のルールセットを指します。
*   その他の用語については、上記のGoogle Cloud Armor `v33-stable`ルールセットの項を参照してください。
# Title: October 16, 2026 
Link: https://docs.cloud.google.com/release-notes#October_16_2026<br>
以下のリリースノートについて、製品への影響有無、対処方法、用語説明を含めて回答いたします。

---

# Cloud SQL for PostgreSQL
## Change
原文: Cloud SQL for PostgreSQL now supports enabling Managed Connection Pooling on existing Private Service Connect instances. Previously, Cloud SQL supported enabling Managed Connection Pooling only on new instances using Private Service Connect.
[Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling)
[Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect)
For more information, see Managed Connection Pooling overview and Configure Managed Connection Pooling.
[Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling)
[Configure Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/configure-mcp)

説明：
Cloud SQL for PostgreSQLにおいて、既存のPrivate Service Connect (PSC) を使用するインスタンスでも、Managed Connection Pooling (MCP) を有効にできるようになりました。これまでは、PSCを利用する場合、新規作成するCloud SQLインスタンスでのみMCPの有効化が可能でした。

影響有無：
影響はありません。これは機能追加であり、既存の動作を変更するものではありません。
既存でPrivate Service Connectを利用しているCloud SQL for PostgreSQLインスタンスがあり、これまでMCPを利用したくてもできなかった場合に、MCPの恩恵を受けられるようになるというポジティブな変更です。

対処方法：
特に必須の対処はありません。
もし、既存のPrivate Service Connectを利用しているCloud SQL for PostgreSQLインスタンスの接続効率を改善したい場合、この機能を利用してManaged Connection Poolingの導入を検討できます。

用語説明：
*   **Managed Connection Pooling (MCP)**: Cloud SQLが提供する接続プール機能です。アプリケーションからのデータベース接続数を効率的に管理し、接続のオーバーヘッドを削減することで、アプリケーションのスケーラビリティとパフォーマンスを向上させます。
*   **Private Service Connect (PSC)**: Google CloudのVPCネットワーク内で、サービスプロデューサー（今回の場合はCloud SQL）とサービスコンシューマー（ユーザーのVPC）間でプライベートかつセキュアな接続を確立するためのネットワークサービスです。インターネットを経由せず、IPアドレスの重複なしにサービスへのアクセスを可能にします。

---

# Google Kubernetes Engine
## Change
原文: For GKE Standard CPU node pools, GKE can now upgrade nodes by updating the existing Compute Engine VM in place, instead of deleting the VM and creating a new one. Because the node keeps its underlying VM, it also keeps its compute capacity during the upgrade. This lowers the risk that a node upgrade fails or stalls because resources aren't available.
To enable this type of upgrade, use surge upgrades with the `maxUnavailable` field set to a value greater than 0. For more details about when GKE reuses the same Compute Engine instance, including exceptions, see maxUnavailable: GKE makes an existing node unavailable to recreate it.
[surge upgrades with the `maxUnavailable` field](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#max-unavailable)
[maxUnavailable: GKE makes an existing node unavailable to recreate it](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#max-unavailable)
This change applies to all GKE versions. To opt out, contact Cloud Customer Care.
[Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support)

説明：
GKE StandardクラスタのCPUノードプールにおいて、ノードアップグレード時の挙動が変更されました。これまでは既存のCompute Engine VMを削除し、新しいVMを再作成していましたが、今後は既存のVMをその場で更新（インプレースアップグレード）できるようになりました。
これにより、アップグレード中にノードが基盤となるVMとその計算能力を維持するため、リソース不足によるアップグレードの失敗や停止のリスクが低減されます。
この新しいアップグレード方法は、`maxUnavailable`フィールドを0より大きい値に設定したサージアップグレード戦略を使用している場合に適用されます。この変更はすべてのGKEバージョンに適用されます。

影響有無：
影響がある可能性があります。
現在GKE StandardクラスタのCPUノードプールを利用しており、ノードアップグレード戦略としてサージアップグレード (`maxUnavailable`を0より大きい値に設定) を採用している場合、この新しいインプレースアップグレードの挙動が自動的に適用されます。
これは、アップグレードの安定性と成功率を高めるポジティブな変更と見なされますが、アップグレードの内部動作が変更されるため、注意が必要です。
もしこの新しい挙動を望まない場合は、オプトアウトが必要となります。

対処方法：
1.  **既存のアップグレード戦略の確認**: 現在運用しているGKE StandardクラスタのCPUノードプールで、ノードアップグレード戦略として`maxUnavailable`がどのように設定されているかを確認してください。
2.  **挙動の理解**: `maxUnavailable` > 0 の設定を使用している場合、このインプレースアップグレードの挙動が適用されることを理解し、これによるアップグレードの安定性向上という恩恵を認識してください。
3.  **テストの検討**: 本番環境に適用される前に、可能であればステージング環境などでノードアップグレードの挙動をテストし、想定通りの動作であることを確認することを推奨します。
4.  **オプトアウトの検討（非推奨）**: この新しい挙動が何らかの理由で望ましくない場合（稀なケースと思われます）、Cloud Customer Careに連絡することでオプトアウトすることが可能です。

用語説明：
*   **GKE Standard CPU node pools**: Google Kubernetes Engine (GKE) のStandardクラスタにおいて、CPUリソースを主体とした一般的なワークロードを実行するために構成されたノード（Compute Engine VMインスタンス）のグループです。
*   **Compute Engine VM**: Google Cloudのインフラストラクチャ上で動作する仮想マシンインスタンスのことで、GKEの各ノードの基盤となります。
*   **In-place upgrade**: 既存のシステムやソフトウェアのインスタンスを削除せずに、その場で（同じリソース上で）バージョンアップや変更を適用するアップグレード方式です。GKEの文脈では、ノードの基盤となるCompute Engine VMを再作成することなく、そのVM自体を更新する方式を指します。
*   **Surge upgrades with `maxUnavailable` field**: GKEのノードプールアップグレード戦略の一つで、アップグレード中に一時的に利用できなくなるノードの最大数（`maxUnavailable`）や、一時的に追加で作成されるノードの数（`maxSurge`）を指定することで、アップグレードプロセスを制御します。`maxUnavailable`を0より大きい値に設定すると、アップグレード中に一部のノードを停止させ、その停止したノードの数を指定した値以下に制限しながらアップグレードを進めます。
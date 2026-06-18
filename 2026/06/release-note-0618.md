
# Title: June 16, 2026 
Link: https://docs.cloud.google.com/release-notes#June_16_2026<br>
Google Cloudのリリースノート調査結果を以下に報告いたします。

---

# BigQuery
## Announcement
原文: Table Explorer behavior is moving to the **Reference** panel. This transition will occur in July 2026 or later. For more information, see Table Explorer.
[Table Explorer](https://docs.cloud.google.com/bigquery/docs/table-explorer)

説明: BigQueryのUIにおけるTable Explorerの表示場所が、「Reference」パネルへ変更されるというアナウンスです。この移行は2026年7月以降に実施される予定です。これはGUIのレイアウト変更であり、BigQueryの機能そのものやAPIの動作に影響を与えるものではありません。

影響有無: 影響なし。
この変更はBigQueryのユーザーインターフェース（GUI）のレイアウト変更に関するものであり、現在構築されているデータパイプライン、クエリ、API連携、またはデータ処理のパフォーマンスには一切影響がありません。また、変更時期も2026年7月以降と長期的なアナウンスです。

対処方法: 特段の対処は不要です。将来的にBigQueryのGUIを使用する際に、Table Explorerの場所が変更されることを認識しておけば十分です。

用語説明:
*   **Table Explorer**: BigQueryのコンソール上で、データセット内のテーブルのスキーマや詳細、プレビューなどを確認できる機能です。
*   **Reference panel**: BigQueryコンソール内において、クエリエディタの横などに表示される、ドキュメントや参照情報などが表示される可能性のあるパネルを指します。

---

# Cloud SDK
## Breaking
原文: (情報なし)

説明: Cloud SDKの「Breaking Change」としてリストアップされていますが、詳細な内容が提供されていません。この情報だけでは、どのような変更があり、それが既存の環境にどのような影響を与えるかを判断することはできません。

影響有無: 不明。
詳細情報が提供されていないため、影響の有無を判断できません。一般的な「Breaking Change」は、下位互換性のない変更を指し、APIの変更、コマンドの動作変更、機能の削除などが含まれる可能性があります。これがアプリケーションやスクリプトに影響を与える可能性を秘めています。

対処方法: 現時点では情報不足のため、具体的な対処はできません。このリリースノートの続報や、Cloud SDKの公式ドキュメント、変更履歴などを定期的に確認し、詳細が提供され次第、利用しているCloud SDKのバージョンとの互換性や、スクリプト、CI/CDパイプラインへの影響を評価し、必要に応じて対応を計画してください。

用語説明:
*   **Breaking Change**: ソフトウェア開発において、以前のバージョンとの互換性が失われる変更を指します。これにより、以前のバージョンで動作していたコードや設定が新しいバージョンでは動作しなくなる可能性があります。

---

# Compute Engine
## Change
原文: For resource-based committed use discounts (CUDs), the default value of CUD scope for most Cloud Billing accounts has changed from **Project** to **Billing account**. If the CUD scope is set to **Billing account**, then resource-based CUDs from a commitment are shared across all projects in that account. If the CUD scope is set to **Project**, then resource-based CUDs from a commitment are available to only the project in which you purchased that commitment.
Depending on the Cloud Billing account's creation date and the active commitments in that account, this change applies in the following way:
- **Cloud Billing accounts created on or after June 16, 2026**: The CUD scope is **Billing account** (CUD sharing enabled) by default.
- **Cloud Billing accounts created before June 16, 2026**:
    - If the account has **no active resource-based commitments** on June 16, 2026, then the CUD scope has changed to **Billing account** (CUD sharing enabled).
    - If the account has **any active resource-based commitments** on June 16, 2026, then the CUD scope remains unchanged and Google Cloud continues to use your existing configuration.
For more information, see Share resource-based CUDs across projects.
[Share resource-based CUDs across projects](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#cud-scope-configuration)

説明: リソースベースのコミット済み利用割引（CUDs）のスコープのデフォルト値が、「プロジェクト」から「請求先アカウント」に変更されました。
*   **「請求先アカウント」スコープ**: コミットメントによるCUDが、その請求先アカウントに属するすべてのプロジェクト間で共有され、最も効率的に割引が適用されます。
*   **「プロジェクト」スコープ**: コミットメントによるCUDが、そのコミットメントを購入した特定のプロジェクトでのみ適用されます。

この変更の適用は、請求先アカウントの作成日と、2026年6月16日時点でのアクティブなリソースベースのコミットメントの有無によって異なります。
*   **2026年6月16日以降に作成された請求先アカウント**: デフォルトでCUDスコープが「請求先アカウント」になります（CUD共有が有効）。
*   **2026年6月16日以前に作成された請求先アカウント**:
    *   2026年6月16日時点でアクティブなリソースベースのコミットメントがない場合: CUDスコープは「請求先アカウント」に変更されます（CUD共有が有効）。
    *   2026年6月16日時点でアクティブなリソースベースのコミットメントがある場合: 既存の設定が維持され、自動的に変更されません。

影響有無: 料金体系に影響あり。既存のワークロードやサービス動作には影響なし。
この変更は、Compute Engineの課金におけるCUDの適用方法のデフォルト設定に関するものです。
*   **コスト最適化の観点**: ほとんどの組織では、CUDを請求先アカウントレベルで共有することで、利用率を高め、全体的なコスト削減を最大化できるため、今回のデフォルト変更は望ましい方向性です。
*   **既存アカウントへの影響**: 既存の請求先アカウントにアクティブなリソースベースCUDが存在する場合、この変更は自動適用されず、現在の設定（プロジェクトスコープまたは請求先アカウントスコープ）が維持されます。したがって、既存のコスト管理に意図しない変更が生じることはありません。
*   **新規アカウントや新規コミットメントへの影響**: 今後、新しい請求先アカウントを作成する場合や、既存アカウントで新たにリソースベースのコミットメントを購入する際に、CUDがデフォルトで請求先アカウント全体で共有されるようになります。これにより、個々のプロジェクトでの利用率に関わらず、割引が適用されやすくなります。
*   **コストアロケーションの観点**: 請求先アカウント全体でCUDが共有される場合、個々のプロジェクトのコストレポートにおいて、割引がどのように配分されているかを理解することが重要になります。

対処方法:
1.  **既存のCUDの確認**: 現在利用している請求先アカウントにアクティブなリソースベースのCUDがあるかを確認し、そのCUDスコープ設定（プロジェクトまたは請求先アカウント）を把握してください。
2.  **CUD共有の検討**: アクティブなCUDがあり、スコープが「プロジェクト」に設定されている場合、請求先アカウント全体でのCUD共有によるコスト削減のメリットを享受するために、手動でCUDスコープを「請求先アカウント」に変更することを検討してください。これはGoogle Cloudコンソールから設定可能です。
3.  **新規コミットメントの認識**: 今後、リソースベースのコミットメントを購入する際は、デフォルトでCUDが請求先アカウント全体で共有されるようになることを認識し、自社のコスト管理ポリシー（例: 部門ごとの厳密なコスト配分）と照らし合わせて、必要であればスコープを「プロジェクト」に明示的に設定する可能性を考慮してください。
4.  **コストレポートの確認**: CUD共有を有効にした場合、Google Cloudの請求レポートで割引の適用状況を確認し、コスト配分の状況を定期的に監視してください。

用語説明:
*   **Committed Use Discounts (CUDs)**: Google Cloudのサービス（Compute Engineなど）を一定期間（1年または3年）利用することをコミットすることで、通常料金よりも大幅な割引を受けられる仕組みです。
*   **リソースベースCUD**: 仮想マシンインスタンスのCPUやメモリなど、特定のコンピューティングリソースの使用量に対して適用されるCUDです。
*   **CUDスコープ**: CUDがどの範囲で適用されるかを定義する設定です。「プロジェクト」スコープは特定のプロジェクトに、「請求先アカウント」スコープは関連するすべてのプロジェクトに適用されます。
*   **請求先アカウント (Cloud Billing account)**: Google Cloudの利用料金を管理する最上位のエンティティです。複数のプロジェクトが1つの請求先アカウントに関連付けられることがあります。
*   **コスト最適化**: クラウドサービス利用費を効率的に管理し、無駄を排除して総所有コスト（TCO）を削減するプロセスです。
# Title: June 15, 2026 
Link: https://docs.cloud.google.com/release-notes#June_15_2026<br>
はい、承知いたしました。Google Cloudのインフラエンジニアとして、ご提示のBigQueryに関するリリースノートについて、影響調査と回答を以下にまとめました。

---

# BigQuery

## Issue

**原文:**
Support for configuring daily token quotas for BigQuery generative AI functions has been temporarily disabled. We are working to restore this feature as soon as possible.

**説明:**
BigQueryの生成AI関数で使用される日次トークンクォータ（1日あたりのトークン利用上限）を設定する機能が一時的に無効化されました。Google Cloudチームは、この機能をできるだけ早く復旧させるために取り組んでいます。

**影響有無:**
**影響あり（条件付き）**

*   **影響を受ける場合:** BigQueryの生成AI関数を利用しており、その日次トークンクォータを新規に設定しようとしている場合、または既存のクォータ設定を変更しようとしている場合に影響があります。一時的にこれらの設定操作ができなくなります。
*   **直接的な影響を受けない場合:** 現在BigQueryの生成AI関数を利用していない、または日次トークンクォータの設定・変更を計画していない場合は、直接的な影響はありません。ただし、クォータ設定が無効化されている間は、意図しない利用量の増加（およびそれに伴う費用増加）のリスク管理が難しくなる可能性があります。
    *   既存のクォータ設定が適用されなくなるのか、それとも単に「設定機能」が停止しているだけで既存設定は有効なのかは明記されていませんが、設定「機能」の停止と解釈するのが一般的です。

**対処方法:**
1.  **機能復旧の監視:** この機能の復旧に関するGoogle Cloudからのアナウンスを継続的に監視してください。
2.  **利用量の監視:** 日次トークンクォータの設定・変更ができない間は、BigQuery生成AI関数の利用量（特に`INFORMATION_SCHEMA` や Cloud Monitoring を使用したトークン消費量）を通常よりも密に監視し、予期せぬ利用量の急増に注意してください。
3.  **計画の調整:** もし日次トークンクォータの新規設定や変更を予定していた場合は、この機能が復旧するまで計画を一時的に延期してください。

**用語説明:**

*   **BigQuery generative AI functions (BigQuery 生成AI関数):** BigQuery上でSQLクエリから直接、Vertex AIの基盤モデル（例: Gemini, PaLM 2など）の生成AI機能（テキスト生成、要約、分類、感情分析など）を利用するための組み込み関数群です。`ML.GENERATE_TEXT` などの関数がこれに該当します。
*   **Token (トークン):** 生成AIモデルがテキストを処理する際の最小単位です。単語、文字の一部、句読点などがトークンとして数えられ、モデルの入力と出力の量を示す指標として使われます。生成AI機能の利用料金やリソースクォータは、このトークン数に基づいて計算されるのが一般的です。
*   **Daily token quotas (日次トークンクォータ):** BigQueryの生成AI関数の利用において、1日あたりに消費できるトークン数の上限を指します。これにより、想定外のコスト発生やリソースの過剰消費を防ぐために利用量を制御します。
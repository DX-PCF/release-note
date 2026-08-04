
# Title: August 03, 2026 
Link: https://docs.cloud.google.com/release-notes#August_03_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、各製品の変更点について、影響調査と回答を行います。

---

# BigQuery

## Announcement

原文: `Support for hybrid search (using the `VECTOR_SEARCH` function to combine a semantic search with a lexical (keyword) search) has been restored. Using `HYBRID` mode in the `AI.SEARCH` function has also been restored.`

説明: BigQueryにおいて、`VECTOR_SEARCH` 関数を使用してセマンティック検索とレキシカル（キーワード）検索を組み合わせる「ハイブリッド検索」のサポートが復元されました。また、`AI.SEARCH` 関数における `HYBRID` モードの利用も復元されています。この機能は以前一時的に利用不可となっていましたが、今回の発表で再度利用可能になったことが示されています。

影響有無: 影響は**軽微**です。
*   この変更は、特定の機能が一時停止状態から再開されたというアナウンスであり、既存のワークロードに破壊的な変更をもたらすものではありません。
*   BigQueryでベクトル検索やセマンティック検索を検討している、または過去にこの機能の停止によりワークロードが影響を受けていた場合は、機能の再開によりメリットを享受できます。
*   現状この機能を利用していない場合は、直接的な影響はありません。

対処方法: 特に対処は**不要**です。
*   ハイブリッド検索や `AI.SEARCH` 関数の `HYBRID` モードを利用したい場合は、BigQueryの公式ドキュメントを参照し、これらの機能を活用することが可能です。

用語説明:
*   **ハイブリッド検索**: セマンティック検索（意味や文脈に基づく検索）とレキシカル検索（キーワードの出現に基づく検索）を組み合わせることで、検索結果の関連性と網羅性を向上させる検索手法です。
*   **セマンティック検索**: クエリの意図や内容を理解し、意味的に関連性の高い結果を返す検索方法です。ベクトル埋め込み（embedding vector）と類似性検索が用いられることが多いです。
*   **レキシカル検索（キーワード検索）**: 入力されたキーワードとテキストデータ内の単語の一致に基づいて結果を返す検索方法です。
*   **`VECTOR_SEARCH` 関数**: BigQuery MLで提供される、埋め込みベクトル間の類似度に基づいてデータを検索するための関数です。
*   **`AI.SEARCH` 関数**: BigQuery MLの機能の一部で、検索機能を含め、さまざまなAI関連タスクをサポートするための関数群です。`HYBRID` モードはその検索オプションの一つです。

---

# Cloud SQL for PostgreSQL

## Change

原文: `You can change the backup plan for your Cloud SQL enhanced backups without first removing the existing plan. For more information, see Change your instance's associated backup plan. [Cloud SQL enhanced backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups) [Change your instance's associated backup plan](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups#change-plan)`

説明: Cloud SQL for PostgreSQLの拡張バックアップにおいて、既存のバックアッププランを一度削除することなく、直接新しいバックアッププランに変更できるようになりました。以前はバックアッププランを変更する際、既存のプランを削除してから新しいプランを設定する必要がありましたが、この操作が簡素化されました。

影響有無: 影響は**軽微**です。
*   Cloud SQL for PostgreSQLの拡張バックアップ機能を利用しているユーザーにとって、バックアッププランの変更操作がよりスムーズになります。これは利便性の向上であり、既存のシステム運用に直接的な悪影響はありません。
*   既存のワークロードや設定に自動的に変更が適用されるものではなく、手動でバックアッププランを変更する際のユーザーエクスペリエンスが改善されるだけです。

対処方法: 特に対処は**不要**です。
*   今後、Cloud SQL for PostgreSQLインスタンスの拡張バックアッププランを変更する必要が生じた際、この新しい簡素化された手順を利用することができます。
*   具体的な変更手順については、提供されたリンク（[Change your instance's associated backup plan](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups#change-plan)）を参照してください。

用語説明:
*   **Cloud SQL enhanced backups（Cloud SQL 拡張バックアップ）**: Cloud SQLが提供する高度なバックアップ機能で、従来の自動バックアップに加えて、より柔軟なバックアップスケジュール、長期間の保持ポリシー、ポイントインタイムリカバリ（PITR）などをサポートします。
*   **バックアッププラン**: Cloud SQLインスタンスのバックアップ設定を定義するポリシーの集合体です。これには、バックアップの頻度、保持期間、データが保存されるリージョンなどが含まれます。
*   **ポイントインタイムリカバリ（PITR）**: 特定の時点（秒単位）までデータベースを復元できる機能です。これは、トランザクションログ（WALファイル）と完全バックアップを組み合わせて実現されます。
# Title: July 31, 2026 
Link: https://docs.cloud.google.com/release-notes#July_31_2026<br>
# Cloud SQL for PostgreSQL
## Change
原文: Starting on August 1, 2026, when you create or clone a Cloud SQL instance enabled with Private Service Connect, or when you enable Private Service Connect for an existing instance, then connection reconciliation behavior is enabled by default and can't be disabled.

[connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation)
When you remove a project from the list of allowed projects, all existing Private Service Connect connections from the removed project are immediately closed (reconciled). This means that applications using Private Service Connect endpoints in those removed projects can't continue to connect to the Cloud SQL instance using those endpoints.

For more information, see Allowed Private Service Connect projects.

[Allowed Private Service Connect projects](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#allowed-psc-projects)

説明：
2026年8月1日以降、Private Service Connect (PSC) を有効化したCloud SQLインスタンスを新規作成、クローン、または既存インスタンスでPSCを有効化する際に、「connection reconciliation (接続調整)」の動作がデフォルトで有効になり、無効化できなくなります。

「connection reconciliation」とは、Cloud SQLへのPrivate Service Connect接続を許可しているプロジェクトのリストから特定のプロジェクトを削除した場合、その削除されたプロジェクトからの既存のPSC接続が即座に切断される（調整される）機能です。これにより、削除されたプロジェクト内のアプリケーションは、Cloud SQLインスタンスへの接続を継続できなくなります。

影響有無：
影響は限定的であり、多くの場合セキュリティ強化としてポジティブな変更です。
*   **対象**: Cloud SQL for PostgreSQLでPrivate Service Connectを利用している、または将来利用を検討しているユーザー。
*   **適用時期**: 2026年8月1日以降の新規作成、クローン、または既存インスタンスでのPSC有効化時に適用されます。
*   **影響内容**:
    *   現在PSCを利用している、または将来利用する予定がある場合、許可プロジェクトリストからプロジェクトを削除した際に、該当プロジェクトからのCloud SQLへのPSC接続が即座に切断される挙動が強制されます。
    *   これはセキュリティのベストプラクティスに沿ったものであり、不要なアクセスが継続することを防ぐため、通常は望ましい挙動です。
    *   もし、許可プロジェクトからプロジェクトを削除した後も一時的に接続を維持したいといった特殊なユースケースがある場合は、その運用に影響が出る可能性があります。しかし、一般的な運用においては、アクセス権がなくなった時点で接続が切断される方がセキュリティ上好ましいとされます。

対処方法：
*   **緊急の対処は不要です**。変更が適用されるのは2026年8月1日以降であり、時間的猶予があります。
*   **将来の考慮**:
    *   2026年8月1日以降にCloud SQL for PostgreSQLでPSCを利用するインスタンスを新規作成、クローン、またはPSCを有効化する場合、この「connection reconciliation」の挙動がデフォルトであり、無効化できないことを認識してシステム設計を行う必要があります。
    *   もし、現在または将来的に、許可プロジェクトから削除した後も接続を維持する必要があるような非常に特殊なユースケースが存在する場合、2026年8月1日までにその運用を見直し、代替の接続方法やセキュリティポリシーの調整を検討してください。

用語説明：
*   **Private Service Connect (PSC)**: Google Cloudのサービスプロデューサー（この場合はCloud SQL）が、サービスコンシューマー（ユーザーのVPCネットワーク）に対して、限定公開IPアドレスを使用して安全にサービスを提供できるネットワーク接続方法です。これにより、トラフィックはGoogleのネットワーク内にとどまり、インターネットを経由せずに接続できます。
*   **Connection Reconciliation (接続調整)**: Private Service Connectにおいて、サービスプロデューサー（Cloud SQL）側で設定された許可プロジェクトリストから特定のプロジェクトが削除された際に、その削除されたプロジェクトからの既存のサービス接続を自動的かつ即座に切断するプロセスを指します。これにより、不要になったアクセス経路が確実に閉じられ、セキュリティが強化されます。
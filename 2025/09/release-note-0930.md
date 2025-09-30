
# Title: September 29, 2025 
Link: https://cloud.google.com/release-notes#September_29_2025<br>
# BigQuery
## Announcement
原文: History-based query optimizations are now enabled by default. If history-based optimizations have been previously disabled, you can re-enable history-based optimizations for your project or organization.
[History-based query optimizations](https://cloud.google.com/bigquery/docs/history-based-optimizations)
[re-enable history-based optimizations](https://cloud.google.com/bigquery/docs/history-based-optimizations#enable-history-based-optimization)

説明：
BigQueryの履歴ベースのクエリ最適化機能が、全てのプロジェクトおよび組織でデフォルトで有効になりました。この機能は、過去のクエリ実行履歴に基づいて、BigQueryがより効率的な実行プランを生成するのに役立ちます。もし以前にこの最適化機能を明示的に無効にしていた場合でも、必要に応じてプロジェクトまたは組織レベルで再度有効にすることができます。

影響有無：
既存のBigQueryワークロードに対し、**ポジティブな影響が期待されます**。
この機能のデフォルト有効化により、多くのクエリで自動的にパフォーマンスが向上する可能性があります。以前にこの機能を明示的に無効にしていた場合、その設定は維持されると解釈され、既存の運用に直接的な負の影響はありません。ただし、新規にプロジェクトを作成する場合や、明示的に設定していなかったプロジェクトでは、デフォルトで有効になることでクエリ性能の向上が期待されます。

対処方法：
基本的な対処は不要です。ほとんどのBigQueryユーザーは、この変更によりクエリパフォーマンスの向上が期待できるため、積極的に何かをする必要はありません。
*   **パフォーマンスのモニタリング:** クエリの実行時間やスロット消費量などのパフォーマンス指標を継続的にモニタリングし、変更による影響（特にポジティブな変化）を確認することをお勧めします。
*   **特定の状況下での考慮:**
    *   もし、ごく稀にこの最適化が特定の複雑なクエリパターンで予期しないパフォーマンス低下を引き起こす場合は、[ドキュメント](https://cloud.google.com/bigquery/docs/history-based-optimizations#disable-history-based-optimization)を参照して、プロジェクトまたは組織レベルでこの機能を無効にすることを検討してください。
    *   以前にこの機能を明示的に無効にしていた場合、その設定は維持されるため、特に何もする必要はありません。もしこの最適化によるメリットを享受したい場合は、[ドキュメント](https://cloud.google.com/bigquery/docs/history-based-optimizations#enable-history-based-optimization)に従って再度有効にすることができます。

用語説明：
*   **履歴ベースのクエリ最適化 (History-based query optimizations):** BigQueryが過去に実行されたクエリの統計情報や実行プランの履歴（例：データへのアクセスパターン、フィルタリングの選択性、ジョインの種類、パーティショニング情報など）を利用して、現在実行しようとしているクエリの実行プランを動的に最適化する機能です。これにより、より効率的なデータ処理パスが選択され、クエリの実行時間短縮、リソース消費量の削減、および全体的なクエリパフォーマンスの向上が期待されます。
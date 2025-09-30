
# Title: September 29, 2025 
Link: https://cloud.google.com/release-notes#September_29_2025<br>
# AlloyDB for PostgreSQL
## Announcement
原文: The `alloydb_scann` extension version `0.1.3` is updated to include the following vector search improvements in (Preview):

- You can now automatically create ScaNN indexes that are optimized for search performance or for a balance between index build times and search performance with the auto index feature.
- AlloyDB AI's adaptive filtering for filtered vector searches now dynamically switches between pre-filtering and inline filtering. This enhancement further optimizes query performance by allowing the query optimizer to dynamically choose the most efficient filtering strategy. For more information, see Activate adaptive filtering in AlloyDB AI.
- AlloyDB AI now integrates ScaNN indexes with the columnar engine. You can now accelerate your vector similarity search by loading ScaNN indexes into the columnar engine.
- The `alloydb_scann` extension now provides a satisfy limit feature that improves query recall for vector searches. If a search returns fewer results than specified in the `LIMIT` clause, the scan continues until the `LIMIT` is met or a configured upper bound is reached. To enable this feature, set the `scann.satisfy_limit` flag to `relaxed order`. You can also use the `scann.max_pct_leaves_to_search` flag to configure the upper bound for the search.
- You can enable vector search index recommendations for Scalable Nearest Neighbors (ScaNN) indexes using the AlloyDB index advisor. For more information, see Use the AlloyDB index advisor with query insights or View the index advisor's index recommendations.
- You can configure automatic index maintenance using the following flags:
    - `scann.max_background_workers` flag to control the number of background workers and increase throughput across multiple indexes.
    - `scann.maintenance_background_naptime_s` flag to control the minimum delay between maintenance runs.

説明: AlloyDB for PostgreSQLの`alloydb_scann`拡張機能がバージョン`0.1.3`に更新され、プレビュー版のベクター検索機能に以下の複数の改善が追加されました。

*   **自動インデックス作成**: 検索パフォーマンスに最適化された、またはインデックス構築時間と検索パフォーマンスのバランスが取れたScaNNインデックスを自動で作成できるようになりました。
*   **適応型フィルタリング**: フィルタリングされたベクター検索において、クエリ最適化のためにプリフィルタリングとインラインフィルタリングを動的に切り替えるようになりました。
*   **カラムナエンジンとの統合**: ScaNNインデックスをカラムナエンジンにロードすることで、ベクター類似性検索を高速化できるようになりました。
*   **`satisfy_limit` 機能**: `LIMIT`句で指定された結果数に満たない場合に、スキャンを継続して結果を補完する機能が追加されました。`scann.satisfy_limit`フラグで設定可能です。
*   **インデックスアドバイザーとの統合**: AlloyDBインデックスアドバイザーがScaNNインデックスの推奨をサポートするようになりました。
*   **自動インデックスメンテナンス**: `scann.max_background_workers`および`scann.maintenance_background_naptime_s`フラグを使用して、自動インデックスメンテナンスを設定できるようになりました。

影響有無: **影響なし (既存利用者にとってはパフォーマンス向上や機能拡張の恩恵)**
理由: これらの機能は、AlloyDB AIのベクター検索機能に対する強化であり、すべてプレビュー段階の機能追加です。既存のワークロードに非互換性のある変更（Breaking Change）をもたらすものではなく、`alloydb_scann`拡張機能を利用しているユーザーは、これらの新機能を活用することでパフォーマンス向上や管理効率化の恩恵を受けることができます。

対処方法:
*   これらの新機能はプレビュー版であり、利用を検討する場合は公式ドキュメントを参照し、テスト環境での評価を推奨します。
*   自動インデックス作成や自動インデックスメンテナンス機能を有効にする場合は、システムの負荷やリソース消費への影響を事前に確認してください。
*   `alloydb_scann`拡張機能のバージョンアップは、通常、AlloyDBのメンテナンスサイクルで自動的に適用されるか、手動での更新オプションが提供されます。ご利用中のAlloyDBインスタンスのバージョンアップポリシーを確認してください。

用語説明:
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、フルマネージドでエンタープライズ向けのPostgreSQL互換データベースサービス。
*   **`alloydb_scann` 拡張機能**: AlloyDBでスケーラブルな近似最近傍探索（Scalable Nearest Neighbors: ScaNN）を可能にするPostgreSQL拡張機能。ベクター類似性検索に利用されます。
*   **ベクター検索 (Vector Search)**: テキスト、画像、音声などの非構造化データを数値ベクトルに変換し、ベクトル間の類似度に基づいて検索を行う技術。AI/MLアプリケーションで活用されます。
*   **ScaNN (Scalable Nearest Neighbors)**: Googleによって開発された、大規模なデータセットから高速かつ効率的に最近傍ベクトルを検索するアルゴリズム。
*   **プレビュー (Preview)**: 一般提供（GA）前の機能で、テストやフィードバック収集のために早期に公開されます。機能やAPIが変更される可能性があります。
*   **カラムナエンジン (Columnar Engine)**: データを列指向で格納・処理するエンジン。分析クエリにおいて高いパフォーマンスを発揮します。AlloyDBでは分析ワークロードの高速化に寄与します。
*   **適応型フィルタリング (Adaptive Filtering)**: クエリ最適化の一種で、特定の条件（フィルタ）を持つベクター検索において、そのフィルタを事前に適用するか（プリフィルタリング）、検索中に適用するか（インラインフィルタリング）を動的に判断し、最も効率的な戦略を選択する機能です。
*   **インデックスアドバイザー (Index Advisor)**: データベースのクエリパフォーマンスを改善するために、新しいインデックスの作成や既存インデックスの変更・削除を推奨するツール。

---

# BigQuery
## Announcement
原文: History-based query optimizations are now enabled by default. If history-based optimizations have been previously disabled, you can re-enable history-based optimizations for your project or organization.

説明: BigQueryにおいて、履歴ベースのクエリ最適化がデフォルトで有効になりました。以前にこの機能を無効にしていた場合でも、プロジェクトまたは組織レベルで再度有効にすることができます。

影響有無: **影響なし (既存利用者にとってはパフォーマンス向上の恩恵)**
理由: この変更は、BigQueryのクエリパフォーマンスを向上させるための内部的な最適化機能がデフォルトで有効になったというものです。ユーザーが明示的にこの機能を無効にしていなければ、既存のクエリは自動的にこの最適化の恩恵を受け、パフォーマンスが向上する可能性があります。無効にしていた場合でも、再有効化のオプションが提供されているため、既存のワークロードに非互換性や問題を引き起こすものではありません。

対処方法:
*   特に必要な対処はありません。
*   もし過去にパフォーマンス上の理由などで履歴ベースのクエリ最適化を無効にしていた場合は、この機会に再有効化を検討することで、クエリパフォーマンスが向上する可能性があります。プロジェクトや組織のポリシーに応じて、再有効化を評価してください。

用語説明:
*   **BigQuery**: Google Cloudが提供するフルマネージドでスケーラブルなデータウェアハウスサービス。大規模なデータセットに対して高速なSQLクエリ実行を可能にします。
*   **履歴ベースのクエリ最適化 (History-based query optimizations)**: BigQueryが過去のクエリ実行履歴や統計情報を利用して、現在のクエリの実行計画をより効率的に最適化する機能。これにより、クエリの実行時間とコストを削減できる可能性があります。

---

# Cloud Service Mesh
## Announcement
原文: CNI/managed data plane controller version 1.23.6-asm.15 is rolling out to all release channels.

説明: Cloud Service MeshのCNI (Container Network Interface) およびマネージドデータプレーンコントローラーのバージョン 1.23.6-asm.15 が、全てのリリースチャネルで展開されています。

## Fixed
原文:
|  |
|  |
| **CVE**
 | **CNI**
 | **MDP Controller**
 |
| CVE-2025-4802
 | Yes
    | Yes
    |
| CVE-2023-29383
 | Yes
    | Yes
    |
| CVE-2024-56406
 | Yes
    | Yes
    |
| CVE-2023-7008
 | Yes
    | Yes
    |
| CVE-2025-1377
 | Yes
    | Yes
    |
| CVE-2023-4039
 | Yes
    | Yes
    |
| CVE-2025-46836
 | Yes
    | Yes
    |
| CVE-2023-50495
 | Yes
    | Yes
    |
| CVE-2025-4598
 | Yes
    | Yes
    |
| CVE-2025-3576
 | Yes
    | Yes
    |
| CVE-2025-30258
 | Yes
    | Yes
    |
| CVE-2017-11164
 | Yes
    | Yes
    |
| CVE-2022-41409
 | Yes
    | Yes
    |
| CVE-2025-1372
 | Yes
    | Yes
    |
| CVE-2022-27943
 | Yes
    | Yes
    |
| CVE-2022-4899
 | Yes
    | Yes
    |
| CVE-2023-34969
 | Yes
    | Yes
    |
| CVE-2023-45918
 | Yes
    | Yes
    |

説明: このバージョンアップには、CNIおよびマネージドデータプレーンコントローラーに影響する多数の共通脆弱性識別子 (CVE) で識別されるセキュリティ脆弱性の修正が含まれています。

影響有無: **間接的に影響あり (セキュリティ体制の向上)**
理由: このリリースは、Cloud Service Meshのコンポーネントのバージョンアップと、それに伴うセキュリティ脆弱性の修正です。既存の機能への直接的な変更や非互換性はありませんが、セキュリティ上のリスクが低減され、システムのセキュリティ体制が強化されます。Cloud Service Meshを利用している場合は、これらの修正が適用されることでセキュリティが向上します。

対処方法:
*   Cloud Service Meshを利用している場合、このバージョンアップはセキュリティ向上のため推奨されます。
*   マネージドなCloud Service Meshの場合、通常はGoogle Cloudが自動的に更新を適用しますが、ご利用のリリースのチャネルや構成を確認し、更新が適用されていることを確認してください。
*   セルフマネージドな構成の場合、または特定のバージョンアップポリシーを設定している場合は、計画的にバージョンアップを適用することを検討してください。
*   更新後に、アプリケーションのネットワーク挙動に予期せぬ変更がないか、簡単な健全性チェックを行うことを推奨します。

用語説明:
*   **Cloud Service Mesh (ASM)**: Google Cloudが提供する、マネージドなIstioベースのサービスメッシュプラットフォーム。トラフィック管理、ポリシー施行、セキュリティ、オブザーバビリティ機能を提供します。
*   **CNI (Container Network Interface)**: Kubernetesエコシステムにおけるネットワークプラグインの標準インターフェース。コンテナにIPアドレスを割り当て、コンテナ間のネットワーク接続を確立するために使用されます。
*   **マネージドデータプレーンコントローラー (Managed Data Plane Controller)**: Cloud Service Meshのコンポーネントの一つで、サービスメッシュ内のデータプレーン（Envoyプロキシなど）を管理および制御する役割を担います。
*   **リリースチャネル (Release Channel)**: Google Kubernetes Engine (GKE) やCloud Service Meshなどで利用される、機能のリリース速度と安定性レベルを示す分類。通常、Rapid、Regular、Stableなどのチャネルがあります。
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアのセキュリティ脆弱性を識別するための標準的な命名規則。各CVEは、特定の脆弱性に対して一意の識別子を提供します。

# Title: September 09, 2025 
Link: https://cloud.google.com/release-notes#September_09_2025<br>
Google Cloud リリースノート調査結果を以下の通りご報告いたします。

---

# Apigee X
## Announcement
原文: On September 9, 2025, we released an updated version of Apigee (1-16-0-apigee-1).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
Apigeeの新しいバージョン `1-16-0-apigee-1` がリリースされました。このリリースの展開（ロールアウト）は本日開始され、全てのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまで、お客様のApigeeインスタンスでは新しい機能や修正が利用できない場合があります。

影響有無：
Apigee Xをご利用の場合、この新しいバージョンへの更新はGoogle Cloudによって自動的に行われるため、お客様側で直接的な操作は不要です。既存のワークロードへの破壊的な変更（Breaking Change）は通常想定されませんが、ロールアウト期間中は新機能や修正が適用されていない状態となる可能性があります。セキュリティ関連の更新も含まれているため、システム全体の健全性向上に寄与します。

対処方法：
基本的に自動アップデートされるため、お客様側での明示的な対処は不要です。ただし、Apigeeインスタンスが新しいバージョンに更新されたことを確認するために、Apigeeのバージョン情報を定期的に確認することを推奨します。

用語説明：
*   **Apigee X**: Google Cloud上で提供されるAPI管理プラットフォームです。APIの設計、セキュリティ、分析、モニタリングなどを提供し、大規模なAPIプログラムを管理するのに役立ちます。
*   **ロールアウト (Rollout)**: ソフトウェアやシステムの新しいバージョンを段階的に展開していくプロセスを指します。これにより、変更による影響を最小限に抑えつつ、新機能を普及させます。

## Changed
原文: Updates to security infrastructure and libraries.

説明：
Apigeeを支える基盤となるセキュリティインフラストラクチャと、使用されているライブラリが更新されました。これには、既知の脆弱性への対応や、セキュリティ機能の強化が含まれる可能性があります。

影響有無：
利用中のApigeeインスタンスは自動的にこれらのセキュリティアップデートを受け取るため、セキュリティ体制が強化されます。お客様の既存のワークロードに直接的な影響はありませんが、セキュリティリスクの低減という点でポジティブな影響があります。

対処方法：
特になし。自動的に適用されるため、お客様側での対処は不要です。

用語説明：
*   **セキュリティインフラストラクチャ (Security Infrastructure)**: システムやアプリケーションを保護するための基盤となるセキュリティ関連のコンポーネント、サービス、設定の総称です。
*   **ライブラリ (Libraries)**: プログラミングにおいて再利用可能な機能を提供するコードの集合体です。セキュリティ関連のライブラリは、暗号化、認証、データ検証などを行うための機能を提供します。

---

# BigQuery
## Changed
原文: You can now perform supervised tuning on a BigQuery ML remote model based on a Vertex AI `gemini-2.5-pro` or `gemini-2.5-flash-lite` model.
[supervised tuning](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model#supervised_tuning)
[remote model](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model)

説明：
BigQuery MLのリモートモデルにおいて、Vertex AIの `gemini-2.5-pro` または `gemini-2.5-flash-lite` モデルを基盤としたモデルで、教師ありチューニング（Supervised Tuning）を実行できるようになりました。これにより、これらの高性能な大規模言語モデル（LLM）をBigQueryから直接利用し、特定のタスクやデータセットに合わせてモデルの性能を向上させることが可能になります。

影響有無：
BigQuery MLをご利用のお客様にとって、大規模言語モデルを活用した新しい機械学習ワークロードをBigQuery内で完結できる選択肢が増えるため、ポジティブな影響があります。既存のBigQuery MLの機能やパフォーマンスに悪影響を与えるものではありません。

対処方法：
新機能のため、既存の利用方法に影響はありません。この機能を利用したい場合は、BigQuery MLのドキュメントを参照し、`CREATE REMOTE MODEL` 文の新しい構文やチューニングオプションについて学習し、導入を検討してください。

用語説明：
*   **BigQuery ML**: Google BigQuery内で標準SQLを使用して機械学習モデルを作成、トレーニング、評価、デプロイできる機能です。データの移動なしに、分析とMLを統合できます。
*   **リモートモデル (Remote Model)**: BigQuery MLが直接管理するのではなく、BigQueryの外部に存在する機械学習モデル（この場合はVertex AI）を参照し、BigQueryから推論などを実行できるモデルタイプです。
*   **Vertex AI**: Google Cloudが提供する統合型機械学習プラットフォームです。データ準備からモデルのトレーニング、デプロイ、管理まで、MLライフサイクル全体をサポートします。
*   **Gemini 2.5 Pro / Gemini 2.5 Flash Lite**: Googleが開発した最新世代の大規模言語モデル（LLM）であるGeminiの特定のバージョンです。`Pro`は高性能な利用、`Flash Lite`は高速かつコスト効率の良い利用に適しています。
*   **教師ありチューニング (Supervised Tuning)**: 既存の基盤モデル（ここではGemini）を、特定のタスクに適した入力と出力のペア（教師データ）を用いて追加で学習させることで、モデルの性能を特定のユースケースに合わせて最適化するプロセスです。ファインチューニングとも呼ばれます。

---

# Compute Engine
## Changed
原文: Hyperdisk Balanced High Availability disks are available in all regions.
Hyperdisk Balanced High Availability disks synchronously replicate disk data from one zone to another. Cross-zonal replication provides data protection in the unlikely event of a zonal outage. For more information, see About Hyperdisk Balanced High Availability.
[About Hyperdisk Balanced High Availability](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha)

説明：
高性能ディスクタイプであるHyperdisk Balanced High Availability (HA) ディスクが、全てのGoogle Cloudリージョンで利用可能になりました。このディスクは、ディスクデータをあるゾーンから別のゾーンへ同期的に複製することで、万が一のゾーン障害が発生した場合にもデータ保護を提供するよう設計されています。

影響有無：
Compute Engineをご利用のお客様にとって、特に高い可用性と耐障害性が求められるワークロードにおいて、新しいディスクタイプを選択できるようになったため、ポジティブな影響があります。既存のディスクタイプや構成に直接的な影響はありません。新規に高可用性構成を検討する際や、既存システムのリライアビリティ向上を検討する際の新たな選択肢となります。

対処方法：
現在Compute Engineで運用しているシステムにおいて、ゾーン障害に対する耐性をさらに高めたい場合や、より高いパフォーマンスと可用性を両立させたい場合に、Hyperdisk Balanced HAディスクへの移行または新規導入を検討してください。導入に際しては、パフォーマンス要件とコスト、およびアプリケーションの要件を総合的に評価することが重要です。

用語説明：
*   **Hyperdisk Balanced High Availability (HA) ディスク**: Google Compute Engineが提供するブロックストレージの一種で、高いIOPSとスループットを持ちながら、ディスクデータを異なるゾーン間で同期的に複製することで、ゾーン障害に対する高い可用性を提供するように設計されています。
*   **リージョン (Region)**: Google Cloudのリソースがデプロイされる特定の地理的エリア（例: `us-central1`, `asia-northeast1`）です。
*   **ゾーン (Zone)**: リージョン内にある独立した物理的なロケーション（例: `us-central1-a`, `us-central1-b`）です。ゾーンは互いに独立しており、一つのゾーンの障害が他のゾーンに影響を与えないように設計されています。
*   **同期複製 (Synchronously Replicate)**: データが書き込まれる際に、そのデータが複数の場所にほぼ同時に書き込まれることを保証するデータ複製方法です。これにより、データの一貫性と可用性が高まります。
*   **ゾーン障害 (Zonal Outage)**: 特定のGoogle Cloudゾーン全体がサービス不能になる事象です。Hyperdisk Balanced HAは、このような事象発生時にもデータへのアクセスを継続できるように設計されています。

---
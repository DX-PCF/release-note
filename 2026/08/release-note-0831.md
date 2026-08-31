
# Title: August 27, 2026 
Link: https://docs.cloud.google.com/release-notes#August_27_2026<br>
Google Cloud のリリースノートに基づき、各サービスへの影響を調査し、回答します。

---

# Apigee X
## Announcement
原文: On August 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-4).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigee の新しいバージョン (1-18-0-apigee-4) がリリースされました。このバージョンのロールアウト（展開）は既に開始されており、すべての Google Cloud ゾーンで完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまで、利用中の Apigee インスタンスでは新機能や修正が利用できない場合があります。

影響有無: 影響あり。
Apigee はフルマネージドサービスであるため、このバージョンアップは自動的に適用されます。利用者が手動でアップグレード操作を行う必要はありません。ただし、ロールアウト期間中は新機能やバグ修正が段階的に適用されるため、環境によっては一時的に機能の利用可否に差異が生じる可能性があります。既存の API プロキシや設定に対する非互換性の変更 (Breaking Change) は記載されていませんが、念のため動作監視を推奨します。

対処方法: 特段の対処は不要です。Apigee を利用しているアプリケーションの動作に変化がないか、ロールアウト期間中は監視を強化することをお勧めします。

用語説明:
*   **ロールアウト (Rollout)**: 新しいソフトウェアバージョンや機能が、システム全体に段階的に展開・適用されるプロセスを指します。
*   **Google Cloud ゾーン (Google Cloud Zone)**: Google Cloud のサービスが展開される地理的な細分化されたリージョン内の区画。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **507878328** | Upgraded the Apigee runtime to run on JDK 17, while maintaining backward compatibility with JDK 11. |
| **530965355** | Added an opt-in Message Processor connection-failure back-off (CWC property HTTPClient.backoff.enabled, defaults to false) that prevents the Message Processor from consuming excessive CPU when a target is completely unavailable. |
| **532793298** | Fixed an API product bug where combining a payloadOperationGroup with a REST or llmOperationGroup rejected REST/LLM traffic with a 401. |
| **534420582** | The JSONThreatProtection policy adds a new optional child element <RejectDuplicateKeys> that rejects request bodies containing duplicate JSON keys within the same object. Defaults to false to preserve existing behavior. |
| **N/A** | Updates to infrastructure and libraries. |

説明: 複数のバグ修正と機能改善が含まれています。
*   Apigee ランタイムが JDK 17 にアップグレードされましたが、JDK 11 との下位互換性は維持されています。
*   Message Processor がターゲットサービスの障害時に過剰な CPU を消費するのを防ぐため、接続失敗時のバックオフ機能が追加されました（デフォルトは無効）。
*   API プロダクトの設定において、`payloadOperationGroup` と `REST` または `llmOperationGroup` を組み合わせた場合に、REST/LLM トラフィックが 401 エラーで拒否されるバグが修正されました。
*   `JSONThreatProtection` ポリシーに、同一オブジェクト内の重複する JSON キーを持つリクエストボディを拒否する新しいオプション要素 `<RejectDuplicateKeys>` が追加されました（デフォルトは既存動作を維持するため `false`）。
*   インフラストラクチャとライブラリの更新が行われました。

影響有無: 影響あり（主に機能改善と安定性向上）。
*   **JDK 17へのアップグレード**: 下位互換性が維持されているため、既存の API プロキシへの直接的な影響は低いと見込まれます。ランタイムの安定性やパフォーマンス向上が期待されます。
*   **Message Processor back-off**: デフォルトで無効であるため、既存の動作には影響しません。必要に応じてオプトインで有効化することで、ターゲットサービス障害時の Apigee のリソース消費を抑制できます。
*   **API Product バグ修正**: 該当のバグに遭遇していた場合は、修正によって正常な動作に戻るため、ポジティブな影響があります。
*   **JSONThreatProtection policy**: デフォルトで無効であるため、既存のポリシー動作には影響しません。セキュリティ要件に応じて有効化を検討できますが、有効化した場合、クライアントからのリクエストが拒否される可能性があるため、影響範囲を確認する必要があります。
*   **インフラ/ライブラリ更新**: Apigee サービスの全体的な安定性、セキュリティ、パフォーマンスの向上が期待されます。

対処方法:
*   JDK 17 へのアップグレードは Apigee の内部ランタイムの変更であり、利用者が直接対応する必要はありません。
*   Message Processor のバックオフ機能は、高負荷環境や外部システムとの連携が多いシステムにおいて、必要に応じて `HTTPClient.backoff.enabled` プロパティを `true` に設定することを検討してください。
*   `JSONThreatProtection` ポリシーの `RejectDuplicateKeys` 機能は、セキュリティ要件に応じて有効化を検討してください。有効化する際は、アプリケーションやクライアントからのリクエストが重複キーを含んでいないことを確認するか、その影響を許容できるか事前にテスト環境で検証することを強く推奨します。
*   API Product のバグは修正済みであるため、特段の対処は不要です。

用語説明:
*   **JDK (Java Development Kit)**: Java アプリケーションの開発と実行に必要なツールとライブラリのセットです。
*   **Message Processor (MP)**: Apigee ランタイムの中核コンポーネントであり、API リクエストの受信、ポリシーの適用、バックエンドへのルーティングなどを担当します。
*   **API Product**: Apigee で管理される API を論理的にグループ化し、アクセス制御、クォータ、レート制限などを定義するための単位です。
*   **JSONThreatProtection policy**: Apigee のセキュリティポリシーの一つで、JSON 形式のリクエストペイロードに対する脅威（例: 深いネスト、巨大なペイロード、重複キーなど）を検出し、防止するために使用されます。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **544570126** | **Security fix for Apigee.** Fixed a security issue in the PythonScript policy. |
| **N/A** | **Security fix for Apigee infrastructure.** |

説明: Apigee の PythonScript ポリシーおよび基盤インフラストラクチャにおけるセキュリティ脆弱性が修正されました。

影響有無: 影響なし（ポジティブな影響）。
セキュリティ脆弱性が修正されるため、Apigee 環境のセキュリティが向上します。これは Apigee サービスの信頼性と安全性を高めるものであり、利用者にとってはポジティブな影響です。

対処方法: 特段の対処は不要です。Apigee がフルマネージドサービスであるため、これらのセキュリティ修正は自動的に適用されます。

用語説明:
*   **PythonScript policy**: Apigee のポリシーの一つで、API リクエスト/レスポンス処理フロー内でカスタムの Python スクリプトを実行できるようにする機能です。これにより、複雑なロジックや特定のデータ変換を実装できます。

---

# BigQuery
## Announcement
原文: Core graph processing for BigQuery Graph requires an Enterprise or Enterprise Plus edition reservation. Existing allowlisted users can continue to use Standard edition or on-demand billing until April 26, 2027, after which these billing models will no longer be supported for core graph processing.
[BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview)
Graph measures will remain available in the Enterprise and Enterprise Plus editions and for queries run using on-demand pricing. Measures are not available in Standard edition.
[Graph measures](https://docs.cloud.google.com/bigquery/docs/graph-measures)

説明: BigQuery Graph のコアグラフ処理機能について、利用可能なエディションが変更されます。今後は Enterprise または Enterprise Plus エディションのリザーベーションが必要となります。既存の許可リストに登録されているユーザーは、2027年4月26日までは Standard エディションまたはオンデマンド課金を引き続き利用できますが、それ以降はこれらの課金モデルでのコアグラフ処理はサポートされなくなります。一方、Graph measures 機能は、引き続き Enterprise および Enterprise Plus エディション、およびオンデマンド課金で利用可能ですが、Standard エディションでは利用できません。

影響有無: 影響あり。
BigQuery Graph のコアグラフ処理機能を利用しており、現在 Standard エディションのリザーベーション、またはオンデマンド課金モデルで BigQuery を利用している場合、2027年4月26日以降はコアグラフ処理機能が利用できなくなります。継続して利用するためには、Enterprise または Enterprise Plus エディションのリザーベーションへの移行が必要になります。

対処方法:
1.  BigQuery Graph のコアグラフ処理機能を利用しているか確認します。
2.  利用している場合、現在利用している BigQuery のエディションおよび課金モデル（Standard エディションのリザーベーションまたはオンデマンド課金）を確認します。
3.  上記に該当する場合、2027年4月26日までに BigQuery Graph の継続利用の要否を判断し、必要であれば Enterprise または Enterprise Plus エディションのリザーベーションへの移行を計画してください。移行には料金体系の変更が伴うため、コストへの影響も評価することが重要です。

用語説明:
*   **BigQuery Graph**: BigQuery の機能の一つで、グラフデータ分析を可能にし、エンティティ間の関係性を探索・分析するのに役立ちます。
*   **Enterprise/Enterprise Plus edition**: BigQuery のエディションで、Standard エディションと比較して、より高度な機能、高いパフォーマンス、厳格な SLA、および強化されたサポートを提供する上位エディションです。
*   **Reservation (BigQuery Reservations)**: BigQuery の計算リソース（スロット）を事前に予約する課金モデルです。これにより、安定したクエリパフォーマンスを確保し、オンデマンド課金よりもコスト効率が良い場合があります。
*   **On-demand billing (オンデマンド課金)**: BigQuery の課金モデルの一つで、実行したクエリが処理したデータ量に基づいて料金が発生します。
*   **Graph measures**: BigQuery Graph において、グラフ分析から得られる特定の指標や計算結果を指します。

---

# Cloud SQL for PostgreSQL
## Change
原文: The rollout of the following extension upgrades is complete:
- `pg_partman` is upgraded from 5.2.4 to 5.4.3.
- `pgfincore` is upgraded from 1.3.1 to 1.4.
- `pgvector` is upgraded from 0.8.1 to 0.8.5.
For more information, see Configure PostgreSQL extensions.
[Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions)

説明: Cloud SQL for PostgreSQL において、以下の拡張機能のアップグレードが完了しました。
*   `pg_partman` がバージョン 5.2.4 から 5.4.3 へアップグレードされました。
*   `pgfincore` がバージョン 1.3.1 から 1.4 へアップグレードされました。
*   `pgvector` がバージョン 0.8.1 から 0.8.5 へアップグレードされました。

影響有無: 影響あり（機能改善、潜在的な互換性考慮）。
これらの PostgreSQL 拡張機能を利用している Cloud SQL for PostgreSQL インスタンスでは、自動的にアップグレードが適用されています。通常、パッチバージョンやマイナーバージョンアップでは後方互換性が維持されることが多いですが、機能の追加や改善により、既存のアプリケーションで予期しない動作変更がないか、念のため確認することを推奨します。特に `pgvector` は AI/ML 関連で利用されることが増えており、その機能改善はポジティブな影響をもたらす可能性があります。

対処方法:
*   上記の拡張機能を利用している場合は、アップグレードされたバージョンでの動作に問題がないか、既存のアプリケーションのテスト環境で動作確認を行うことを推奨します。
*   各拡張機能の具体的な変更内容については、それぞれの公式ドキュメントや変更履歴を参照し、非互換性のある変更がないか確認してください。

用語説明:
*   **PostgreSQL extensions (拡張機能)**: PostgreSQL の標準機能に加えて、特定の機能、データ型、関数などを追加するモジュールです。
*   **`pg_partman`**: PostgreSQL のテーブルパーティショニングを自動的に管理し、パーティションの作成・削除を効率化するための拡張機能です。
*   **`pgfincore`**: PostgreSQL がファイルシステムのページキャッシュ（メモリキャッシュ）を操作し、パフォーマンスを最適化するための機能を提供する拡張機能です。
*   **`pgvector`**: PostgreSQL にベクトル埋め込み（vector embeddings）のサポートを追加し、高次元空間における類似性検索（similarity search）を可能にする拡張機能です。AI/ML アプリケーションで特に重要です。

---

# Cloud Service Mesh
## Security
原文: The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.6-asm.71 is rolling out to the rapid release channel.
- 1.20.8-asm.119 is rolling out to the regular release channel.
- 1.19.10-asm.109 is rolling out to the stable release channel.
These versions resolve the security vulnerabilities listed in Security Bulletin
GCP-2026-057.
[GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057)

説明: マネージド Cloud Service Mesh の各リリースチャネル（rapid、regular、stable）向けに、セキュリティ脆弱性 (GCP-2026-057) を解決する新しいバージョンが現在展開されています。

影響有無: 影響なし（ポジティブな影響）。
セキュリティ脆弱性が修正されるため、Cloud Service Mesh 環境のセキュリティ体制が向上します。Cloud Service Mesh はマネージドサービスであるため、これらのアップデートは自動的に適用されます。機能的な非互換性は低いと考えられますが、サービスメッシュのバージョン更新により、念のため既存のワークロードに意図しない動作変更がないか注意深く監視することが推奨されます。

対処方法:
*   特段の対処は不要です。
*   Cloud Service Mesh を利用する重要なサービスの場合、アップデート適用後にアプリケーションの動作に問題がないか、通常よりも注意深く監視することをお勧めします。必要に応じて、利用中のリリースチャネルがビジネス要件に合致しているか再評価することも検討できます。

用語説明:
*   **Cloud Service Mesh (ASM)**: Google Cloud が提供するフルマネージドのサービスメッシュ。Istio をベースとしており、マイクロサービス間の通信、監視、セキュリティ、トラフィック管理を簡素化します。
*   **Release Channel (リリースチャネル)**: Cloud Service Mesh のバージョン更新が提供される頻度と安定性を示すチャネルです。
    *   `rapid`: 最新の機能や修正が最も早く提供されますが、安定性は他のチャネルより低い可能性があります。
    *   `regular`: 安定性と最新機能のバランスが取れています。
    *   `stable`: 最も安定性が重視され、検証されたバージョンが提供されます。
*   **Security Bulletin (セキュリティ速報)**: 既知のセキュリティ脆弱性、その影響、および提供される修正に関する情報を提供する公式文書です。
*   **GCP-2026-057**: Google Cloud Service Mesh の特定のセキュリティ脆弱性に関連する識別子です。
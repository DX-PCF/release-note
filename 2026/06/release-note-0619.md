
# Title: June 18, 2026 
Link: https://docs.cloud.google.com/release-notes#June_18_2026<br>
Google Cloud のリリースノート調査結果は以下の通りです。

---

# Apigee X

## Announcement

**原文:**
On June 18th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-9**, your instance will be updated to **1-17-0-apigee-9** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will not be updated:
- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.

**説明:**
2026年6月18日より、メンテナンスウィンドウを設定しているApigeeインスタンスのメンテナンスアップデートが開始されました。もしお客様のApigeeインスタンスがメンテナンスウィンドウを設定しており、かつバージョンが `1-17-0-apigee-9` 未満である場合、今後7〜21日以内に自動的に `1-17-0-apigee-9` にアップデートされます。アップグレード予定日を含む通知は、今後2営業日以内に送信されます。
ただし、以下のいずれかの条件に該当するインスタンスはアップデートされません。
1.  既知の問題 445936920 に記載されているDNS設定ミスが存在する場合。
2.  2025年10月16日付のApigeeリリースノートに記載されている、既に削除されたApigee Java Libraryを使用している場合。

詳細については、[Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) および [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows) を参照してください。

**影響有無:**
**影響あり。**
Apigee X インスタンスを運用しており、かつメンテナンスウィンドウを設定している場合、対象バージョンのインスタンスは強制的にアップデートされます。これは、セキュリティパッチの適用やプラットフォームの安定性向上を目的としたものですが、APIプロキシやカスタムポリシーの動作に予期せぬ影響がないか、事前の確認が推奨されます。特に、削除されたApigee Java Libraryを使用している場合は、そのインスタンスはアップデートされませんが、ライブラリの非推奨化に伴う機能停止のリスクがあります。また、DNS設定ミスがある場合もアップデート対象外となるため、健全性の観点から修正が必要です。

**対処方法:**
1.  **インスタンスバージョンの確認:** Apigee X インスタンスの現在のバージョンを確認し、`1-17-0-apigee-9` 未満であるかを確認してください。
2.  **通知の監視:** Google Cloudからのアップグレード予定日に関する通知メールを注意深く確認してください。
3.  **互換性テストの実施:** アップデート前に、可能であればテスト環境などで既存のAPIプロキシやカスタムポリシーが `1-17-0-apigee-9` で正しく動作するか互換性テストを実施することを強く推奨します。
4.  **Apigee Java Libraryの使用状況確認:** カスタムロジックでApigee Java Libraryを使用している場合、[2025年10月16日付のApigeeリリースノート](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025) を参照し、削除対象のライブラリを利用していないか確認してください。利用している場合は、代替手段への移行を計画してください。
5.  **DNS設定の確認と修正:** [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues) を参照し、DNS設定に問題がないことを確認してください。問題がある場合は、サービス可用性に影響を及ぼす可能性があるため、速やかに修正してください。

**用語説明:**
*   **Apigee X:** Google Cloudが提供するAPI管理プラットフォームの最新バージョン。APIの設計、セキュリティ、デプロイ、トラフィック管理、監視などを統合的に行います。
*   **メンテナンスウィンドウ (Maintenance windows):** Google Cloudなどのクラウドプロバイダが、基盤サービスのメンテナンスを実施するために指定する時間帯。ユーザーは、サービス停止やパフォーマンス低下のリスクを最小限に抑えるために、自社のサービスに影響の少ない時間帯をこのウィンドウとして設定できます。
*   **Apigee Java Library:** Apigeeプラットフォーム上でカスタムビジネスロジックを実装するために使用できるJavaベースのライブラリ群。例えば、Java Calloutポリシーを通じて利用されます。
*   **DNS misconfiguration:** ドメインネームシステム (DNS) の設定が誤っている状態。これにより、ドメイン名が正しいIPアドレスに解決されず、サービスへのアクセス障害や通信問題が発生する可能性があります。

---

# Cloud Logging

## Change

**原文:**
The Cloud Logging API adds support for the `ca` regional endpoint. For a complete list of regional endpoints, see the REST reference pages.

**説明:**
Cloud Logging APIが、カナダ（`ca`）リージョンにおけるエンドポイントのサポートを追加しました。これにより、ログデータをカナダリージョンに明示的にルーティングし、保存することが可能になります。利用可能なすべてのリージョンエンドポイントのリストは、[REST reference pages](https://docs.cloud.google.com/logging/docs/reference/v2/rest?rep_location=global) で確認できます。

**影響有無:**
**影響なし（ただし、新規要件によってはポジティブな影響あり）。**
既存のロギング構成やデータフローに自動的な変更は発生しないため、直接的な負の影響はありません。しかし、カナダリージョンにデータを保持したいといったデータレジデンシー要件や、カナダリージョン内のワークロードに対するログ収集のレイテンシ最適化を求める場合には、この新しいエンドポイントを利用できるようになるため、ポジティブな影響があります。

**対処方法:**
既存の構成を変更する必要がなければ、特別な対処は不要です。
もし、カナダリージョンにGoogle Cloudリソースをデプロイしており、ログデータを同リージョンに保持したい、またはレイテンシを最適化したい場合は、Cloud Logging APIクライアントやロギングエージェント（例えばFluentdやLogstashなど）の設定において、`ca` リージョンエンドポイントを明示的に使用するように変更することを検討してください。

**用語説明:**
*   **Cloud Logging:** Google Cloudが提供するフルマネージドなロギングサービス。Google Cloudリソース、オンプレミス、他のクラウド環境からのログデータを取り込み、一元的に保存、検索、分析、エクスポートできます。
*   **リージョンエンドポイント (Regional endpoint):** クラウドサービスが特定の地理的リージョン内に提供するAPIアクセスポイント。データレジデンシー要件（データが特定の国や地域に留まる必要がある規制）を満たすためや、ネットワークレイテンシを最小化するために利用されます。特定のリージョンエンドポイントを使用することで、そのリージョン内でデータの処理と保存が行われることが保証されやすくなります。
*   **REST reference pages:** RESTful APIの仕様、利用可能なリソース、HTTPメソッド、パラメータ、レスポンス形式などに関する詳細な公式ドキュメント。APIをプログラムから利用する開発者やインフラエンジニアが参照します。
# Title: June 16, 2026 
Link: https://docs.cloud.google.com/release-notes#June_16_2026<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響を調査いたしました。

---

# BigQuery
## Announcement
原文: `Table Explorer behavior is moving to the **Reference** panel. This transition will occur in July 2026 or later. For more information, see Table Explorer.`

説明：
BigQuery コンソールにおける「Table Explorer」の表示挙動が変更され、**Reference** パネルに機能が統合されるというアナウンスです。この機能移行は、2026年7月以降に実施される予定です。

影響有無：
**影響なし**
これはUIの配置変更に関するアナウンスであり、機能の廃止や既存のデータ、クエリの実行には影響ありません。変更は2026年7月以降と将来の予定であるため、現時点での運用への影響はありません。

対処方法：
現時点での具体的な対処は不要です。2026年7月以降にUIが変更された際、BigQuery コンソールでのテーブル情報の参照方法が一部変わることを認識しておき、必要に応じて新しいUIに慣れてください。

用語説明：
*   **Table Explorer**: BigQuery コンソール内で、データセット内のテーブルやビューの詳細情報（スキーマ、詳細、プレビュー、パーティション情報など）を確認できる機能です。
*   **Reference panel**: BigQuery コンソールのSQLエディタの右側などに表示され、テーブルやカラムのドキュメント、関数情報などを参照できるパネルです。

---

# Compute Engine
## Change
原文: `For resource-based committed use discounts (CUDs), the default value of CUD scope for most Cloud Billing accounts has changed from **Project** to **Billing account**. If the CUD scope is set to **Billing account**, then resource-based CUDs from a commitment are shared across all projects in that account. If the CUD scope is set to **Project**, then resource-based CUDs from a commitment are available to only the project in which you purchased that commitment. Depending on the Cloud Billing account's creation date and the active commitments in that account, this change applies in the following way: - **Cloud Billing accounts created on or after June 16, 2026**: The CUD scope is **Billing account** (CUD sharing enabled) by default. - **Cloud Billing accounts created before June 16, 2026**: - If the account has **no active resource-based commitments** on June 16, 2026, then the CUD scope has changed to **Billing account** (CUD sharing enabled). - If the account has **any active resource-based commitments** on June 16, 2026, then the CUD scope remains unchanged and Google Cloud continues to use your existing configuration. For more information, see Share resource-based CUDs across projects.`

説明：
Compute Engine のリソースベースのコミット済み利用割引 (CUD) において、その適用範囲 (CUD scope) のデフォルト値が、大半の Cloud Billing アカウントで「プロジェクト (Project)」から「請求先アカウント (Billing account)」に変更されました。
*   「Billing account」スコープの場合、購入した CUD は当該請求先アカウント内の全てのプロジェクトで共有され、割引が適用されます。
*   「Project」スコープの場合、CUD は購入した特定のプロジェクトのみに適用されます。

この変更の適用条件は、Cloud Billing アカウントの作成日と、2026年6月16日時点でのアクティブなリソースベース CUD の有無によって異なります。
*   **2026年6月16日以降に作成された Cloud Billing アカウント**: デフォルトで CUD スコープは「Billing account」となります。
*   **2026年6月16日より前に作成された Cloud Billing アカウント**:
    *   2026年6月16日時点でアクティブなリソースベース CUD が**存在しない**場合: CUD スコープは「Billing account」に変更されます。
    *   2026年6月16日時点でアクティブなリソースベース CUD が**存在する**場合: 既存の設定（スコープ）が維持されます。

詳細については、[Share resource-based CUDs across projects](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#cud-scope-configuration) を参照してください。

影響有無：
**潜在的な影響あり**
この変更は、Compute Engine のコスト最適化戦略に直接影響を与える可能性があります。特に複数のプロジェクトで Compute Engine リソースを利用している場合、デフォルトのスコープが「Billing account」になることで、CUDの利用効率が向上し、全体のコスト削減に繋がる可能性があります。一方で、既存のコスト管理や課金レポートのロジックに影響がないか確認が必要です。この変更は2026年6月16日という将来の日付を基準としているため、現時点での直接的な運用影響は少ないですが、将来のCUD購入や請求アカウントの管理に影響を与えるため、認識しておくべきです。

対処方法：
1.  **自社 Cloud Billing アカウントの状況確認**: 現在利用している Cloud Billing アカウントが、上記変更のどの条件（作成日、2026年6月16日時点のアクティブな CUD の有無）に該当するかを確認してください。
2.  **コスト管理方針との整合性確認**:
    *   現在リソースベース CUD を利用しており、既存の設定が維持される場合、すぐに変更の必要はありませんが、将来的に新たな CUD を購入する際に、デフォルトスコープが「Billing account」になる可能性があることを考慮に入れてください。
    *   現在 CUD を利用していない場合、または2026年6月16日時点で CUD がない場合で、将来 CUD の導入を検討している場合は、デフォルトで「Billing account」スコープとなることで、コスト効率が向上するかどうかを評価してください。
3.  **関連部署との連携**: コスト管理チームや財務担当者と連携し、この変更が請求体系やコスト分析に与える影響について認識を共有し、必要に応じて対応方針を検討してください。

用語説明：
*   **Committed Use Discounts (CUDs)**: （コミット済み利用割引）Google Cloud のリソース（例: Compute Engine VM）を一定期間（通常1年または3年）利用することをコミットすることで得られる大幅な割引です。オンデマンド料金よりも低価格でリソースを利用できます。
*   **Resource-based CUDs**: 特定のリソースタイプ（例: 特定のvCPU数、メモリ量）の利用に対して適用される CUD です。VM インスタンスの稼働時間ではなく、プロビジョニングされたリソース量に対して割引が適用されます。
*   **CUD scope**: CUD の適用範囲を指します。
    *   **Project**: CUD を購入した特定のプロジェクト内でのみ割引が適用されます。
    *   **Billing account**: CUD を購入した請求先アカウントに関連付けられている全てのプロジェクトで CUD が共有され、割引が適用されます。これにより、複数のプロジェクト間でリソース利用量の変動があっても、請求先アカウント全体で CUD を最大限に活用し、コスト最適化を図りやすくなります。
# Title: June 15, 2026 
Link: https://docs.cloud.google.com/release-notes#June_15_2026<br>
# BigQuery
## Issue
原文: Support for configuring daily token quotas for BigQuery generative AI functions has been temporarily disabled. We are working to restore this feature as soon as possible.

説明: BigQueryの生成AI機能（`ML.GENERATE_TEXT`など）において、日次トークン使用量の上限（クォータ）を設定する機能が一時的に無効化されています。Google Cloudは、この機能をできるだけ早く復旧させるために取り組んでいます。

影響有無: BigQueryの生成AI機能を利用しており、特に**日次トークン使用量の上限を設定してコスト管理を行っている、またはこれから設定しようとしていたユーザー**に影響があります。この機能が一時的に無効化されているため、意図したトークン使用量の制限ができない可能性があります。ただし、生成AI機能自体の利用が停止したわけではありません。

対処方法:
この機能の一時的な無効化はGoogle Cloud側で対応中であるため、ユーザー側で直接的な対処はできません。
*   現在、BigQueryの生成AI機能を利用している場合は、予期せぬトークン使用量の増加によるコストを避けるため、Cloud MonitoringなどでBigQueryのクエリ実行や`ML.GENERATE_TEXT`などの関数の利用状況を監視し、必要に応じてアラートを設定することを推奨します。
*   機能の復旧を待ち、復旧後に日次トークンクォータの設定を再確認または再設定してください。

用語説明:
*   **BigQuery generative AI functions (BigQuery 生成AI機能)**: BigQuery MLの機能の一つで、SQL文から直接、大規模言語モデル（LLM）を利用できる機能です。例えば、`ML.GENERATE_TEXT`関数を使用してテキスト生成、要約、感情分析などを行うことができます。
*   **Daily token quotas (日次トークンクォータ)**: 生成AIモデルが処理するテキストの最小単位である「トークン」の1日あたりの使用量に設定できる上限値です。これにより、予期せぬ高額な利用料金を防ぎ、コストを管理することが可能になります。

---

# Title: February 17, 2026 
Link: https://docs.cloud.google.com/release-notes#February_17_2026<br>
ご担当者様

Google Cloudのリリースノートに関するお問い合わせ、ありがとうございます。インフラエンジニアとして、BigQueryサービスへの影響を調査し、以下の通り回答いたします。

---

# BigQuery

## Deprecated

**原文:**
Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices constraint` won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM deny policies.

**説明:**
2026年3月17日以降、組織ポリシー（Organization Policies）において、`gcp.managed.allowedMCPServices constraint` を使用したMCP（Managed Control Plane）の使用制御機能が非推奨となり、機能しなくなります。今後は、IAM拒否ポリシー（IAM deny policies）を使用してMCPの使用を制御することが推奨されます。詳細な制御方法については、[Control MCP use with IAM deny policies](https://docs.cloud.google.com/mcp/control-mcp-use-iam) のドキュメントを参照してください。

**影響有無:**
*   **影響あり**：現在、お客様の組織でBigQueryのMCP使用を制限するために `gcp.managed.allowedMCPServices constraint` を含む組織ポリシーを適用している場合、2026年3月17日以降、そのポリシーは機能しなくなります。
*   **影響なし**：上記の組織ポリシーを利用していない場合、直接的な影響はありません。

**対処方法:**
1.  **現状確認:** まず、お客様のGoogle Cloud組織において、`gcp.managed.allowedMCPServices constraint` を使用している組織ポリシーが存在するかどうかを確認してください。
2.  **移行計画:** もし該当の組織ポリシーを使用している場合、2026年3月17日までにIAM拒否ポリシーへの移行を計画・実行する必要があります。
3.  **ドキュメント参照:** 移行作業の具体的な手順や考慮事項については、提供されたリンク先の公式ドキュメント「[Control MCP use with IAM deny policies](https://docs.cloud.google.com/mcp/control-mcp-use-iam)」を詳細に参照し、適切なIAM拒否ポリシーを設計・適用してください。

**用語説明:**
*   **MCP (Managed Control Plane):** Google Cloudが提供するフルマネージドサービス（例: BigQuery）の背後にある、Googleによって管理される制御プレーンのこと。サービスのスケーリング、状態管理、API提供などを担当します。
*   **組織ポリシー (Organization Policy):** Google Cloudリソースの構成とデプロイに対して、組織レベルで制限やルールを設定できるサービス。リソースの一貫性を確保し、セキュリティとコンプライアンスを強化するために使用されます。
*   **制約 (Constraint):** 組織ポリシーで適用される特定のルールや条件を定義する要素。`gcp.managed.allowedMCPServices constraint` は、特定のManaged Control Planeサービスの利用を許可または拒否するための制約です。
*   **IAM拒否ポリシー (IAM deny policies):** IAM（Identity and Access Management）において、特定のアクション（操作）を明示的に拒否するためのポリシー。許可ポリシーよりも優先されるため、特定のユーザーやサービスアカウントが特定のリソースに対して行えることを厳密に制限するために使用されます。

---

## Change

**原文:**
After March 17, 2026, when you enable BigQuery, the BigQuery MCP server is automatically enabled.

**説明:**
2026年3月17日以降、BigQueryサービスを有効にする際（新規プロジェクトでのBigQuery APIの有効化や、既存プロジェクトでのBigQuery利用開始など）、BigQueryのMCPサーバーが自動的に有効化されるようになります。

**影響有無:**
*   **影響あり（将来的な動作変更）**：既存のBigQuery利用には直接影響しませんが、2026年3月17日以降に新規でBigQueryを有効化する際には、MCPサーバーが自動的に有効化される動作となります。
*   この変更は、上記の組織ポリシーの非推奨化と関連しており、MCPの制御方法がIAM拒否ポリシーに集約されることを意味します。MCPサーバーの自動有効化を阻止したい特別な要件がある場合は、IAM拒否ポリシーによる制御を検討する必要があります。

**対処方法:**
*   この変更はBigQueryのデフォルトの有効化動作に関するものであり、ほとんどのユースケースにおいては特別な対処は不要です。
*   ただし、BigQueryのMCPサーバーの自動有効化を明示的に避けたい特定の環境やコンプライアンス要件がある場合は、前述の「Deprecated」セクションで説明されているIAM拒否ポリシーを用いて、BigQuery MCPサーバーの有効化を制御することを検討してください。
*   現時点では、この自動有効化によって既存のワークロードに問題が発生する可能性は低いため、継続してGoogle Cloudのアップデート情報を注視してください。

**用語説明:**
*   **BigQuery MCP server:** BigQueryサービスが内部的に使用するManaged Control Planeのサーバーコンポーネント。BigQueryのクエリ実行、データ管理、メタデータ管理など、中核的な機能を提供します。

---

ご不明な点がございましたら、お気軽にお問い合わせください。
# Title: February 16, 2026 
Link: https://docs.cloud.google.com/release-notes#February_16_2026<br>
Google Cloud インフラエンジニアとして、お使いの環境（Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)）への影響有無を調査し、以下の通り回答いたします。

---

# Cloud Composer

## Change

原文:
```
 New Airflow builds
are available in Cloud Composer 3:

[Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-3.1.0-build.9
- composer-3-airflow-2.10.5-build.26 (default)
- composer-3-airflow-2.9.3-build.46

[composer-3-airflow-3.1.0-build.9](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-0-build-9)
[composer-3-airflow-2.10.5-build.26](https://cloud.google.com/composer/docs/versions-packages#composer-2-10-5-build-26)
[composer-3-airflow-2.9.3-build.46](https://cloud.google.com/composer/docs/versions-packages#composer-2-9-3-build-46)
```
説明：
Cloud Composer 3環境向けに、新しいApache Airflowのビルドバージョンが利用可能になりました。具体的には、Airflow 3.1.0、2.10.5（デフォルト）、2.9.3の新しいビルドイメージが追加されています。これらは、最新の機能や修正、セキュリティアップデートを含んでいる可能性があります。

影響有無：
影響なし。
貴社環境はCloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) をご利用のため、Cloud Composer 3に関する今回の変更は直接的な影響を与えません。

対処方法：
なし。

用語説明：
*   **Cloud Composer 3**: Google Cloudが提供するマネージドApache AirflowサービスであるCloud Composerのメジャーバージョンの一つです。新しい機能や、より新しいAirflowバージョン、および関連するGoogle Cloudサービスとの統合が強化されています。
*   **Airflow builds**: Apache Airflowの特定のバージョンに、Cloud Composer環境で最適に動作するためのGoogle Cloud独自のパッチ、依存関係、および設定を統合したパッケージ化されたイメージを指します。

## Change

原文:
```
 New images
are available in Cloud Composer 2:

[images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
- composer-2.16.4-airflow-2.10.5 (default)
- composer-2.16.4-airflow-2.9.3

[composer-2.16.4-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-16-4-airflow-2-10-5)
[composer-2.16.4-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-16-4-airflow-2-9-3)
```
説明：
Cloud Composer 2環境向けに、新しいComposerイメージが利用可能になりました。具体的には、`composer-2.16.4-airflow-2.10.5`（デフォルト）と`composer-2.16.4-airflow-2.9.3`が追加されています。これらのイメージは、新しいAirflowバージョンやComposerの機能更新を含んでいます。

影響有無：
影響なし（直接的）。
貴社環境はComposer version 2.7.1, Airflow version 2.7.3をご利用です。今回の発表は、既存環境のバージョンが自動的にアップグレードされるものではなく、新しいイメージが利用可能になったという情報です。したがって、現行の運用には直接的な影響はありません。ただし、将来的なアップグレードを検討する際には、これらの新しいイメージバージョンが選択肢となります。

対処方法：
現時点での即座の対応は不要です。しかし、Cloud Composer環境は継続的に改善されており、古いバージョンはサポート終了となる場合があります。そのため、貴社環境がサポートされている最新バージョンから大きく遅れていないか、定期的に確認し、計画的なアップグレードを検討することをお勧めします。新しいComposer 2.16.4とAirflow 2.10.5/2.9.3は、貴社の現在のComposer 2.7.1, Airflow 2.7.3よりも新しいバージョンです。

用語説明：
*   **Cloud Composer Image**: Cloud Composer環境の基盤となる仮想マシンイメージであり、特定のCloud ComposerバージョンとApache Airflowバージョン、および必要なソフトウェアコンポーネントがプリインストールされています。環境を新規作成したり、既存環境をアップグレードしたりする際に選択します。

## Deprecated

原文:
```
 The following Cloud Composer versions and builds have reached their
end of support period:
composer-3-airflow-2.9.3-build.15 and composer-2.11.2-*.

[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support)
```
説明：
以下のCloud Composerのバージョンおよびビルドが、サポート終了期間に達したことがアナウンスされました。対象は `composer-3-airflow-2.9.3-build.15` と `composer-2.11.2-*` です。サポート終了後は、セキュリティパッチやバグ修正が提供されなくなり、技術サポートも限定的になります。

影響有無：
影響なし。
貴社環境はComposer version 2.7.1, Airflow version 2.7.3をご利用です。サポート終了対象のバージョンは `composer-2.11.2-*` であり、貴社の `composer-2.7.1` とは異なります。したがって、貴社の環境には直接的な影響はありません。

対処方法：
なし。
ただし、Cloud Composerのライフサイクルポリシーに従い、現在ご利用のバージョンが将来的にサポート終了となる時期を定期的に確認し、計画的なアップグレードロードマップを策定することをお勧めします。

用語説明：
*   **End of Support (EOS) Period**: 特定のソフトウェアバージョンや製品に対するベンダー（この場合はGoogle Cloud）からの公式サポートが終了する期間を指します。この期間を過ぎると、新たなパッチやセキュリティアップデート、技術的な問題に対する修正が提供されなくなるため、運用上のリスクが増大します。

## Announcement

原文:
```
 A new Cloud Composer release has started on **February 16, 2026**. Get ready
for upcoming changes and features as we roll out the new release to all regions.
This release is in progress at the moment. Listed changes and features might
not be available in some regions yet.
```
説明：
2026年2月16日に新しいCloud Composerのリリースが開始されたとのアナウンスです。このリリースは現在、すべてのリージョンに展開中であり、記載されている変更点や新機能は、一部のリージョンではまだ利用できない可能性があるとのことです。
**注記**: 記載されている日付「February 16, 2026」は未来の日付であり、通常のリリースの表現とは異なります。これは将来のメジャーリリースに関する事前予告である可能性や、リリースノートの記述ミスである可能性も考えられます。

影響有無：
影響なし（直接的）。
貴社環境はComposer version 2.7.1, Airflow version 2.7.3をご利用です。2026年という未来の日付で開始されるリリースであるため、現時点での貴社環境への直接的な影響はありません。しかし、これは将来のCloud Composerのメジャーアップデートに関する重要な予告である可能性があり、その場合は将来のアップグレード計画やアーキテクチャの検討に影響を与える可能性があります。

対処方法：
現時点での即座の対応は不要です。しかし、このアナウンスが将来の重要なリリースを指している可能性があるため、定期的にCloud Composerの公式リリースノートやロードマップを確認し、今後の機能変更やアップグレードパスに関する情報を収集することが推奨されます。特に、現在ご利用のComposer 2.xがこの将来のリリースとどのように連携し、サポートされるのかを注視してください。

用語説明：
*   **Cloud Composer Release**: Cloud Composerサービス全体のアップデートを指します。これには、Apache Airflowのバージョンアップグレード、Google Cloudとの連携強化、新機能の追加、パフォーマンス改善、セキュリティ修正などが含まれます。メジャーリリースは、プラットフォームの大きな変更や、互換性に影響する可能性のある変更を伴うことがあります。
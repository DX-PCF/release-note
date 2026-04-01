
# Title: March 31, 2026 
Link: https://docs.cloud.google.com/release-notes#March_31_2026<br>
# Cloud NAT
## Announcement
原文: The default TCP `TIME_WAIT` timeout for Cloud NAT is scheduled to decrease from 120 seconds to 30 seconds, across all regions, as follows:
[`TIME_WAIT`](https://docs.cloud.com/nat/docs/tune-nat-configuration#nat-timeouts)
- **From June 30 to September 29, 2026**: new Cloud NAT gateways will use either the 120-second or 30-second default, depending on when the update is deployed in a specific region.
- **On or after September 30, 2026**: all new Cloud NAT gateways in all regions will use the 30-second default.

**Impact on gateways**
- **New gateways**: after the update is deployed in a region, all new Cloud NAT gateways created in that region will use the 30-second default. This change also applies if a pre-update gateway is deleted and then recreated.
- **Existing gateways**: Cloud NAT gateways created before the regional update will retain the 120-second default. You can adjust this value by using the `--tcp-time-wait-timeout` flag at any time. Cloud NAT gateways configured with a custom `TIME_WAIT` value aren't affected and will continue to use your configured custom value.

The following table outlines the applicable default timeout for new gateways throughout the deployment timeline.
| Gateway type | Default timeout(before June 30) | Default timeout(June 30—September 29) | Default timeout(on or after September 30) |
| --- | --- | --- | --- |
| New | 120 seconds | 30 or 120 seconds | 30 seconds |

説明:
Cloud NATサービスのTCP `TIME_WAIT`タイムアウトのデフォルト値が、現在の120秒から30秒へと段階的に短縮されることがアナウンスされました。この変更は2026年6月30日から9月29日までの期間に各リージョンで展開され、2026年9月30日以降は全ての新規Cloud NATゲートウェイで30秒がデフォルト値となります。既存のCloud NATゲートウェイはデフォルト値が120秒のままで維持されますが、新規に作成されるゲートウェイ（既存ゲートウェイを削除して再作成する場合を含む）には新しいデフォルト値が適用されます。`--tcp-time-wait-timeout`フラグを用いてカスタムの`TIME_WAIT`値を設定しているゲートウェイには影響ありません。

影響有無:
影響は限定的であり、現時点での既存システム運用への直接的な影響はありません。
理由:
- この変更は2026年6月30日以降に段階的に適用される予定の将来のアナウンスメントであるため、現時点での既存リソースへの自動的な変更や即時的な影響はありません。
- 既存のCloud NATゲートウェイはデフォルト値が120秒のまま維持されるため、現在稼働中のサービスに影響はありません。
- お客様が明示的にカスタムの`TIME_WAIT`値を設定しているCloud NATゲートウェイにも影響はありません。
- 将来的に（2026年6月30日以降）新規にCloud NATゲートウェイを作成する場合、または既存のゲートウェイを削除して再作成する場合には、デフォルトの`TIME_WAIT`値が30秒に変更されます。これにより、特に大量の短命なTCP接続を扱うワークロードにおいて、ポート枯渇のリスクが低減され、リソース消費が改善される可能性があります。一方で、アプリケーションが長い`TIME_WAIT`時間を前提としている場合は、意図しない接続挙動が発生しないか将来的に注意が必要になる可能性があります。

対処方法:
現時点での具体的な対処は不要です。
- 2026年6月30日以降に新規Cloud NATゲートウェイをデプロイする際、または既存ゲートウェイを再作成する際には、デフォルトの`TIME_WAIT`値が30秒になることを認識してください。
- もし、デフォルトの30秒ではなく、より長い`TIME_WAIT`タイムアウト（例えば従来の120秒）が必要な場合は、ゲートウェイ作成時または更新時に`--tcp-time-wait-timeout`フラグを使用して明示的に値を指定することを検討してください。
- アプリケーションがTCP `TIME_WAIT`状態の短縮による影響を受ける可能性があるか、将来的に確認およびテストすることを推奨します。

用語説明:
- **Cloud NAT (Network Address Translation)**: Google Cloudのネットワークサービスの一つで、VPCネットワーク内のプライベートIPアドレスを持つ仮想マシンインスタンスが、インターネットなどの外部ネットワークと通信するための仲介を行います。これにより、インスタンスが外部と通信する際に単一の外部IPアドレスを使用し、セキュリティとIPアドレスの効率的な利用を実現します。
- **TCP `TIME_WAIT`**: TCP接続が正常に終了した後、その接続で使用されていたソケットが一定期間（通常は接続の最大セグメント寿命の2倍）保持される状態です。これは、遅延したパケットが新しい接続で誤って解釈されることを防ぐためのもので、TCPプロトコルにおける信頼性確保のための重要なメカニズムです。この状態の間、ポートは再利用できません。
- **ポート枯渇**: 多数の短期間のTCP接続が頻繁に発生するシステムにおいて、多くのソケットが`TIME_WAIT`状態にとどまることで、利用可能な発信元ポートが不足してしまう現象です。これにより、新しい接続を確立できなくなり、サービスに支障をきたす可能性があります。`TIME_WAIT`タイムアウトの短縮は、このポート枯渇のリスクを軽減する効果があります。
- **`--tcp-time-wait-timeout`**: `gcloud compute routers nat create`または`update`コマンドで使用されるオプションフラグで、Cloud NATゲートウェイのTCP `TIME_WAIT`タイムアウト値をカスタム設定するために利用します。デフォルト値の範囲内で、秒単位で値を指定できます。
    - Cloud NAT の構成の調整: [https://cloud.google.com/nat/docs/tune-nat-configuration](https://cloud.google.com/nat/docs/tune-nat-configuration)
    - Cloud NAT ゲートウェイの構成の変更: [https://cloud.google.com/nat/docs/tune-nat-configuration#change-conn-timeouts](https://cloud.google.com/nat/docs/tune-nat-configuration#change-conn-timeouts)
# Title: March 30, 2026 
Link: https://docs.cloud.google.com/release-notes#March_30_2026<br>
Google Cloudのリリースノートに基づく、貴社構築済みサービスへの影響調査結果を以下にご報告いたします。

---

# Cloud Logging
## Change
原文: For any new project that is created on or after March 30, 2026, if the project enables the Cloud Logging API, then Google Cloud Observability also enables the Telemetry API.

説明：2026年3月30日以降に新規作成されるGoogle Cloudプロジェクトにおいて、Cloud Logging APIを有効化した場合、同時にGoogle Cloud Observabilityの一部であるTelemetry APIも自動的に有効化されるようになります。これは将来的な新規プロジェクトに対する変更であり、既存プロジェクトには適用されません。

影響有無：**影響なし**。
この変更は、2026年3月30日以降に作成される「新規プロジェクト」が対象であり、かつ「Cloud Logging APIを有効化する場合」に適用されます。貴社で現在ご利用中の既存プロジェクトや、現在の運用に対して直接的な影響はありません。Telemetry APIの有効化は、Google Cloud Observabilityの機能強化に繋がるため、既存のサービス動作に悪影響を及ぼす可能性は低いと考えられます。

対処方法：なし。
将来的に新規プロジェクトを立ち上げる際に、この仕様を認識しておく程度で十分です。

用語説明：
*   **Cloud Logging API**: Google Cloudが提供する統合ログ管理サービスであるCloud Loggingに、プログラムからアクセスするためのAPIです。ログの書き込み、読み取り、エクスポート構成などに利用されます。
*   **Google Cloud Observability**: Google Cloudにおける監視、ロギング、トレースといった運用管理機能を提供する統合プラットフォームです。旧称はStackdriverです。
*   **Telemetry API**: Google Cloud Observabilityの一部として、各種テレメトリデータ（ログ、メトリクス、トレースなど）を収集し、サービスの状態を可視化するための基盤となるAPI群です。

---

# Cloud Monitoring
## Change
原文: For any new project that is created on or after March 30, 2026, if the project enables the Cloud Monitoring API, Telemetry API.

説明：2026年3月30日以降に新規作成されるGoogle Cloudプロジェクトにおいて、Cloud Monitoring APIを有効化した場合、Telemetry APIも自動的に有効化されるようになります。これは将来的な新規プロジェクトに対する変更であり、既存プロジェクトには適用されません。

影響有無：**影響なし**。
この変更は、2026年3月30日以降に作成される「新規プロジェクト」が対象であり、かつ「Cloud Monitoring APIを有効化する場合」に適用されます。貴社で現在ご利用中の既存プロジェクトや、現在の運用に対して直接的な影響はありません。Telemetry APIの有効化は、監視機能の強化に繋がるため、既存のサービス動作に悪影響を及ぼす可能性は低いと考えられます。

対処方法：なし。
将来的に新規プロジェクトを立ち上げる際に、この仕様を認識しておく程度で十分です。

用語説明：
*   **Cloud Monitoring API**: Google Cloudが提供する監視サービスであるCloud Monitoringに、プログラムからアクセスするためのAPIです。カスタムメトリクスの書き込み、アラートポリシーの設定、ダッシュボードの管理などに利用されます。
*   **Telemetry API**: Cloud Loggingの項目で説明済みです。

---

# Cloud SQL for PostgreSQL
## Breaking
原文: Vector assist (Preview) is temporarily disabled for all Cloud SQL for PostgreSQL instances.

説明：Cloud SQL for PostgreSQLのプレビュー機能である「Vector assist」が、すべてのCloud SQL for PostgreSQLインスタンスにおいて一時的に無効化されます。

影響有無：**影響あり（特定の条件の場合）**。
もし、貴社で構築済みのCloud SQL for PostgreSQLインスタンスにおいて、現在プレビュー機能の「Vector assist」を積極的に利用している、または利用を前提としたシステム開発や検証を進めている場合は、この機能が一時的に使用できなくなるため直接的な影響を受けます。
「Vector assist」機能を全く利用していない、または利用する計画がない場合は、直接的な影響はありません。

対処方法：
*   **「Vector assist」を現在利用中の場合、または利用を予定していた場合**:
    *   この機能に依存するワークロードがある場合は、その機能が利用できなくなるため、代替手段の検討、またはワークロードの一時的な停止・計画の見直しが必要です。
    *   無効化の期間が明示されていないため、今後のGoogle Cloudからのアナウンスに注意を払ってください。
    *   詳細な情報（機能の再開時期など）については、Google Cloudサポートへの問い合わせを推奨します。

用語説明：
*   **Cloud SQL for PostgreSQL**: Google Cloudが提供する、フルマネージドなPostgreSQLデータベースサービスです。データベースのプロビジョニング、パッチ適用、バックアップ、レプリケーションなどの運用管理がGoogle Cloudによって行われます。
*   **Vector assist**: Cloud SQL for PostgreSQLにおけるベクター埋め込みのサポートを強化するプレビュー機能です。機械学習モデルから生成されるベクターデータ（例：画像やテキストの埋め込み表現）をデータベース内で効率的に保存・検索するための機能であり、RAG（Retrieval Augmented Generation）などのAIアプリケーションでの利用が想定されます。
*   **Preview (プレビュー)**: Google Cloudの製品リリースステージの一つです。一般提供（GA: General Availability）前の段階であり、機能がまだ完全でなく、将来的に仕様変更される可能性や、提供が中止される可能性もあります。通常、本番環境での利用は推奨されません。
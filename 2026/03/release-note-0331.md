
# Title: March 30, 2026 
Link: https://docs.cloud.google.com/release-notes#March_30_2026<br>
Google Cloudインフラエンジニアとして、ご依頼のリリースノートについて調査しました。

## Cloud Logging
### Change
原文:
For any new project that is created on or after March 30, 2026, if the project enables the Cloud Logging API, then Google Cloud Observability also enables the Telemetry API.
[Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview)

説明:
2026年3月30日以降に新規作成されるGoogle Cloudプロジェクトにおいて、Cloud Logging APIが有効化されると、Google Cloud Observabilityの一部であるTelemetry APIも自動的に有効化されるようになります。

影響有無:
**影響なし**
現在ご利用中のGoogle Cloud Composer2環境は、既存のプロジェクトに構築されているため、この変更の対象外です。この変更は「2026年3月30日以降に作成される新規プロジェクト」にのみ適用されます。

対処方法:
既存の環境に対しては、特に必要な対処はありません。将来的に新規プロジェクトを立ち上げる際に、Cloud Logging APIを有効化するとTelemetry APIも有効になることを認識しておいてください。

用語説明:
*   **Cloud Logging API**: Google CloudのロギングサービスであるCloud Loggingに、プログラムからアクセスするためのAPIです。ログの書き込み、読み取り、フィルタリングなどが行えます。
*   **Google Cloud Observability**: Google Cloudにおける監視、ロギング、トレース、エラーレポート、プロファイリングなどを統合的に提供するサービスの総称で、以前はStackdriverとして知られていました。
*   **Telemetry API**: Google Cloud Observabilityの一部であり、ログ、メトリック、トレースといったテレメトリーデータを収集、処理、エクスポートするための基盤を提供するAPIです。これにより、異なるオブザーバビリティコンポーネント間でのデータ連携が円滑に行われます。

## Cloud Monitoring
### Change
原文:
For any new project that is created on or after March 30, 2026, if the project enables the Cloud Monitoring API, Telemetry API.

説明:
2026年3月30日以降に新規作成されるGoogle Cloudプロジェクトにおいて、Cloud Monitoring APIが有効化されると、Telemetry APIも自動的に有効化されるようになります。

影響有無:
**影響なし**
現在ご利用中のGoogle Cloud Composer2環境は、既存のプロジェクトに構築されているため、この変更の対象外です。この変更は「2026年3月30日以降に作成される新規プロジェクト」にのみ適用されます。

対処方法:
既存の環境に対しては、特に必要な対処はありません。将来的に新規プロジェクトを立ち上げる際に、Cloud Monitoring APIを有効化するとTelemetry APIも有効になることを認識しておいてください。

用語説明:
*   **Cloud Monitoring API**: Google Cloudの監視サービスであるCloud Monitoringに、プログラムからアクセスするためのAPIです。メトリックの収集、カスタムメトリックの作成、アラートポリシーの設定などが行えます。
*   **Telemetry API**: Google Cloud Observabilityの一部であり、ログ、メトリック、トレースといったテレメトリーデータを収集、処理、エクスポートするための基盤を提供するAPIです。これにより、異なるオブザーバビリティコンポーネント間でのデータ連携が円滑に行われます。
# Title: March 27, 2026 
Link: https://docs.cloud.google.com/release-notes#March_27_2026<br>
Google Cloudインフラエンジニアとして、お使いのGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) 環境への影響を調査し、以下の通りご報告いたします。

---

# Cloud Composer
## Announcement
原文: A new Cloud Composer release has started on March 27, 2026. Get ready for upcoming changes and features as we roll out the new release to all regions. This release is in progress at the moment. Listed changes and features might not be available in some regions yet.
説明: 2026年3月27日から、新しいCloud Composerのリリースが開始されたことを示すアナウンスです。新しい変更や機能が順次全リージョンに展開されており、一部のリージョンではまだ利用できない可能性があることを示しています。
影響有無: 影響なし。これは今後の変更の予告であり、現在のCloud Composer 2.7.1環境に直接的な動作変更を伴うものではありません。
対処方法: なし。今後のリリースノートに注視し、関連するアップデート情報に留意してください。

## Change
原文: New Airflow builds are available in Cloud Composer 3:
[Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-3.1.7-build.3
- composer-3-airflow-2.10.5-build.32 (default)
- composer-3-airflow-2.9.3-build.52
説明: Cloud Composer 3向けに、新しいApache Airflowビルド（バージョン3.1.7、2.10.5、2.9.3）が利用可能になりました。
影響有無: 影響なし。現在ご利用の環境はCloud Composer 2 (Composer version 2.7.1)であり、この変更はCloud Composer 3に関するものです。
対処方法: なし。
用語説明:
*   **Airflow builds (Airflowビルド):** Apache Airflowの特定のバージョンと、Google Cloud Composerによって提供される追加の最適化、修正、および依存関係を組み合わせた、実行可能なイメージのことです。Composer環境はこのビルドに基づいて構築されます。
*   **Cloud Composer 3:** Cloud Composerのメジャーバージョンの一つで、主にApache Airflow 2.x以降の新しいバージョンをサポートし、インフラストラクチャの最適化や新機能が導入されています。

## Deprecated
原文: The following Cloud Composer versions and builds have reached their end of support period: composer-3-airflow-2.9.3-build.19 and composer-2.12.0-*.
説明: 以下のCloud Composerバージョンおよびビルドがサポート終了期間に達しました: composer-3-airflow-2.9.3-build.19 および composer-2.12.0-*。
影響有無: 影響なし。現在ご利用の環境はCloud Composer 2 (Composer version 2.7.1)であり、今回のサポート終了対象リストには含まれていません。
対処方法: なし。ただし、現行のバージョンも将来的にはサポート終了となる可能性があるため、定期的なバージョンアップ計画を検討し、サポートされている最新のComposerバージョンへの移行を推奨します。
用語説明:
*   **End of support period (サポート終了期間):** 特定のソフトウェアバージョンや製品が、ベンダーからの公式な技術サポート、バグ修正、セキュリティパッチの提供を受けられなくなる期間のことです。サポート終了後は、セキュリティリスクや機能不全のリスクが高まるため、サポートされているバージョンへの移行が強く推奨されます。

## Change
原文: New images are available in Cloud Composer 2:
[images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
- composer-2.16.9-airflow-2.10.5 (default)
- composer-2.16.9-airflow-2.9.3
説明: Cloud Composer 2向けに新しいイメージ（composer-2.16.9-airflow-2.10.5およびcomposer-2.16.9-airflow-2.9.3）が利用可能になりました。
影響有無: 影響あり。現在ご利用のCloud Composer 2 (Composer version 2.7.1、Airflow version 2.7.3)環境において、より新しいAirflowバージョン（2.10.5, 2.9.3）へのアップデートパスが提供されます。現在のAirflowバージョン(2.7.3)よりも新しいバージョンが提供されているため、セキュリティパッチや新機能の恩恵を受けるために、アップデートを検討する良い機会となります。既存の環境に自動的に適用されるわけではないため、即座のBreaking Changeはありません。
対処方法: 環境の安定性とセキュリティを考慮し、新しいイメージへのアップグレードを検討してください。アップグレード前に、新しいAirflowバージョンとの互換性をDAGやカスタムプラグインで確認し、ステージング環境での十分なテストを実施することを推奨します。
用語説明:
*   **Cloud Composer 2 images (Cloud Composer 2 イメージ):** Cloud Composer 2環境を構築するために使用される事前設定済みの仮想マシンイメージです。これには特定のCloud ComposerバージョンとApache Airflowのバージョン、および関連する依存関係が含まれています。
*   **Airflow 2.10.5, Airflow 2.9.3:** Apache Airflowの特定のバージョン番号です。数値が高いほど新しいバージョンを示し、通常はバグ修正、セキュリティパッチ、パフォーマンス改善、新機能などが含まれます。

## Announcement
原文: Cloud Composer 2 environments can no longer be created in Melbourne (australia-southeast2). We're switching this region to supporting only Cloud Composer 3 environments. Existing Cloud Composer 2 environments in this region aren't affected by this change.
説明: メルボルン（australia-southeast2）リージョンでは、Cloud Composer 2環境の新規作成ができなくなり、Cloud Composer 3環境のみをサポートするようになるアナウンスです。既存のCloud Composer 2環境は影響を受けません。
影響有無: 影響なし。現在ご利用の環境は `australia-southeast2` リージョンで稼働しているとは限りません。また、この変更は「新規作成」に限定されており、既存の環境には影響しないため、現在の運用に直接的な影響はありません。
対処方法: なし。ただし、今後 `australia-southeast2` リージョンでCloud Composer 2環境を新規作成する計画がある場合は、Cloud Composer 3の利用を検討する必要があります。

## Change
原文: *(Airflow 3.1.7)* Starting from version composer-3-airflow-3.1.7-build.1, Airflow workers no longer have direct access to the Airflow database of your environment. This feature was announced previously and has finished gradually rolling out to all regions supported by Cloud Composer 3.
説明: Airflow 3.1.7以降のバージョン（composer-3-airflow-3.1.7-build.1から）では、Airflow workerがAirflowデータベースに直接アクセスできなくなる変更です。この変更はCloud Composer 3でサポートされているすべてのリージョンに段階的に展開が完了しました。
影響有無: 影響なし。現在ご利用の環境はCloud Composer 2 (Composer version 2.7.1)であり、この変更はCloud Composer 3の特定のAirflowバージョン（3.1.7）に関するものです。
対処方法: なし。
用語説明:
*   **Airflow worker (Airflowワーカー):** Apache Airflowにおいて、DAG（Directed Acyclic Graph）で定義されたタスクを実行するコンポーネントです。通常、複数のワーカーが並行してタスクを処理します。
*   **Airflow database (Airflowデータベース):** Apache Airflowのメタデータ（DAGの実行履歴、タスクの状態、接続情報など）を保存するデータベースです。

---

# Compute Engine
## Security
原文: A vulnerability (CVE-2026-23268) about CrackArmor was discovered and has been addressed. For more information, see the GCP-2026-015 security bulletin.
説明: CrackArmorに関する脆弱性（CVE-2026-23268）が発見され、修正されました。詳細はセキュリティ速報GCP-2026-015を参照してください。
影響有無: 影響なし。現在ご利用のサービスはCloud Composerであり、この脆弱性はCompute Engineに関するものです。Cloud Composer環境の基盤としてCompute Engineが利用されていますが、これはGoogle Cloudが管理する基盤レイヤーの脆弱性であり、既に修正済みとされています。ユーザー側で直接的な対処は不要です。
対処方法: なし。Google Cloudの責任範囲で修正済みです。ただし、関連するセキュリティ速報GCP-2026-015を確認し、詳細を把握することをお勧めします。
用語説明:
*   **CVE (Common Vulnerabilities and Exposures):** 既知のサイバーセキュリティの脆弱性や情報セキュリティの暴露を識別し、公開するための国際的な標準識別子システムです。
*   **CrackArmor:** このリリースノートで言及されている脆弱性に関連する特定の技術またはツールの名称です。詳細は提供されたセキュリティ速報で確認できます。
*   **Security bulletin (セキュリティ速報):** 特定の製品やサービスにおけるセキュリティ脆弱性とその対処法について、ベンダーが公開する公式の情報です。

# Title: July 28, 2025 
Link: https://cloud.google.com/release-notes#July_28_2025<br>
ご提示のリリースノートに基づき、お客様の環境 (Google Cloud Composer2, Composer version 2.7.1, Airflow version 2.7.3) への影響調査結果を以下にご報告いたします。

---

# Cloud Composer

## Fixed

原文: Fixed an issue that caused unexpected restarts of Airflow component workloads in the environment's cluster.

説明：
Cloud Composer環境内のクラスターで、Airflowコンポーネント（Webサーバー、スケジューラー、ワーカーなど）のワークロードが予期せず再起動する問題を修正しました。この修正により、環境の安定性が向上します。

影響有無：
間接的に影響あり。
お客様の現在のComposer 2.7.1環境で同様の予期せぬ再起動が発生している場合、この修正を含む新しいComposerバージョンへアップグレードすることで、安定性が向上する可能性があります。しかし、現在のバージョンではこの修正は適用されていません。

対処方法：
現在の環境でAirflowコンポーネントの予期せぬ再起動が頻繁に発生している場合、後述する新しいComposerイメージが提供されているため、そのバージョンへのアップグレードを検討してください。アップグレードにより本修正が適用され、安定性が向上する可能性があります。

用語説明：
*   **Airflow component workloads**: Apache Airflowの環境を構成する主要なプロセス群を指します。具体的には、DAGの実行を管理するScheduler、ユーザーインターフェースを提供するWebserver、タスクを実行するWorker（ExecutorによってKubernetesPodOperatorなど、具体的な実装は異なります）などが該当します。

---

## Fixed

原文: *(Cloud Composer 3)* The `DAGS_FOLDER` reserved environment variable now correctly points to the local directory where DAG files are stored.

説明：
Cloud Composer 3環境において、予約済みの環境変数 `DAGS_FOLDER` が、DAGファイルが格納されているローカルディレクトリを正しく指すように修正されました。これにより、`DAGS_FOLDER` を参照するスクリプトやカスタムコードが正しく動作するようになります。

影響有無：
影響なし。
お客様がご利用中の環境はCloud Composer 2 (Composer version 2.7.1) であるため、本修正は適用対象外です。

対処方法：
不要です。

---

## Changed

原文: New Airflow builds are available in Cloud Composer 3:
[Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-2.10.5-build.10 (default)
- composer-3-airflow-2.9.3-build.30

説明：
Cloud Composer 3向けに、Apache Airflowの新しいビルドイメージが利用可能になりました。デフォルトとして `composer-3-airflow-2.10.5-build.10` が提供され、`composer-3-airflow-2.9.3-build.30` も選択可能です。

影響有無：
影響なし。
お客様がご利用中の環境はCloud Composer 2 (Composer version 2.7.1) であるため、本変更は適用対象外です。

対処方法：
不要です。

---

## Changed

原文: New images are available in Cloud Composer 2:
[images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
- composer-2.13.8-airflow-2.10.5 (default)
- composer-2.13.8-airflow-2.9.3

説明：
Cloud Composer 2向けに、新しいComposerイメージが利用可能になりました。具体的には、Composerバージョン `2.13.8` をベースとし、Apache Airflowバージョン `2.10.5` (デフォルト) または `2.9.3` を含むイメージが提供されています。

影響有無：
影響あり。
お客様の環境 (Composer 2.7.1, Airflow 2.7.3) は、これらの新しいイメージ (Composer 2.13.8) よりも古いバージョンです。新しいイメージが提供されたことで、セキュリティパッチ、バグ修正、新機能を含む、より最新かつ安定した環境へのアップグレードパスが利用可能になりました。Airflowのバージョンも `2.7.3` から `2.9.3` または `2.10.5` へと大幅に更新されるため、DAGの互換性確認が必要になります。

対処方法：
現在の環境は引き続き動作しますが、後述のサポート終了の項目と合わせて、環境のアップグレード計画を早急に策定し、実行することを強く推奨します。アップグレードの際は、ターゲットとなる `composer-2.13.8` および `Airflow 2.9.3` または `2.10.5` のリリースノート（特に非互換性のある変更点）を確認し、既存のDAGs、カスタムプラグイン、PyPIパッケージなどへの影響を評価し、十分なテストを実施してください。

---

## Deprecated

原文: Cloud Composer version 2.8.6 has reached its end of support period.
[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support)

説明：
Cloud Composerバージョン 2.8.6がサポート終了期間に達しました。これは、Google Cloudからの公式なサポート（セキュリティパッチ、バグ修正、技術サポートなど）が提供されなくなることを意味します。

影響有無：
**重大な影響あり。**
お客様が現在ご利用中のComposerバージョンは `2.7.1` であり、これはサポート終了した `2.8.6` よりもさらに古いバージョンです。Google Cloud Composerのバージョンポリシーに基づくと、**Composer 2.7.1は既にサポート期間が終了しています（2024年4月23日にサポート終了済み）**。

サポート終了したバージョンを継続して使用することは、以下のような運用上の重大なリスクを伴います。
*   **セキュリティリスクの増大**: 新たなセキュリティ脆弱性が発見されても、修正パッチが提供されません。
*   **バグ修正の未提供**: 発生した問題に対する公式なバグ修正が提供されません。
*   **技術サポートの欠如**: 問題発生時にGoogle Cloudからの技術サポートを受けられない場合があります。
*   **将来的な機能互換性の問題**: 最新のGoogle Cloudサービスとの連携で問題が発生する可能性があります。

対処方法：
**直ちにCloud Composer環境のアップグレード計画を策定し、実行してください。** サポートが終了したバージョンは、運用上のリスクが非常に高いため、速やかにサポート対象の最新バージョン（例: 上記の `composer-2.13.8-airflow-2.10.5`）への移行を強く推奨します。

アップグレード作業においては、以下の点を特に注意して計画・実行してください。
1.  **アップグレードパスの確認**: Composerのバージョンアップは、段階的なアップグレードが必要な場合があります。公式ドキュメントで推奨されるアップグレードパスを確認してください。
2.  **非互換性のある変更の確認**: AirflowやComposerのメジャー・マイナーバージョンアップに伴う、既存のDAGs、カスタムプラグイン、環境変数、Pythonパッケージへの影響（破壊的変更など）を詳細に調査してください。
3.  **テスト計画**: アップグレード後の環境で、既存のDAGsが期待通りに動作することを確認するための詳細なテスト計画を策定し、実行してください。
4.  **ロールバック戦略**: 万が一問題が発生した場合に備え、ロールバック戦略を準備してください。

用語説明：
*   **End of Support (EOS)**: 製品やソフトウェアのバージョンに対するベンダーからの公式なサポートが終了する期限を指します。これには、セキュリティパッチの提供、バグ修正、技術サポート、および互換性保証などが含まれます。EOSを迎えたソフトウェアは、セキュリティリスクや運用リスクが高まるため、速やかにサポート対象のバージョンへ移行することが推奨されます。
# Title: July 25, 2025 
Link: https://cloud.google.com/release-notes#July_25_2025<br>
# Compute Engine

## Changed
原文: Hyperdisk Extreme is available in all regions and zones.
For more information, see About Hyperdisk Extreme.

[About Hyperdisk Extreme](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme)
説明: Hyperdisk Extreme が全てのGoogle Cloudリージョンおよびゾーンで利用可能になりました。これにより、特定のリージョンに限定されていた高性能ブロックストレージの提供範囲がグローバルに拡大されます。
影響有無: 影響なし。現在Hyperdisk Extremeは利用していません。将来的に高性能なストレージオプションが必要になった際の選択肢が広がりますが、既存のインフラ構成には変更を要しません。
対処方法: 不要。
用語説明:
*   **Hyperdisk Extreme**: Google Compute Engineが提供する最高性能のブロックストレージタイプです。非常に高いIOPS（Input/Output Operations Per Second）とスループットを実現し、超低レイテンシが求められるデータベースや分析ワークロードなどに最適です。

## Changed
原文: You can now resize Hyperdisk Balanced volumes twice within a 4-hour window. For more information, see Capacity changes.

[Capacity changes](https://cloud.google.com/compute/docs/disks/modify-hyperdisks#capacity_changes)
説明: Hyperdisk Balanced ボリュームの容量変更（リサイズ）操作が、4時間以内に2回まで実行できるようになりました。これにより、ストレージ容量の調整における柔軟性が向上します。
影響有無: 影響なし。現在Hyperdisk Balancedは利用していません。もし利用していたとしても、リサイズ操作の制限緩和は運用上の利便性向上であり、既存の動作に悪影響はありません。
対処方法: 不要。
用語説明:
*   **Hyperdisk Balanced**: Google Compute Engineが提供する汎用的なブロックストレージタイプです。パフォーマンスとコストのバランスが取れており、幅広いワークロードに適しています。

# Google Kubernetes Engine

## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

 - Version 1.33.2-gke.1111000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:

- 1.28.15-gke.2488000
- 1.29.15-gke.1656000
- 1.30.12-gke.1340000
- 1.31.10-gke.1034000
- 1.32.6-gke.1025000
- 1.33.2-gke.1240000

- The following versions are no longer available in the Extended channel:

- 1.28.15-gke.2303000
- 1.28.15-gke.2380000
- 1.28.15-gke.2428000
- 1.28.15-gke.2445000
- 1.28.15-gke.2475000
- 1.29.15-gke.1415000
- 1.29.15-gke.1493000
- 1.29.15-gke.1549000
- 1.29.15-gke.1594000
- 1.29.15-gke.1639000
- 1.30.12-gke.1168000
- 1.30.12-gke.1208000
- 1.30.12-gke.1246000
- 1.30.12-gke.1279000
- 1.30.12-gke.1320000
- 1.31.9-gke.1044001
- 1.31.9-gke.1119000
- 1.31.9-gke.1176000
- 1.31.9-gke.1218000
- 1.31.9-gke.1287000
- 1.32.4-gke.1415000
- 1.32.4-gke.1603000
- 1.32.4-gke.1698000
- 1.32.4-gke.1767000
- 1.33.1-gke.1107000
- 1.33.1-gke.1386000
- 1.33.1-gke.1584000
- 1.33.1-gke.1744000
- 1.33.2-gke.1043000

- Auto-upgrade targets are now available for the following minor versions:

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2456000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2456000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1607000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1333000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.10-gke.1021000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1013000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.2-gke.1111000 with this release.

- Version 1.33.2-gke.1111000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:

- 1.28.15-gke.2488000
- 1.29.15-gke.1656000
- 1.30.12-gke.1340000
- 1.31.10-gke.1034000
- 1.32.6-gke.1025000
- 1.33.2-gke.1240000

- The following versions are no longer available in the Extended channel:

- 1.28.15-gke.2303000
- 1.28.15-gke.2380000
- 1.28.15-gke.2428000
- 1.28.15-gke.2445000
- 1.28.15-gke.2475000
- 1.29.15-gke.1415000
- 1.29.15-gke.1493000
- 1.29.15-gke.1549000
- 1.29.15-gke.1594000
- 1.29.15-gke.1639000
- 1.30.12-gke.1168000
- 1.30.12-gke.1208000
- 1.30.12-gke.1246000
- 1.30.12-gke.1279000
- 1.30.12-gke.1320000
- 1.31.9-gke.1044001
- 1.31.9-gke.1119000
- 1.31.9-gke.1176000
- 1.31.9-gke.1218000
- 1.31.9-gke.1287000
- 1.32.4-gke.1415000
- 1.32.4-gke.1603000
- 1.32.4-gke.1698000
- 1.32.4-gke.1767000
- 1.33.1-gke.1107000
- 1.33.1-gke.1386000
- 1.33.1-gke.1584000
- 1.33.1-gke.1744000
- 1.33.2-gke.1043000

- Auto-upgrade targets are now available for the following minor versions:

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2456000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2456000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1607000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1333000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.10-gke.1021000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1013000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.2-gke.1111000 with this release.

[1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
- 1.28.15-gke.2488000
- 1.29.15-gke.1656000
- 1.30.12-gke.1340000
- 1.31.10-gke.1034000
- 1.32.6-gke.1025000
- 1.33.2-gke.1240000

[1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
[1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
[1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
[1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
- 1.28.15-gke.2303000
- 1.28.15-gke.2380000
- 1.28.15-gke.2428000
- 1.28.15-gke.2445000
- 1.28.15-gke.2475000
- 1.29.15-gke.1415000
- 1.29.15-gke.1493000
- 1.29.15-gke.1549000
- 1.29.15-gke.1594000
- 1.29.15-gke.1639000
- 1.30.12-gke.1168000
- 1.30.12-gke.1208000
- 1.30.12-gke.1246000
- 1.30.12-gke.1279000
- 1.30.12-gke.1320000
- 1.31.9-gke.1044001
- 1.31.9-gke.1119000
- 1.31.9-gke.1176000
- 1.31.9-gke.1218000
- 1.31.9-gke.1287000
- 1.32.4-gke.1415000
- 1.32.4-gke.1603000
- 1.32.4-gke.1698000
- 1.32.4-gke.1767000
- 1.33.1-gke.1107000
- 1.33.1-gke.1386000
- 1.33.1-gke.1584000
- 1.33.1-gke.1744000
- 1.33.2-gke.1043000

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2456000 with this release.

[1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2456000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1607000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1333000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.10-gke.1021000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1013000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.2-gke.1111000 with this release.

[1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.1607000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
[1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
[1.32.6-gke.
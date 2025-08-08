
# Title: August 06, 2025 
Link: https://cloud.google.com/release-notes#August_06_2025<br>
以下にGoogle Cloud GKEのリリースノートに関する影響調査結果を報告します。

---

# Google Kubernetes Engine
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
> Rollouts are already in progress when we publish the release notes, and can take
> multiple days to complete across all Google Cloud zones.
>
> - The following versions are now available in the Extended channel:
>
> - 1.28.15-gke.2488000
> - 1.28.15-gke.2527000
> - 1.29.15-gke.1656000
> - 1.29.15-gke.1713000
> - 1.30.12-gke.1390000
> - 1.31.11-gke.1002000
> - 1.32.6-gke.1096000
>
> - The following versions are no longer available in the Extended channel:
>
> - 1.28.15-gke.2461000
> - 1.28.15-gke.2507000
> - 1.29.15-gke.1614000
> - 1.29.15-gke.1686000
> - 1.30.12-gke.1340000
> - 1.31.10-gke.1034000
> - 1.32.6-gke.1025000
>
> - Auto-upgrade targets are now available for the following minor versions:
>
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2475000 with this release.
>
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2475000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1639000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1060000 with this release.
>
> - The following versions are now available in the Extended channel:
>
> - 1.28.15-gke.2488000
> - 1.28.15-gke.2527000
> - 1.29.15-gke.1656000
> - 1.29.15-gke.1713000
> - 1.30.12-gke.1390000
> - 1.31.11-gke.1002000
> - 1.32.6-gke.1096000
>
> - The following versions are no longer available in the Extended channel:
>
> - 1.28.15-gke.2461000
> - 1.28.15-gke.2507000
> - 1.29.15-gke.1614000
> - 1.29.15-gke.1686000
> - 1.30.12-gke.1340000
> - 1.31.10-gke.1034000
> - 1.32.6-gke.1025000
>
> - Auto-upgrade targets are now available for the following minor versions:
>
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2475000 with this release.
>
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2475000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1639000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1060000 with this release.
>
> - 1.28.15-gke.2488000
> - 1.28.15-gke.2527000
> - 1.29.15-gke.1656000
> - 1.29.15-gke.1713000
> - 1.30.12-gke.1390000
> - 1.31.11-gke.1002000
> - 1.32.6-gke.1096000
>
> [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
> [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
> [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
> [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
> [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
> [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
> [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
> - 1.28.15-gke.2461000
> - 1.28.15-gke.2507000
> - 1.29.15-gke.1614000
> - 1.29.15-gke.1686000
> - 1.30.12-gke.1340000
> - 1.31.10-gke.1034000
> - 1.32.6-gke.1025000
>
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2475000 with this release.
>
> [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
> [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2475000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1639000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1060000 with this release.
>
> [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
> [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
> [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
> [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
> [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)

説明：
Extendedチャネルにおいて、GKEの複数の新しいバージョン（1.28.15-gke.2488000、1.29.15-gke.1656000など）が利用可能になりました。同時に、いくつかの古いバージョン（1.28.15-gke.2461000、1.29.15-gke.1614000など）は利用できなくなりました。
また、自動アップグレードターゲットが更新され、Extendedチャネルで自動アップグレードが有効なクラスタは、マイナーバージョンアップグレードの場合、バージョン1.27から1.28.15-gke.2475000へアップグレードされます。パッチのみのアップグレードターゲットも更新され、既存のマイナーバージョン（1.28、1.29、1.30、1.31、1.32）からそれぞれの最新パッチバージョン（例: 1.28.15-gke.2475000、1.29.15-gke.1639000）へアップグレードされるよう設定されました。

影響有無：
**影響なし**
Google Cloud Composer2はマネージドサービスであり、その基盤となるGKEクラスタのバージョンはGoogleによって管理されます。現在のComposer 2.7.1がExtendedチャネルのGKEを使用しているかどうかは明示されていませんが、通常、ComposerはGoogleが互換性を検証した特定のGKEバージョンに固定され、自動的に更新されます。この変更はGKEクラスタの利用可能バージョンと自動アップグレードのターゲットに関するものであり、Composerユーザーが直接GKEのバージョン選択やアップグレードを操作するものではありません。

対処方法：
特段の対処は不要です。Composerのリリースノートやドキュメントで、基盤となるGKEバージョンの変更がアナウンスされた場合は、その内容を確認してください。

用語説明：
*   **Extendedチャネル**: GKEのリリースチャネルの一つで、より長期間サポートされるバージョンを提供するチャネルです。一般的に、新しい機能よりも安定性と長期サポートが重視されます。
*   **自動アップグレードターゲット**: GKEクラスタで自動アップグレードが有効になっている場合に、どのバージョンにアップグレードされるかの目標バージョンを指します。
*   **コントロールプレーン**: Kubernetesクラスタの制御層で、APIサーバー、スケジューラ、コントローラーマネージャなどが含まれます。
*   **ノード**: Kubernetesクラスタのワーカーマシンで、コンテナ化されたアプリケーションを実行します。
*   **パッチバージョンアップグレード**: Kubernetesバージョンの末尾の数字（例: 1.28.15 の `15`）の変更を伴うアップグレードで、主にバグ修正やセキュリティ修正を含みます。
*   **マイナーバージョンアップグレード**: Kubernetesバージョンの2番目の数字（例: 1.28.15 の `28`）の変更を伴うアップグレードで、新機能の追加やAPIの変更が含まれることがあります。

---

# Google Kubernetes Engine
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
> Rollouts are already in progress when we publish the release notes, and can take
> multiple days to complete across all Google Cloud zones.
>
> - The following versions are now available:
>
> - 1.30.14-gke.1011000
> - 1.31.11-gke.1064000
> - 1.32.7-gke.1016000
> - 1.33.3-gke.1136000
>
> - The following node versions are now available:
>
> - 1.28.15-gke.2527000
> - 1.29.15-gke.1713000
> - 1.30.14-gke.1011000
> - 1.31.11-gke.1064000
> - 1.32.7-gke.1016000
> - 1.33.3-gke.1136000
>
> - The following versions are no longer available:
>
> - 1.30.12-gke.1320000
> - 1.31.9-gke.1287000
> - 1.32.4-gke.1698000
> - 1.33.2-gke.4780000
>
> - Auto-upgrade targets are now available for the following minor versions:
>
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.32.6-gke.1013000 with this release.
>
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version 1.32.6-gke.1013000 with this release.
>
> - The following versions are now available:
>
> - 1.30.14-gke.1011000
> - 1.31.11-gke.1064000
> - 1.32.7-gke.1016000
> - 1.33.3-gke.1136000
>
> - The following node versions are now available:
>
> - 1.28.15-gke.2527000
> - 1.29.15-gke.1713000
> - 1.30.14-gke.1011000
> - 1.31.11-gke.1064000
> - 1.32.7-gke.1016000
> - 1.33.3-gke.1136000
>
> - The following versions are no longer available:
>
> - 1.30.12-gke.1320000
> - 1.31.9-gke.1287000
> - 1.32.4-gke.1698000
> - 1.33.2-gke.4780000
>
> - Auto-upgrade targets are now available for the following minor versions:
>
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.32.6-gke.1013000 with this release.
>
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version 1.32.6-gke.1013000 with this release.
>
> - 1.30.14-gke.1011000
> - 1.31.11-gke.1064000
> - 1.32.7-gke.1016000
> - 1.33.3-gke.1136000
>
> [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
> [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
> [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
> [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
> - 1.28.15-gke.2527000
> - 1.29.15-gke.1713000
> - 1.30.14-gke.1011000
> - 1.31.11-gke.1064000
> - 1.32.7-gke.1016000
> - 1.33.3-gke.1136000
>
> [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
> [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
> [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
> [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
> [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
> [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
> - 1.30.12-gke.1320000
> - 1.31.9-gke.1287000
> - 1.32.4-gke.1698000
> - 1.33.2-gke.4780000
>
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.12-gke.1372000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.31.10-gke.1067000 with this release.
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.32.6-gke.1013000 with this release.
>
> [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
> [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
> [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
> [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
> - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.12-gke.137
# Title: August 05, 2025 
Link: https://cloud.google.com/release-notes#August_05_2025<br>
# Compute Engine
## Deprecated
原文: The Compute Engine feature that deploys containers on VMs during VM creation is deprecated. For more information about the alternative solutions for running containers on VMs and MIGs, see Compute Engine container startup agent deprecation.
説明: Compute Engineの仮想マシン（VM）作成時にコンテナをデプロイする機能が非推奨になりました。この機能は、VM起動時に指定されたコンテナイメージを実行するためのエージェントを利用していました。今後は、Container-Optimized OS、Google Kubernetes Engine (GKE)、Cloud Run、またはCompute Engine上で手動でコンテナ環境を構築するなどの代替ソリューションへの移行が推奨されます。
影響有無: なし。本機能を利用していない場合は影響ありません。利用している場合は、非推奨化により将来的にサポートが終了する可能性があるため、代替ソリューションへの移行計画が必要です。
**Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響:** ComposerはGKE上で動作するマネージドサービスであり、この機能は通常利用しません。直接的な影響はありません。
対処方法: 当該機能を利用している場合は、Compute Engine container startup agent deprecationに記載されている代替手段への移行を検討してください。
用語説明:
*   **Compute Engine container startup agent**: Compute Engine VMの起動時にコンテナイメージを実行するために使用されていた、VMのOSレベルで動作するエージェントです。
*   **Container-Optimized OS (COS)**: Googleが提供する、コンテナ実行に最適化されたVMイメージです。Dockerなどのコンテナランタイムがプリインストールされています。
*   **Managed Instance Groups (MIGs)**: 複数のVMインスタンスをグループ化し、自動スケーリングや自動修復機能を提供するCompute Engineの機能です。

# Google Kubernetes Engine
## Fixed
原文: A fix is available for an issue in which the Compute Engine Persistent Disk CSI driver failed with an `invalid cpuString` error on GKE nodes that used custom machine types. This issue prevented successful attachment and mounting of Persistent Disk volumes on affected nodes. The fix is available in the following GKE versions:
- 1.31.10-gke.1034000 and later
- 1.32.4-gke.1698000 and later
- 1.33.1-gke.1386000 and later
説明: カスタムマシンタイプを使用するGKEノードで、Compute Engine Persistent Disk CSIドライバーが`invalid cpuString`エラーで失敗し、Persistent Diskボリュームの接続とマウントができない問題が修正されました。この修正は、特定のGKEバージョン（1.31.10-gke.1034000以降、1.32.4-gke.1698000以降、1.33.1-gke.1386000以降）で利用可能です。
影響有無: あり（限定的）。GKEクラスタでカスタムマシンタイプを使用しており、かつPersistent Diskの接続・マウントに関するエラーが発生していた場合に影響します。該当バージョンにアップグレードすることで問題が解消されます。影響がない場合は対処不要です。
**Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響:** Composer 2はGKE上に構築されています。もしComposer環境のノードプールでカスタムマシンタイプを使用しており、GKEバージョンが修正前のバージョンで上記の問題が発生している場合は、間接的に影響を受ける可能性があります。ただし、Composerはマネージドサービスであるため、GKEのバージョンアップグレードはGoogleによって管理されます。ユーザーが直接GKEクラスタをアップグレードする必要はありません。
対処方法: GKEクラスタでカスタムマシンタイプを使用しており、上記のエラーが発生している場合は、GKEクラスタを修正が含まれるバージョン（1.31.10-gke.1034000以降、1.32.4-gke.1698000以降、1.33.1-gke.1386000以降）にアップグレードすることを検討してください。
用語説明:
*   **Persistent Disk CSI driver**: GKEクラスタがCompute Engine Persistent Diskを動的にプロビジョニング、アタッチ、マウントするために使用するContainer Storage Interface (CSI) ドライバです。
*   **カスタムマシンタイプ**: Compute Engineで提供される、CPUとメモリのコア数をユーザーが自由に指定できるVMインスタンスタイプです。標準のマシンタイプよりも柔軟な構成が可能です。
*   **`invalid cpuString` error**: CPUに関する不正な文字列が原因で発生するエラーで、今回の場合はPersistent Disk CSIドライバがCPU情報を正しく解析できなかったことに起因していました。

# Google SecOps
## Feature
原文: **New YARA-L features**
The following capabilities have been added to YARA-L 2.0 to enhance search precision, data analysis, and investigative workflows:
- **Conditions in UDM search and dashboards**
You can now filter aggregates defined in the `outcome` section using the new `condition` clause. This gives you more precise control over your results and supports more targeted investigations.
- New functionality includes support for `OR` and `n` of `[a, b, c.. z]` expressions.
- General availability for search and dashboards.
- **Deduplicate events in searches and dashboards**
The new `dedup` section lets you remove duplicate events after the `match` clause in both standard UDM searches and YARA-L 2.0 queries.
General availability for search and dashboards.
- **Use metrics functions in UDM searches**
You can now apply `metrics` functions in the `outcome` section of your search to access aggregated historical data directly in your search queries.
- Uses the same syntax as `metrics` in rules.
- General availability for search.
- **Increased limits for array and array_distinct**
The element limit for `array` and `array_distinct` aggregation functions in YARA-L has increased from 25 to 1,000.
- General availability for search and dashboards.
- Private preview for rules.
- **Restrict search results using limit**
The `limit` keyword now lets you restrict the number of results returned by a search. Use this to quickly preview data, optimize performance, or focus on a subset of results.
General availability for search and dashboards.
- **`earliest`** and **`latest`** **timestamps**
New `earliest` and `latest` timestamps let you extract the time range of your data (within microseconds) during aggregation.
General availability for search.
- **Layer aggregations and analytics across multi-stage queries**
Recent updates to multi-stage queries let you:
- Layer aggregations and data statistical functions. Calculate baselines, deviations, and trends across multiple stages of data processing.
- Conduct joins both within and across stages.
Private preview for search and dashboards. Contact your Google SecOps representative to enroll.
- **Join events, the entity graph, and data tables**
You can now perform Inner joins between events, the entity graph, and data tables. These queries require a `match` clause for these joins and return results as statistics.
Private preview for search and dashboards. Contact your Google SecOps representative to enroll.
説明: Google SecOpsの脅威検知ルール言語であるYARA-L 2.0に、検索精度、データ分析、および調査ワークフローを強化する多数の新機能が追加されました。これには、UDM検索およびダッシュボードでの条件句 (`condition`)、重複イベントの除去 (`dedup`)、メトリクス関数の利用、`array`および`array_distinct`集約関数の要素数上限の増加（25から1,000へ）、検索結果の制限 (`limit`)、`earliest`/`latest`タイムスタンプの利用、多段階クエリでの集約と分析の層化、イベント、エンティティグラフ、データテーブル間の結合機能などが含まれます。
影響有無: なし。これらの機能は追加されたものであり、既存のGoogle SecOpsの動作や設定に影響を与えるものではありません。新機能を活用することで、より高度なセキュリティ分析が可能になります。
**Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響:** 直接的な関連はありません。
対処方法: 不要。必要に応じて、追加された新機能を利用してセキュリティ分析を強化することを検討してください。プライベートプレビューの機能については、Google SecOps担当者にお問い合わせください。
用語説明:
*   **YARA-L**: Google SecOpsが提供する、脅威検知ルールを記述するための言語です。
*   **UDM (Unified Data Model)**: ログデータを標準化された共通形式で表現するためのデータモデルです。
*   **エンティティグラフ**: セキュリティイベント内のエンティティ（ユーザー、IPアドレス、デバイスなど）間の関係性を可視化し、調査を支援する機能です。
*   **集約関数**: データの集合に対して計算を行い、単一の結果を返す関数（例: COUNT, SUM, AVGなど）です。

# Google SecOps SIEM
## Feature
原文: **New YARA-L features**
The following capabilities have been added to YARA-L 2.0 to enhance search precision, data analysis, and investigative workflows:
- **Conditions in UDM search and dashboards**
You can now filter aggregates defined in the `outcome` section using the new `condition` clause. This gives you more precise control over your results and supports more targeted investigations.
- New functionality includes support for `OR` and `n` of `[a, b, c.. z]` expressions.
- General availability for search and dashboards.
- **Deduplicate events in searches and dashboards**
The new `dedup` section lets you remove duplicate events after the `match` clause in both standard UDM searches and YARA-L 2.0 queries.
General availability for search and dashboards.
- **Use metrics functions in UDM searches**
You can now apply `metrics` functions in the `outcome` section of your search to access aggregated historical data directly in your search queries.
- Uses the same syntax as `metrics` in rules.
- General availability for search.
- **Increased limits for array and array_distinct**
The element limit for `array` and `array_distinct` aggregation functions in YARA-L has increased from 25 to 1,000.
- General availability for search and dashboards.
- Private preview for rules.
- **Restrict search results using limit**
The `limit` keyword now lets you restrict the number of results returned by a search. Use this to quickly preview data, optimize performance, or focus on a subset of results.
General availability for search and dashboards.
- **`earliest`** and **`latest`** **timestamps**
New `earliest` and `latest` timestamps let you extract the time range of your data (within microseconds) during aggregation.
General availability for search.
- **Layer aggregations and analytics across multi-stage queries**
Recent updates to multi-stage queries let you:
- Layer aggregations and data statistical functions. Calculate baselines, deviations, and trends across multiple stages of data processing.
- Conduct joins both within and across stages.
Private preview for search and dashboards. Contact your Google SecOps representative to enroll.
- **Join events, the entity graph, and data tables**
You can now perform Inner joins between events, the entity graph, and data tables. These queries require a `match` clause for these joins and return results as statistics.
Private preview for search and dashboards. Contact your Google SecOps representative to enroll.
説明: Google SecOps SIEMの脅威検知ルール言語であるYARA-L 2.0に、検索精度、データ分析、および調査ワークフローを強化する多数の新機能が追加されました。これには、UDM検索およびダッシュボードでの条件句 (`condition`)、重複イベントの除去 (`dedup`)、メトリクス関数の利用、`array`および`array_distinct`集約関数の要素数上限の増加（25から1,000へ）、検索結果の制限 (`limit`)、`earliest`/`latest`タイムスタンプの利用、多段階クエリでの集約と分析の層化、イベント、エンティティグラフ、データテーブル間の結合機能などが含まれます。この内容はGoogle SecOpsのリリースノートと同一です。
影響有無: なし。これらの機能は追加されたものであり、既存のGoogle SecOps SIEMの動作や設定に影響を与えるものではありません。新機能を活用することで、より高度なセキュリティ分析が可能になります。
**Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響:** 直接的な関連はありません。
対処方法: 不要。必要に応じて、追加された新機能を利用してセキュリティ分析を強化することを検討してください。プライベートプレビューの機能については、Google SecOps担当者にお問い合わせください。
用語説明:
*   **SIEM (Security Information and Event Management)**: セキュリティ関連のログやイベントを収集、分析、管理し、脅威の検出や対応を支援するシステムです。
*   **YARA-L**: Google SecOpsが提供する、脅威検知ルールを記述するための言語です。
*   **UDM (Unified Data Model)**: ログデータを標準化された共通形式で表現するためのデータモデルです。

# Spanner
## Feature
原文: Columnar engine for Spanner is now in Preview. Columnar engine is a storage technique used with analytics queries to speed up scans. Spanner columnar engine accelerates analytical query performance on live operational data by up to 200 times without affecting transaction workloads. This eliminates the need for ETL into separate data warehouses while maintaining strong consistency. For more information, see the Columnar engine for Spanner overview.
説明: Spannerの「Columnar engine」がプレビュー版として利用可能になりました。これは、分析クエリのスキャンを高速化するためのストレージ技術です。このエンジンは、ライブの運用データに対する分析クエリのパフォーマンスを最大200倍高速化し、トランザクションワークロードには影響を与えません。これにより、データウェアハウスへのETL（抽出、変換、ロード）が不要になり、強力な整合性を保ちつつ分析が可能になります。
影響有無: なし。新機能の追加であり、既存のSpannerインスタンスやクエリに直接的な影響はありません。プレビュー機能のため、利用する場合は明示的に有効化が必要です。
**Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響:** 直接的な関連はありません。
対処方法: 不要。Spannerで大規模な分析クエリを実行しており、パフォーマンス改善を検討している場合は、本機能のプレビュー版利用を検討してください。
用語説明:
*   **Columnar engine (カラムナーエンジン)**: データを列（カラム）ごとに格納するストレージ方式です。行ごとに格納する方式（行指向）と比較して、特定の列に対する集計処理やスキャンが高速になるため、分析ワークロードに適しています。
*   **分析クエリ**: 大量のデータを集計、分析し、傾向やパターンを発見するためのクエリです。
*   **トランザクションワークロード**: 短い時間で頻繁にデータを読み書きする、OLTP（Online Transaction Processing）のようなワークロードです。
*   **ETL (Extract, Transform, Load)**: データをあるシステムから抽出し、必要に応じて変換し、別のシステム（通常はデータウェアハウス）にロードするプロセスです。

# Vertex AI Workbench
## Feature
原文: Generally available: You can consume reservations with Vertex AI Workbench instances. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your jobs have the necessary resources to run. For more information, see Use reservations with Vertex AI Workbench instances.
説明: Vertex AI Workbenchインスタンスで、Compute Engineの予約（Reservations）を利用できるようになりました。これは一般提供（GA）された機能です。Compute Engineのゾーンリソース予約を利用することで、Vertex AI Workbenchのジョブが必要なリソースを確保できる保証レベルが高まります。
影響有無: なし。新機能の一般提供であり、既存のVertex AI Workbenchの利用に直接的な影響はありません。リソース確保の課題を抱えている場合に、この機能を利用することでメリットが得られます。
**Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響:** 直接的な関連はありません。
対処方法: 不要。Vertex AI Workbenchインスタンスの起動時にリソース不足によるエラーが頻繁に発生する場合、または特定の時間帯に確実にリソースを確保したい場合に、予約の利用を検討してください。
用語説明:
*   **Vertex AI Workbench**: 機械学習の開発環境を提供するGoogle Cloudのサービスです。Jupyter Notebookなどのツールをホストします。
*   **Compute Engine Reservations**: 特定のVMインスタンスタイプやリソースを、指定したゾーンで事前に予約しておく機能です。これにより、リソースが必要な時に確実に利用できる保証を得られます。
*   **ゾーンリソース**: 特定のGoogle Cloudゾーン（例: us-central1-a）に限定されたCompute Engineのリソースです。
# Title: August 04, 2025 
Link: https://cloud.google.com/release-notes#August_04_2025<br>
# Apigee X
## Announcement
原文: On August 4, 2025, we released an updated version of Apigee (1-15-0-apigee-8).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.
説明: Apigeeの新しいバージョン `1-15-0-apigee-8` がリリースされました。このリリースの展開は本日開始され、すべてのGoogle Cloudゾーンで完了するには4営業日以上かかる可能性があります。展開が完了するまで、お客様のインスタンスでは新機能や修正が利用できない場合があります。
影響有無: 軽微な影響あり。
ApigeeのバージョンアップグレードはGoogle Cloudによって管理されるため、お客様側で直接的な操作は不要です。ただし、ロールアウト期間中はゾーンによって適用されるバージョンが異なるため、新機能や修正が利用できるようになるまでにタイムラグが発生する可能性があります。この期間中に新機能を利用したい場合や、特定の修正が適用されていることを確認したい場合は注意が必要です。
対処方法:
ロールアウト期間中は、特定の機能や修正が利用可能かどうかをシステムの状態やリリースノートで確認してください。緊急の修正がこのリリースに含まれている場合、適用されるまで待機する必要があります。
用語説明:
*   **ロールアウト (Rollout)**: ソフトウェアの新しいバージョンや機能が、段階的にシステム全体に展開されていくプロセスのこと。
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォーム。APIの設計、セキュリティ、分析、モニタリングなど、APIライフサイクル全体を管理します。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **435620966** | **Fixed a regression that occurred when upgrading from ASM 1.22 to 1.23 that resulted in 503 errors.** |
説明: ASM 1.22から1.23へのアップグレード時に発生し、503エラーを引き起こしていた回帰バグが修正されました。
影響有無: 利用状況によって影響あり。
お客様の環境でApigeeがASM (Anthos Service Mesh) 1.22から1.23へアップグレードする際に503エラーが発生していた場合、この修正により問題が解決されます。現在ASM 1.22またはそれ以前のバージョンを利用しており、将来的に1.23へのアップグレードを計画している場合は、この修正の恩恵を受けられます。
対処方法:
現在ASM 1.22から1.23へのアップグレードパスで503エラーに遭遇している場合は、今回のApigeeのバージョンアップグレードにより問題が解消されるか確認してください。問題が解消されない場合は、Google Cloudサポートにお問い合わせください。
用語説明:
*   **ASM (Anthos Service Mesh)**: Anthosの一部として提供されるマネージドサービスメッシュ。サービス間の通信を制御・監視し、信頼性、セキュリティ、オブザーバビリティを向上させます。Apigeeと連携して利用されることがあります。
*   **回帰バグ (Regression Bug)**: 以前のバージョンでは正常に動作していた機能が、新しいバージョンの変更によって再び動作しなくなるバグ。
*   **503エラー (Service Unavailable)**: HTTPステータスコードの一つで、サーバーがリクエストを処理できないことを示します。一時的な過負荷やメンテナンスなどで発生することがあります。

# BigQuery
## Libraries
### Java
原文:
A weekly digest of client library updates from across the Cloud SDK.
**Changes for google-cloud-bigquery**
[google-cloud-bigquery](https://github.com/googleapis/java-bigquery)
[2.54.0](https://github.com/googleapis/java-bigquery/compare/v2.53.0...v2.54.0)
- **bigquery:** Add OpenTelemetry Samples (#3899) (e3d9ed9)
- **bigquery:** Add otel metrics to request headers (#3900) (4071e4c)
- update dependency com.google.cloud:google-cloud-bigquerystorage-bom to v3.16.1 (#3912)
- Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.70.0 (#3890)
- Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250706-2.0.0 (#3910)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 (#3901)
- Update dependency io.opentelemetry:opentelemetry-api to v1.52.0 (#3902)
- Update dependency io.opentelemetry:opentelemetry-bom to v1.52.0 (#3903)
- Update dependency io.opentelemetry:opentelemetry-context to v1.52.0 (#3904)
- Update dependency io.opentelemetry:opentelemetry-exporter-logging to v1.52.0 (#3905)
説明:
BigQueryのJavaクライアントライブラリ `google-cloud-bigquery` がバージョン `2.54.0` にアップデートされました。主な変更点は以下の通りです。
*   OpenTelemetryのサンプルとメトリクスが追加され、リクエストヘッダーにOpenTelemetryメトリクスが含められるようになりました。これにより、BigQuery操作のトレーシングとオブザーバビリティが向上します。
*   各種依存ライブラリが最新バージョンに更新されました。
影響有無: なし。
お客様のシステムではJavaアプリケーションは利用されていません。また、Google Cloud Composer (Pythonベース) はこのJavaライブラリを直接使用しないため、影響はありません。JavaアプリケーションでBigQueryクライアントライブラリを利用している場合は、このアップデートによってOpenTelemetryを利用したトレースやメトリクス収集が可能になります。
対処方法: なし。
用語説明:
*   **クライアントライブラリ (Client Library)**: プログラミング言語ごとに提供される、Google Cloudサービスと対話するためのSDK（ソフトウェア開発キット）の一部。開発者はこれを利用して簡単にサービスを操作できます。
*   **OpenTelemetry**: 分散トレーシング、メトリクス、ログ収集のためのオープンソースのオブザーバビリティフレームワーク。アプリケーションの振る舞いを監視し、問題の特定やパフォーマンス分析に役立ちます。
*   **メトリクス (Metrics)**: システムのパフォーマンスや状態を数値で表現したデータ。CPU使用率、メモリ使用量、リクエスト数など。
*   **トレーシング (Tracing)**: 分散システムにおけるリクエストのライフサイクルを追跡し、各サービスでの処理時間やエラーを可視化する仕組み。

# Cloud Logging
## Libraries
### Java
原文:
A weekly digest of client library updates from across the Cloud SDK.
**Changes for google-cloud-logging**
[google-cloud-logging](https://github.com/googleapis/java-logging)
[3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 (6a268f8)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 (#1834) (2e46f6e)
説明:
Cloud LoggingのJavaクライアントライブラリ `google-cloud-logging` がバージョン `3.23.1` にアップデートされました。主な変更点は以下の通りです。
*   Javaコードジェネレータ (`gapic-generator-java`) がバージョン `2.60.2` に更新されました。
*   依存ライブラリ `sdk-platform-java-config` がバージョン `3.50.2` に更新されました。
影響有無: なし。
お客様のシステムではJavaアプリケーションは利用されていません。また、Google Cloud Composer (Pythonベース) はこのJavaライブラリを直接使用しないため、影響はありません。
対処方法: なし。
用語説明:
*   **GAPIC (Google API Client Libraries)**: GoogleのAPIクライアントライブラリを生成するためのフレームワーク。多くのGoogle CloudクライアントライブラリはGAPICによって自動生成されています。
*   **コードジェネレータ (Code Generator)**: API定義などから、特定のプログラミング言語のコードを自動的に生成するツール。

# Pub/Sub
## Libraries
### Go
原文:
A weekly digest of client library updates from across the Cloud SDK.
**Changes for pubsub/apiv1**
[pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)
[1.50.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.49.0...pubsub/v1.50.0)
- **pubsub/v2:** Add new v2 library (#12218) (c798f62)
- **pubsub:** Update google.golang.org/api to 0.229.0 (3319672)
- **pubsub:** Add docs comment to MaxOutstandingBytes (#12601) (76ddb34)
説明:
Pub/SubのGoクライアントライブラリ `pubsub/apiv1` がバージョン `1.50.0` にアップデートされました。主な変更点は以下の通りです。
*   新しいv2ライブラリが追加されました。これは将来的なAPI拡張に対応するための準備です。
*   依存ライブラリ `google.golang.org/api` が更新されました。
*   `MaxOutstandingBytes` フィールドにドキュメントコメントが追加されました。
影響有無: なし。
お客様のシステムではGoアプリケーションは利用されていません。Google Cloud Composer (Pythonベース) はこのGoライブラリを直接使用しないため、影響はありません。
対処方法: なし。
用語説明:
*   **v2ライブラリ (v2 library)**: APIの新しいメジャーバージョンに対応するライブラリ。通常、APIの大きな変更や改善が含まれます。

### Java
原文:
A weekly digest of client library updates from across the Cloud SDK.
**Changes for google-cloud-pubsub**
[google-cloud-pubsub](https://github.com/googleapis/java-pubsub)
[1.141.1](https://github.com/googleapis/java-pubsub/compare/v1.141.0...v1.141.1)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 (7afae21)
- Remove element_count_limit and request_byte_limit from pubsub_gapic.yaml (7afae21)
- Update dependency com.google.cloud:google-cloud-bigquery to v2.53.0 (#2489)
- Update dependency com.google.cloud:google-cloud-core to v2.58.2 (#2493)
- Update dependency com.google.cloud:google-cloud-storage to v2.53.3 (#2486)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 (#2494)
- Update dependency org.xerial.snappy:snappy-java to v1.1.10.8 (#2492)
説明:
Pub/SubのJavaクライアントライブラリ `google-cloud-pubsub` がバージョン `1.141.1` にアップデートされました。主な変更点は以下の通りです。
*   Javaコードジェネレータ (`gapic-generator-java`) がバージョン `2.60.2` に更新されました。
*   内部設定ファイル `pubsub_gapic.yaml` から `element_count_limit` および `request_byte_limit` の項目が削除されました。これは内部的なAPI構成の変更であり、通常利用するAPIの振る舞いに直接的な影響はありません。
*   各種依存ライブラリが最新バージョンに更新されました。
影響有無: なし。
お客様のシステムではJavaアプリケーションは利用されていません。Google Cloud Composer (Pythonベース) はこのJavaライブラリを直接使用しないため、影響はありません。
対処方法: なし。

### Python
原文:
A weekly digest of client library updates from across the Cloud SDK.
**Changes for google-cloud-pubsub**
[google-cloud-pubsub](https://github.com/googleapis/python-pubsub)
[2.31.1](https://github.com/googleapis/python-pubsub/compare/v2.31.0...v2.31.1)
- Change Log Severities for Terminated Streams (#1433) (3a3aa79)
- Propagate Otel Context to Subscriber Callback if Provided (#1429) (b0f6f49)
説明:
Pub/SubのPythonクライアントライブラリ `google-cloud-pubsub` がバージョン `2.31.1` にアップデートされました。主な変更点は以下の通りです。
*   ストリームが終了した際のログレベルが変更されました。これにより、診断情報がより適切に記録される可能性があります。
*   サブスクライバーのコールバック関数にOpenTelemetryのコンテキストが伝播されるようになりました（提供されている場合）。これにより、OpenTelemetryを利用してPub/Subメッセージ処理のトレーシングをより詳細に行うことが可能になります。
影響有無: 影響あり。
お客様のGoogle Cloud Composer環境 (Airflow version 2.7.3) で、PythonOperatorなどを介して `google-cloud-pubsub` ライブラリを明示的に使用している場合、このライブラリのバージョンが更新されると影響を受ける可能性があります。
*   **ログレベルの変更**: ストリーム終了時のログ出力の重要度が変わるため、ログ監視やアラート設定に影響を与える可能性があります。より詳細なログが出力されることで、デバッグがしやすくなる一方で、ログ量が増加する可能性も考慮する必要があります。
*   **OpenTelemetryコンテキストの伝播**: OpenTelemetryを導入しており、Pub/Subメッセージの処理における分散トレーシングを強化したい場合に、この新機能を利用できます。既存のワークロードでOpenTelemetryを利用していない場合は、直接的な影響はありません。
対処方法:
1.  **ライブラリバージョンの確認**: Composer環境で実際に使用されている `google-cloud-pubsub` のバージョンを確認してください。`pip freeze` や `pip show google-cloud-pubsub` コマンドをComposer環境のターミナルやDAG内で実行することで確認できます。
2.  **OpenTelemetryの利用状況**: 現在OpenTelemetryによる分散トレーシングを導入しているか、または将来的に導入予定があるかを確認してください。もし導入している場合、この機能によってより詳細なトレーシングが可能になります。
3.  **ログ監視のレビュー**: ストリーム終了時のログレベル変更が、既存のログ監視システムやアラート設定に影響を与えないか確認してください。必要に応じて、ログフィルターやアラート条件を調整してください。
4.  **ライブラリのアップグレード検討**: 新機能（特にOpenTelemetry連携）の恩恵を受けたい場合や、ログの改善が必要な場合は、アプリケーションコードの依存関係として `google-cloud-pubsub==2.31.1` またはそれ以降のバージョンを指定し、ライブラリをアップグレードすることを検討してください。アップグレードの際は、事前にテスト環境での動作確認を推奨します。
用語説明:
*   **サブスクライバー (Subscriber)**: Pub/Subのサブスクリプションからメッセージを受信するアプリケーションやサービス。
*   **コールバック関数 (Callback Function)**: あるイベントが発生した際に自動的に呼び出される関数。Pub/Subのサブスクライバーでは、メッセージが受信された際にコールバック関数が実行され、メッセージ処理ロジックが記述されます。
*   **コンテキスト伝播 (Context Propagation)**: 分散システムにおいて、リクエストに関連するメタデータ（例：トレーシングID）を、サービス間で引き継いでいくメカニズム。これにより、リクエスト全体のフローを追跡できます。
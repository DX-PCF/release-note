
# Title: August 29, 2025 
Link: https://cloud.google.com/release-notes#August_29_2025<br>
インフラエンジニアとして、ご指定のリリースノートについて、製品への影響有無を調査し、以下の通りご回答いたします。

---

# Artifact Registry

## Changed

原文: The Container Analysis API now supports the option of returning partial results during region-down failure conditions when listing notes, listing occurrences, or generating vulnerability summaries. For more information, view the `returnPartialSuccess` parameter for the following requests:

- v1.projects.locations.notes.list
- v1.projects.locations.occurrences.getVulnerabilitySummary
- v1.projects.locations.occurrences.list
- v1.projects.notes.list
- v1.projects.occurrences.getVulnerabilitySummary
- v1.projects.occurrences.list
- v1beta1.projects.locations.notes.list
- v1beta1.projects.locations.occurrences.getVulnerabilitySummary
- v1beta1.projects.locations.occurrences.list
- v1beta1.projects.notes.list
- v1beta1.projects.occurrences.getVulnerabilitySummary
- v1beta1.projects.occurrences.list

[v1.projects.locations.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.notes/list)
[v1.projects.locations.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences/getVulnerabilitySummary)
[v1.projects.locations.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences/list)
[v1.projects.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes/list)
[v1.projects.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences/getVulnerabilitySummary)
[v1.projects.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences/list)
[v1beta1.projects.locations.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes/list)
[v1beta1.projects.locations.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/getVulnerabilitySummary)
[v1beta1.projects.locations.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/list)
[v1beta1.projects.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/list)
[v1beta1.projects.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.occurrences/getVulnerabilitySummary)
[v1beta1.projects.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/list)

説明：
Container Analysis APIにおいて、リージョン障害発生時にノートのリスト取得、オカレンスのリスト取得、または脆弱性サマリーの生成を行う際に、部分的な結果を返すオプションである`returnPartialSuccess`パラメータがサポートされるようになりました。これにより、障害時でも利用可能なデータの一部を受け取ることができるようになります。

影響有無：
影響なし。これはAPIの可用性を向上させるための機能追加であり、既存の動作は変更されません。明示的に`returnPartialSuccess`パラメータを使用しない限り、既存のシステムに影響はありません。障害発生時のAPIの応答性が向上し、運用上はプラスの影響が期待されます。

対処方法：
特になし。この新機能を利用したい場合は、API呼び出しに`returnPartialSuccess`パラメータを追加することを検討してください。

用語説明：
*   **Container Analysis API**: Google Cloud上のコンテナイメージの脆弱性やソフトウェア部品構成（SBOM）を分析し、セキュリティ情報を管理するためのAPI。Artifact Registryと連携し、保存されたコンテナイメージのセキュリティ状態を評価します。
*   **Notes (ノート)**: コンテナイメージに関連付けられたメタデータ（例: 脆弱性情報、ビルド情報、署名情報など）。
*   **Occurrences (オカレンス)**: 特定のイメージ内で発見されたノート（例: 特定の脆弱性）のインスタンス。
*   **Vulnerability Summary (脆弱性サマリー)**: 特定のイメージまたはプロジェクト全体の脆弱性の概要レポート。
*   **`returnPartialSuccess` パラメータ**: API呼び出しにおいて、リクエスト全体が成功しない場合でも、利用可能な部分的な結果を返すことを許可するためのパラメータ。分散システムで一部のノードが利用不能な場合に有用です。

---

# Google Kubernetes Engine

## Fixed

原文: A fix is available for an issue with Cloud Storage FUSE CSI driver that could cause Pod to be stuck during startup after a node restart event. Cloud Storage FUSE CSI driver now gracefully handles a node restart behavior.

The fix is available in the following GKE versions:

- 1.32.6-gke.1125000 and later
- 1.33.1-gke.1959000 and later

説明：
Cloud Storage FUSE CSIドライバにおける不具合が修正されました。この不具合は、GKEノードの再起動イベント後にPodが起動時にスタックする原因となっていました。修正により、Cloud Storage FUSE CSIドライバがノード再起動の挙動を適切に処理し、Podの起動が正常に行われるようになります。この修正は、指定されたGKEバージョン以降で利用可能です。

影響有無：
影響あり（ポジティブな影響）。
現在Cloud Storage FUSE CSIドライバを使用しており、かつGKEクラスタのバージョンが記載された修正バージョンよりも古い場合、この問題が発生する可能性があります。この修正により、システムの安定性と信頼性が向上します。

対処方法：
Cloud Storage FUSE CSIドライバを使用している場合は、GKEクラスタを記載された修正バージョン（1.32.6-gke.1125000以降、または1.33.1-gke.1959000以降）にアップグレードすることを強く推奨します。これにより、Podがスタックする問題が解消されます。

用語説明：
*   **Cloud Storage FUSE CSI driver**: Google Cloud StorageバケットをKubernetes PodにファイルシステムとしてマウントするためのContainer Storage Interface (CSI) ドライバ。これにより、アプリケーションは通常のファイルI/O操作でCloud Storageにアクセスできます。
*   **Pod**: Kubernetesでデプロイされる最小のデプロイ可能単位。1つ以上のコンテナを内包します。
*   **Node restart event**: GKEクラスタ内のワーカーノード（VMインスタンス）が再起動するイベント。メンテナンスや障害復旧などで発生します。
*   **CSI (Container Storage Interface)**: Kubernetesなどのコンテナオーケストレーションシステムが、様々なストレージシステムと連携するための標準インターフェース。

---

# Spanner

## Libraries

### Go

原文:
## Go
## Changes for spanner/admin/database/apiv1
[spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)
[1.84.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.83.0...spanner/v1.84.0)
- **spanner/adapter:** Add last field in AdaptMessageResponse for internal optimization usage (c574e28)
- **spanner/admin/database:** Proto changes for an internal api (eeb4b1f)
- **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` (ac4970b)
- **spanner:** Add Google Cloud standard otel attributes (#11652) (f59fcff)

[c574e28](https://github.com/googleapis/google-cloud-go/commit/c574e287f49cc1c3b069b35d95b98da2bc9b948f)
[eeb4b1f](https://github.com/googleapis/google-cloud-go/commit/eeb4b1fe8eb83b73ec31b0bd46e3704bdc0212c3)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[#11652](https://github.com/googleapis/google-cloud-go/issues/11652)
[f59fcff](https://github.com/googleapis/google-cloud-go/commit/f59fcfffdfcd01ef5b436b76fa83351e2b695920)
- **spanner:** Context cancel in traces in case of skipping trailers (#12635) (509dc90)
- **spanner:** Enforce only one resource header (#12618) (4e04b7e)
- **spanner:** Fix blind retry for ResourceExhausted (#12523) (f9b6e88)
- **spanner:** Remove stream wrapper for direct path check (#12622) (88a36cd)

[#12635](https://github.com/googleapis/google-cloud-go/issues/12635)
[509dc90](https://github.com/googleapis/google-cloud-go/commit/509dc90cd13061f8302d20451af1d9f7e186641f)
[#12618](https://github.com/googleapis/google-cloud-go/issues/12618)
[4e04b7e](https://github.com/googleapis/google-cloud-go/commit/4e04b7efd68a979837f78d94ac1dbc930c2e5efb)
[#12523](https://github.com/googleapis/google-cloud-go/issues/12523)
[f9b6e88](https://github.com/googleapis/google-cloud-go/commit/f9b6e88bd3fce735ea58f70e3a7634837886d393)
[#12622](https://github.com/googleapis/google-cloud-go/issues/12622)
[88a36cd](https://github.com/googleapis/google-cloud-go/commit/88a36cdfb7f7d1d265f45ed8795b6c08915fe183)
- **spanner:** A comment for enum value `OPTIMISTIC` in enum `ReadLockMode` is changed (ac4970b)
- **spanner:** A comment for enum value `PESSIMISTIC` in enum `ReadLockMode` is changed (ac4970b)
- **spanner:** A comment for enum value `READ_LOCK_MODE_UNSPECIFIED` in enum `ReadLockMode` is changed (ac4970b)
- **spanner:** A comment for field `commit_stats` in message `.google.spanner.v1.CommitResponse` is changed (ac4970b)
- **spanner:** A comment for field `exclude_txn_from_change_streams` in message `.google.spanner.v1.TransactionOptions` is changed (ac4970b)
- **spanner:** A comment for field `multiplexed_session_previous_transaction_id` in message `.google.spanner.v1.TransactionOptions` is changed (ac4970b)
- **spanner:** A comment for field `precommit_token` in message `.google.spanner.v1.CommitResponse` is changed (ac4970b)
- **spanner:** A comment for message `.google.spanner.v1.MultiplexedSessionPrecommitToken` is changed (ac4970b)
- **spanner:** A comment for message `.google.spanner.v1.TransactionOptions` is changed (ac4970b)

[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23)
[1.84.1](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.84.0...spanner/v1.84.1)
- **spanner:** Release 1.84.1 (#12663) (8b410ec)

[#12663](https://github.com/googleapis/google-cloud-go/issues/12663)
[8b410ec](https://github.com/googleapis/google-cloud-go/commit/8b410ec689591a591aecb46831f2f50706cb973f)
- **spanner:** Release 1.84.1 (#12665) (a1ce8c2)

[#12665](https://github.com/googleapis/google-cloud-go/issues/12665)
[a1ce8c2](https://github.com/googleapis/google-cloud-go/commit/a1ce8c26651e7a0ba4f1b20aba4c0fefbab0b972)
**DO NOT USE**
This version is retracted due to https://github.com/googleapis/google-cloud-go/issues/12659, use version >=v1.84.1

説明：
SpannerのGoクライアントライブラリがアップデートされ、内部最適化、内部APIのプロトコル変更、`CommitResponse`メッセージへの`snapshot_timestamp`フィールド追加、OpenTelemetry属性のサポート追加が行われました。また、トレース、リソースヘッダー、`ResourceExhausted`エラーに対するリトライ処理などの修正が含まれます。
特に重要な点として、バージョン`1.84.0`はバグにより使用が推奨されておらず（"DO NOT USE"）、`1.84.1`以降のバージョンを使用するように指示されています。

影響有無：
影響あり。
*   **Goクライアントライブラリの`1.84.0`を使用している場合、重大な問題があるため、早急に`1.84.1`以降のバージョンにアップグレードする必要があります。**
*   その他の変更は主に機能追加、改善、内部的な最適化であり、通常はアプリケーションコードの変更なしにアップグレードできます。ただし、`CommitResponse`に新しいフィールドが追加されているため、もしアプリケーションがこのレスポンス構造に厳密に依存している場合は確認が必要です。
*   OpenTelemetryとの連携強化は、監視体制の改善に役立ちます。

対処方法：
*   **Goクライアントライブラリのバージョンが`1.84.0`の場合は、速やかに`1.84.1`以降にアップグレードしてください。**
*   現在Spannerを使用しているGoアプリケーションでこれらのクライアントライブラリを使用している場合は、最新バージョンへのアップグレードを検討し、アプリケーションの動作テストを実施することを推奨します。

### Java

原文:
## Java
## Changes for google-cloud-spanner
[google-cloud-spanner](https://github.com/googleapis/java-spanner)
[6.98.0](https://github.com/googleapis/java-spanner/compare/v6.97.1...v6.98.0)
- Proto changes for an internal api (675e90b)
- **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` (675e90b)
- Support Exemplar (#3997) (fcf0a01)
- Use multiplex sessions for RW and Partition Ops (#3996) (a882204)

[675e90b](https://github.com/googleapis/java-spanner/commit/675e90b4582b4fc968118121e6c23ec98ee178e9)
[675e90b](https://github.com/googleapis/java-spanner/commit/675e90b4582b4fc968118121e6c23ec98ee178e9)
[#3997](https://github.com/googleapis/java-spanner/issues/3997)
[fcf0a01](https://github.com/googleapis/java-spanner/commit/fcf0a0182a33f229e865e4593635efaed34d6dac)
[#3996](https://github.com/googleapis/java-spanner/issues/3996)
[a882204](https://github.com/googleapis/java-spanner/commit/a882204e07a2084b228c14fb37ac53e4e33d0f59)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 (675e90b)

[675e90b](https://github.com/googleapis/java-spanner/commit/675e90b4582b4fc968118121e6c23ec98ee178e9)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 (#4004) (986c0e0)

[#4004](https://github.com/googleapis/java-spanner/issues/4004)
[986c0e0](https://github.com/googleapis/java-spanner/commit/986c0e07fddecd51cd310a9759ce1d41c1f5c657)
[6.98.1](https://github.com/googleapis/java-spanner/compare/v6.98.0...v6.98.1)
- Add missing span.end calls for AsyncTransactionManager (#4012) (1a4adb4)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 (8156ef3)

[#4012](https://github.com/googleapis/java-spanner/issues/4012)
[1a4adb4](https://github.com/googleapis/java-spanner/commit/1a4adb4d70c3a3822fa6bda93d689f2dae1835fa)
[8156ef3](https://github.com/googleapis/java-spanner/commit/8156ef31d93932c14f9fdd13c8c5e5b7ce370ba5)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 (#4013) (4e90c29)

[#4013](https://github.com/googleapis/java-spanner/issues/4013)
[4e90c29](https://github.com/googleapis/java-spanner/commit/4e90c29ce3447d14411368e45a39c7b0965cb40a)

説明：
SpannerのJavaクライアントライブラリがアップデートされ、内部APIのプロトコル変更、
# Title: August 28, 2025 
Link: https://cloud.google.com/release-notes#August_28_2025<br>
はい、承知いたしました。Google Cloudのリリースノートについて、製品ごとの影響有無、対処方法を調査し、ご回答します。

---

# Cloud Storage

## Changed

原文: Beginning October 31, 2025, if you set an object's `age` condition to a value of `0` when setting Object Lifecycle Management rules, the condition is satisfied at midnight UTC after the object is created, which helps reduce unintended data loss. To learn more about the `age` condition, see [Lifecycle conditions](https://cloud.google.com/storage/docs/lifecycle#conditions).

説明：
2025年10月31日より、Cloud Storageのオブジェクトライフサイクル管理ルールにおいて、オブジェクトの`age`条件を`0`に設定した場合の挙動が変更されます。これまではオブジェクト作成後すぐに条件が満たされる可能性がありましたが、この変更により、オブジェクトが作成された後の協定世界時（UTC）深夜0時に条件が満たされるようになります。この変更は、意図しないデータ削除（例えば、作成直後に`age:0`で削除されることを防ぐ）のリスクを低減することを目的としています。

影響有無：
**影響あり（将来的な変更）**

*   現在、Cloud Storageのオブジェクトライフサイクル管理ルールで`age`条件を`0`に設定している場合、2025年10月31日以降にその挙動が変わります。
*   この変更により、オブジェクト作成からUTC深夜0時までの間にライフサイクルルールが適用されなくなるため、特に短期間でオブジェクトの作成と削除を繰り返すようなワークロードにおいて、意図した挙動と異なる結果が生じる可能性があります。
*   Google Cloud Composer (Composer version 2.7.1) は、Cloud Storageを直接操作することが多いため、Composerのワークフロー内でCloud Storageのライフサイクル管理ルールが重要な役割を果たしている場合は、将来的な影響を考慮する必要があります。

対処方法：
*   **現時点では対応不要です。** 変更が適用されるのは2025年10月31日以降です。
*   2025年10月31日までに、現在利用しているCloud Storageのライフサイクル管理ルールに`age:0`の条件が含まれていないか確認してください。
*   もし`age:0`を使用している場合、この変更が既存のデータ管理ポリシーやワークフローにどのような影響を与えるかを評価してください。
*   オブジェクト作成後すぐにライフサイクルルールを適用する必要がある場合は、`age:0`以外の条件（例: `daysSinceCustomTime`、`numNewerVersions`など）の使用を検討するか、他の手段によるオブジェクト管理を検討してください。

用語説明：
*   **Object Lifecycle Management**: Cloud Storageバケット内のオブジェクトに対して、定義された条件に基づいて自動的に特定のアクション（例: 削除、ストレージクラスの変更）を実行する機能です。これにより、データ管理を効率化し、コストを最適化できます。
*   **`age` condition**: オブジェクトがCloud Storageに作成されてからの経過日数に基づいてライフサイクルアクションをトリガーする条件です。

---

# Google Kubernetes Engine

## Security

原文: GKE version 1.33.0-gke.1276000 and later remediate a low severity vulnerability, in which an attacker with the ability to patch Node resources by using the Kubernetes API could change specific node labels in clusters that use Workload Identity Federation for GKE. This could result in the attacker gaining access to node metadata, such as the IAM service account. To remediate this vulnerability, a validation policy is enforced that prevents unauthorized modifications to the node labels that control metadata protection.

説明：
GKEバージョン1.33.0-gke.1276000以降で、低重要度（low severity）のセキュリティ脆弱性が修正されました。この脆弱性は、Kubernetes APIを使用してNodeリソースをパッチできる権限を持つ攻撃者が、GKEのWorkload Identity Federationを使用しているクラスタにおいて、特定のノードラベルを不正に変更できるというものでした。これにより、攻撃者がIAMサービスアカウントなどのノードメタデータにアクセスできる可能性がありました。この脆弱性に対処するため、メタデータ保護を制御するノードラベルの不正な変更を防ぐバリデーションポリシーが適用されます。

影響有無：
**影響あり（潜在的なリスクが解消）**

*   本番環境でGKEクラスタを使用している場合、このセキュリティ修正は重要です。
*   特に、GKEクラスタでWorkload Identity Federationを使用しており、GKEバージョンが1.33.0-gke.1276000未満である場合、この脆弱性の影響を受ける可能性があります。
*   Google Cloud Composer 2 (Composer version 2.7.1) は、基盤としてGKEクラスタを利用しています。Composer環境のGKEクラスタが上記のバージョン範囲に該当する場合、この脆弱性の対象となります。Google Cloud ComposerのGKEクラスタは、Googleによって管理・アップグレードされることが多いため、通常は自動的にこの修正が適用されると期待されます。

対処方法：
*   **GKEクラスタのバージョン確認とアップグレード:**
    *   ご利用中のGKEクラスタのバージョンが1.33.0-gke.1276000未満である場合、速やかにクラスタを最新のパッチバージョンにアップグレードすることを強く推奨します。
    *   GKEの自動アップグレード機能が有効になっている場合は、特別な手動操作は不要で、修正が自動的に適用されるはずです。自動アップグレード設定を確認してください。
*   **Google Cloud Composer環境について:**
    *   Composer環境の基盤GKEクラスタのバージョンは、Google Cloud Composerのメンテナンス期間中に自動的に更新されます。
    *   Composerのリリースノートやメンテナンス情報で、基盤となるGKEバージョンがこの修正を含むバージョンに更新されたことを確認してください。通常、特別なユーザー操作は不要です。

用語説明：
*   **Workload Identity Federation for GKE**: GKEワークロードがGoogle Cloudリソースにアクセスするために、GCPサービスアカウントを模倣するKubernetesサービスアカウントを使用できるようにする機能です。これにより、GCPサービスアカウントキーをクラスタ内に配布する必要がなくなり、セキュリティが向上します。
*   **Node labels**: Kubernetesクラスタ内のノードに付与されるキーと値のペアのメタデータです。ノードの役割や特性を示すために使用され、スケジューリングやポリシー適用などの目的で利用されます。
*   **IAM service account**: Google CloudのIdentity and Access Management (IAM) におけるサービスアカウントです。Google Cloudリソースにアクセスするための認証情報として機能し、アプリケーションやサービスがGoogle Cloud APIを呼び出す際に使用されます。

---

# Resource Manager

## Fixed

原文: Certain Organization Policy managed constraints that were released on August 21, 2025 were not functioning as intended. The Organization Policy Service evaluated these constraints as if the `effectiveInstanceMetadata` field of the resources that they were enforced on was empty, causing them to always evaluate to either allow or deny access to the resource. [managed constraints](https://cloud.google.com/resource-manager/docs/organization-policy/overview#managed-constraints) The following managed constraints were evaluated to always allow creation of resources where they were enforced: - `constraints/compute.managed.disableGuestAttributesAccess` - `constraints/compute.managed.disableSerialPortAccess` - `constraints/compute.managed.disableSerialPortLogging` The following managed constraints were evaluated to always block creation of resources where they were enforced: - `constraints/compute.managed.disallowGlobalDns` - `constraints/compute.managed.requireOsConfig` - `constraints/compute.managed.requireOsLogin` This issue has been corrected, and these constraints now properly evaluate the `effectiveInstanceMetadata` field to determine whether resource creation should be allowed or blocked.

説明：
（※原文中の「August 21, 2025」は日付の誤植または将来の特定のリリースを指す可能性がありますが、「Fixed」カテゴリであるため、既に修正が適用された過去の事象として説明します。）

2025年8月21日にリリースされた（またはリリース時にバグを含んでいた）特定のOrganization Policyのmanaged constraintsが、意図した通りに機能していなかった問題が修正されました。
この問題により、これらの制約は対象リソースの`effectiveInstanceMetadata`フィールドが空であるかのように評価されていました。結果として、ポリシーが常にリソース作成を許可してしまうか、あるいは常にブロックしてしまうという予期せぬ挙動を示していました。

具体的には以下の制約が影響を受けていました。
*   常にリソース作成を許可していた制約（本来は特定の条件でブロックすべきもの）：
    *   `constraints/compute.managed.disableGuestAttributesAccess`
    *   `constraints/compute.managed.disableSerialPortAccess`
    *   `constraints/compute.managed.disableSerialPortLogging`
*   常にリソース作成をブロックしていた制約（本来は特定の条件で許可すべきもの）：
    *   `constraints/compute.managed.disallowGlobalDns`
    *   `constraints/compute.managed.requireOsConfig`
    *   `constraints/compute.managed.requireOsLogin`

今回の修正により、これらの制約は`effectiveInstanceMetadata`フィールドを適切に評価し、リソース作成の可否を正確に判断するようになりました。

影響有無：
**影響あり（問題解消による正常化、または意図しない変更）**

*   もし貴社環境で上記のいずれかの`managed constraints`を使用していた場合、今回の修正によりポリシーが正常に機能するようになります。
*   **ポジティブな影響**: `disallowGlobalDns`や`requireOsConfig`などが常にブロックしていたため、リソース作成が妨げられていた環境では、問題が解消され、ポリシーの意図通りの挙動を示すようになります。
*   **注意が必要な影響**: `disableGuestAttributesAccess`などが常に許可していたため、本来はブロックされるべきリソース作成が許可されていた環境では、今後ポリシーが正常に適用され、本来ブロックされるべきリソース作成がブロックされるようになる可能性があります。この場合、既存の自動化されたデプロイメントやワークロードに影響を与える可能性があります。
*   Google Cloud Composer 2 (Composer version 2.7.1) は、Compute Engineインスタンスを基盤として利用しており、これらの制約はCompute Engineインスタンスの挙動に関連します。プロジェクトまたはフォルダレベルでこれらのOrganization Policyが適用されている場合、Composerの基盤となるリソースのデプロイや挙動に間接的に影響を与えていた可能性があり、今回の修正により正常化します。

対処方法：
*   **設定状況の確認:**
    *   現在、貴社のGoogle Cloud環境で上記の`managed constraints`のいずれかがOrganization Policyとして設定されているか確認してください。
    *   特に、これまで意図しない挙動（例: `disable`系の制約を設定しているのにリソース作成が許可されていた）を経験していた場合は、今回の修正により正常な挙動に戻ったことを確認してください。
*   **ワークフローの評価:**
    *   もし`disable`系の制約を適用しており、過去にそれが機能していなかったためにリソース作成が許可されていたケースがあった場合、今回の修正によってそれらのリソース作成がブロックされるようになる可能性があります。関連するデプロイメントや自動化されたワークフローに影響がないか評価し、必要に応じてポリシー設定の見直しやワークフローの調整を検討してください。

用語説明：
*   **Organization Policy**: Google Cloudのリソース階層（組織、フォルダ、プロジェクト）全体にわたって、リソースの利用方法や設定を強制的に制御するためのサービスです。これにより、コンプライアンスやセキュリティの要件を組織全体で一貫して適用できます。
*   **Managed constraints**: Organization Policyで利用可能な、Googleによって事前に定義・管理されている制約です。特定のAPIの使用、リソースの構成、サービスの使用などを制限するために使用されます。
*   **`effectiveInstanceMetadata`**: Compute Engineインスタンスのメタデータキーとその値の集合。特定のメタデータ（例えば、シリアルポートアクセスやゲスト属性など）は、インスタンスのセキュリティや機能に影響を与えるため、Organization Policyで制御対象となることがあります。
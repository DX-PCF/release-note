# 1.34.1

### 追加された「Bug or Regression」セクションの要約と注目点

これらの変更は、主にバグ修正であり、Kubernetes 1.34.0 のリリース後の回帰（regression）や、特定条件下での問題に対処しています。

*   **SELinux Warning Controller のイベント発行:**
    *   **変更点:** SELinux ラベルの競合が発生した場合に、SELinux Warning Controller がイベントを発行しない問題が修正されました。
    *   **重要度:** **中**。SELinux を使用している環境で、SELinux ポリシー違反に関する警告やデバッグ情報が適切に取得できていなかった場合、問題の特定が遅れる可能性がありました。この修正により、SELinux ポリシー関連の問題がより迅速に検知できるようになります。

*   **API リソースのシェル補完の破損:**
    *   **変更点:** `kubectl` の API リソースに対するシェル補完機能が壊れていた問題が修正されました。
    *   **重要度:** **低**〜**中**。開発者やオペレーターが `kubectl` コマンドを操作する際に、API リソース名を補完できなくなるため、作業効率に影響が出る可能性があります。

*   **Kube-apiserver の CustomResourceDefinition (CRD) フォーマット警告 (Regression):**
    *   **変更点:** Kubernetes 1.34.0 で、CRD の数値型や整数型プロパティに対して、実際には存在しない「認識されないフォーマット」に関する誤った警告が表示されていた回帰が修正されました。
    *   **重要度:** **中**。これは 1.34.0 で発生した回帰であり、CRD を頻繁に扱う環境では、不要な警告ログがノイズとなっていた可能性があります。

*   **Kube-apiserver の "Error getting keys" ログメッセージ (Regression):**
    *   **変更点:** Kubernetes 1.34.0 で、etcd へのキー取得時に「Error getting keys」という偽のログメッセージが表示される回帰が修正されました。
    *   **重要度:** **中**。これは誤ったログであり、実際の障害と見間違える可能性があったため、デバッグの妨げになっていました。

*   **Kube-apiserver のオブジェクトサイズ統計計算パフォーマンス (Regression):**
    *   **変更点:** Kubernetes 1.34.0 で、Watch Cache から提供されないリソース（通常は Events）のオブジェクトサイズ統計を計算する際のパフォーマンス低下という回帰が修正されました。
    *   **重要度:** **中**。特に大量の Event を扱うような環境では、API サーバーのパフォーマンスに影響が出ていた可能性があります。

*   **Kubeadm v1beta3 `APIServer.TimeoutForControlPlane` 尊重:**
    *   **変更点:** Kubeadm の新しいバージョンで v1beta4 がデフォルトになった際、v1beta3 の `ClusterConfiguration.APIServer.TimeoutForControlPlane` 設定が尊重されないバグが修正されました。
    *   **重要度:** **中**〜**高**。クラスタの初期化やアップグレード時に、API サーバーへのタイムアウト設定が正しく適用されないと、コントロールプレーンコンポーネントの起動に問題が発生する可能性があります。特に、API サーバーの起動が遅い環境や、ネットワーク遅延が大きい環境では影響が出やすいです。

### 「Dependencies」セクションについて

「Dependencies」セクションに「Nothing has changed」と記載されていることから、この追加情報においては、**依存関係の更新による影響はない**と判断できます。

### まとめとアクションアイテム

これらの追加情報から、特に以下の点に注意してください。

1.  **Kubeadm のアップグレード:**
    *   もし Kubeadm を使用してクラスタを管理しており、`ClusterConfiguration.APIServer.TimeoutForControlPlane` を `v1beta3` の設定でカスタマイズしていた場合、1.34.0 へのアップグレード後にこの設定が期待通りに機能しない回帰が発生していた可能性があります。この修正は、**クラスタの安定稼働に直接関わるため、重要度が高い**です。
    *   **アクション:** Kubeadm のアップグレードパスや設定ファイルを確認し、必要であれば API バージョンを v1beta4 に合わせる、あるいは Kubeadm の再実行による設定適用を検討してください。

2.  **API サーバーの回帰修正:**
    *   Kube-apiserver に関する CRD フォーマット警告、"Error getting keys" ログ、オブジェクトサイズ統計のパフォーマンス回帰は、いずれも 1.34.0 リリース後の回帰であり、この修正パッチ (おそらく 1.34.x のマイナーリリース) によって解消されます。
    *   **アクション:** 監視ログにこれらの問題が見られた場合、この修正を適用したバージョンへのアップデートを検討してください。

3.  **SELinux ユーザー:**
    *   SELinux を有効にして Kubernetes を運用している場合は、SELinux Warning Controller のバグ修正により、ポリシー関連の問題のデバッグが容易になります。
    *   **アクション:** SELinux を使用している環境では、この修正による恩恵が期待できます。

これらの修正は、Kubernetes 1.34.0 のリリース後に発見された問題に対するパッチリリースに含まれるものと思われます。もし、これらの問題に遭遇している、あるいは懸念がある場合は、最新のマイナーバージョンへのアップデートを検討することをお勧めします。

==========================================================================
# 1.34.0

## Kubernetes 1.34.0 リリースノートの要約と注目点

今回のリリースでは、メトリクスラベルの変更、Kubelet の deprecated フラグ削除、DRA (Dynamic Resource Allocation) の機能強化など、多岐にわたる変更が行われています。特に、**Urgent Upgrade Notes** に記載されているメトリクスの変更は、監視システムに影響を与える可能性があるため、優先的に確認が必要です。

### 1. 必須のアップグレード注意事項 (Urgent Upgrade Notes)

これは最も重要です。アップグレード前に必ず確認し、対応を検討してください。

*   **メトリクスラベルの変更:** 多くの apiserver および etcd メトリクスのラベルが変更・追加されています。
    *   `apiserver_cache_list_fetched_objects_total`, `apiserver_cache_list_returned_objects_total`, `apiserver_cache_list_total` では、`resource_prefix` ラベルが `API group` および `resource` ラベルに置き換えられます。
    *   `etcd_request_duration_seconds`, `etcd_requests_total`, `etcd_request_errors_total` では、`type` ラベルが `API resource` および `group` ラベルに置き換えられます。
    *   `apiserver_selfrequest_total` に `API group` ラベルが追加されます。
    *   `apiserver_watch_events_sizes`, `apiserver_watch_events_total` では、`API kind` ラベルが `resource` ラベルに置き換えられます。
    *   その他多数のメトリクスで、`resource` ラベルから `group` ラベルが抽出され、API グループ情報が新しい `group` ラベルに格納されます。

    **【対応】** 監視ツールのクエリやアラート設定で、これらのメトリクスラベルの変更に合わせて修正が必要になります。Prometheus や Grafana などの設定を確認してください。

*   **Kubelet の deprecated フラグ削除:** `--cloud-config` フラグが削除されました。
    **【対応】** Kubelet の起動オプションから `--cloud-config` を削除してください。

*   **静的 Pod の Admission 拒否:** Kubelet が、API オブジェクトを参照する静的 Pod の Admission を拒否するようになりました。これは、ミラー Pod の作成に失敗した場合でも、静的 Pod がサイレントに実行され続けることを防ぐための変更です。
    **【影響】** 静的 Pod が何らかの理由で API オブジェクトを参照できなくなった場合、Pod が起動しなくなります。

*   **スケジューリングフレームワークの変更:** `NodeInfos` が `PreFilter` プラグインに公開され、`NodeInfo` リストを引数として受け取れるようになりました。
    **【影響】** カスタムスケジューラプラグインを開発している場合、この変更に対応する必要があります。

### 2. 主要な変更点 (Changes by Kind)

#### 2.1. 非推奨 (Deprecation)

*   **Apimachinery:** `MessageCountMap` と `CreateAggregateFromMessageCountMap` が非推奨になりました。
*   **DRA Kubelet:** DRA の gRPC API が `v1` に昇格し、`v1beta1` は非推奨となりました。
*   **kubeconfig:** kubeconfig の `preferences` フィールドが、`kuberc` の利用を推奨する形で非推奨となりました。

#### 2.2. API 変更 (API Change)

*   **PodSpec の `hostnameOverride`:** Pod のホスト名を指定できるようになりました。`HostnameOverride` feature gate で制御されます。
*   **ContainerRestartRules (Alpha):** コンテナレベルの再起動ルールが Alpha 版として導入されました。`ContainerRestartRules` feature gate で制御されます。
*   **EnvFiles:** コンテナがファイルから環境変数をロードできるようになりました。`EnvFiles` feature gate で制御されます。
*   **Resource Slice / Resource Claim 拡張:** DRA におけるデバイスの共有、リソース要求、スケジューリングに関するフィールドが追加・拡張されました。
*   **JWT Authenticator の Egress Selector:** JWT 認証で `controlplane` または `cluster` の egress selector を指定できるようになりました。
*   **DRA のリソースヘルス監視:** Kubelet が DRA で割り当てられたデバイスのヘルスを監視し、`pod.status.containerStatuses.allocatedResourcesStatus` に報告できるようになりました。
*   **Kubelet のイメージプル認証情報追跡:** Service Account ベースの検証がサポートされ、同一 Service Account を使用する Pod はキャッシュされたイメージに再認証なしでアクセスできるようになりました。
*   **PodLevelResources on Windows OS:** Windows OS での `PodLevelResources` の使用が拒否されるようになりました。
*   **Headless Service の警告:** Headless Service で `loadBalancerIP`, `externalIPs`, `SessionAffinity` を設定した場合に警告が表示されるようになりました。
*   **`pvc.spec.VolumeAttributesClassName` の変更:** `nil` から非 `nil` への変更が許可されるようになりました。
*   **Hugepage cgroup 伝播:** Pod レベルの hugepage cgroup が、コンテナに hugepage リソースが指定されていない場合でも伝播されるようになり、関連するバリデーションも追加されました。
*   **DRA API の変更 (`resource.k8s.io/v1alpha3`)**: `DeviceTaintRule` のみが残り、他のタイプは削除されました。以前のバージョンからのアップグレード時に注意が必要です。
*   **DRA の `resource.k8s.io/admin-access` ラベル:** `resource.kubernetes.io/admin-access` に更新されました。
*   **DRA スケジューラプラグインのタイムアウト:** `FilterTimeout` が設定可能になり、デフォルトで 10 秒でタイムアウトするようになりました。
*   **DRA の Prioritized List:** デバイス割り当て数が許可数を超えた場合に、スケジューラが早期に試行を中止するようになりました。
*   **DRA kubelet gRPC API `v1alpha4` のサポート削除:** `v1beta1` が推奨されます。
*   **`StreamingConnectionIdleTimeout` (Kubelet):** 非推奨になりました。
*   **DRA コア機能の GA:** 構造化パラメータを使用した DRA のコア機能が GA (General Availability) になりました。
*   **`PodCertificateRequest` および `PodCertificate` プロジェクテッドボリューム:** Kube-apiserver でサポートされ、`PodCertificateRequest` feature gate で制御されます。
*   **DRA バックの拡張リソース:** `DeviceClass` に `extendedResourceName` を指定できるようになり、Pod のリクエストで DRA デバイスを指定できるようになりました。
*   **NodePorts スケジューリングプラグイン:** 再起動する init コンテナが使用する `hostPorts` を考慮するようになりました。
*   **Kube-scheduler の Regression Fix:** コンテナの spec と status にわたるリソース要求の集計時に発生していた nil panic が修正されました。
*   **`PodCertificateRequest` の prerelease lifecycle:** 修正されました。
*   **CRD スキーマの OpenAPI フォーマット:** `k8s-short-name` および `k8s-long-name` のサポートが追加されました。
*   **`admissionregistration.k8s.io/v1beta1/MutatingAdmissionPolicy` API:** Alpha 版として導入されました。
*   **Kube-apiserver の Webhook 決定キャッシング無効化:** `cacheAuthorizedRequests` および `cacheUnauthorizedRequests` フィールドで制御できます。
*   **Kube-apiserver の `StructuredAuthenticationConfiguration`:** GA に昇格しました。
*   **Kube-apiserver の `--authentication-config`:** `apiserver.config.k8s.io/v1` に昇格しました。
*   **Kube-log-runner:** ログローテーション、古いログファイルの自動削除、定期的なフラッシュ機能が追加されました。
*   **Kubectl `kuberc` サポート:** Beta 版に昇格しました。
*   **Job Pod Replacement Policy:** GA に昇格しました。
*   **`MutableCSINodeAllocatableCount`:** Beta 版に昇格しました。
*   **`VolumeAttributesClass`:** GA に昇格し、`storage.k8s.io/v1` API が提供されます。
*   **`APIServerTracing` feature gate:** GA に昇格しました。
*   **`AuthorizeWithSelectors` / `AuthorizeNodeWithSelectors` feature gate:** Stable になり、ロックされました。
*   **`KubeletTracing` feature gate:** GA に昇格しました。
*   **`RelaxedEnvironmentVariableValidation` feature gate:** GA に昇格し、デフォルトで有効になりました。
*   **`hostNetwork` のポート要件に関する記載削除:** Pod spec の `hostNetwork` フィールド設定時にポートが必要であるという不正確な記述が削除されました。
*   **gogo プロトコル定義の削除:** `k8s.io/kubelet/pkg/apis/pluginregistration` から削除され、`google.golang.org/protobuf` に置き換えられました。
*   **boolean-pointer-helper 関数の置き換え:** `k8s.io/utils/ptr` の実装に置き換えられました。
*   **`k8s.io/utils/pointer` の deprecation:** `k8s.io/utils/ptr` に置き換えられました。
*   **ゼロ値の `metadata.creationTimestamp`:** JSON, YAML, CBOR 出力で `null` がシリアライズされなくなりました。
*   **AppArmor プロファイルのアノテーションコピー削除:** 非推奨の `container.apparmor.security.beta.kubernetes.io/` アノテーションへのコピーがなくなりました。
*   **`MultiCIDRServiceAllocator`:** ロックされ、デフォルトで有効になりました。

#### 2.3. 機能 (Feature)

*   **スケジューラ非同期APIコールメトリクス:** `SchedulerAsyncAPICalls` feature gate で有効になる、API コールの実行状況や所要時間を追跡する 3 つの新しいメトリクスが追加されました。
*   **HPA と Pod-level リソース:** Pod-level リソース機能が有効な場合、HPA が `pod.Spec.Resources` から Pod リソースを計算できるようになりました。
*   **`kubectl describe service` のトラフィック分散表示:** トラフィック分散フィールドが表示されるようになりました。
*   **`SizeBasedListCostEstimate` feature gate:** LIST リクエストのコストを推定できるようになり、APF シートの割り当て方法が変更されました。
*   **`apiserver_resource_size_estimate_bytes` メトリクス:** API サーバーに追加されました。
*   **ユーザー名前空間 Pod の作成メトリクス:** 作成の成功・失敗を追跡するメトリクスが追加されました。
*   **`kubectl top` の `--show-swap` オプション:** 追加されました。
*   **`container_swap_limit_bytes` メトリクス:** コンテナに割り当てられたスワップ制限を公開します。
*   **Kubelet 起動後のノード更新遅延:** ノードステータス更新のトラフィックと負荷を均等に分散させるために遅延が追加されました。
*   **`kubectl version` のクライアント/サーバーバージョン不一致検出:** サポート範囲外のバージョン不一致を検出するフラグが追加されました。
*   **`PreBindPlugin` インターフェースの `PreBindPreFlight`:** 新しい関数が追加され、すべてのインツリー `PreBind` プラグインが実装されました。
*   **Alpha メトリクスとエミュレートバージョン:** Alpha メトリクスをエミュレートバージョンで使用した場合に警告が表示されるようになりました。
*   **互換性バージョニングの Alpha メトリクス:** 追加されました。
*   **協調リーダー選出のための Kube-apiserver フラグ:** 設定可能になりました。
*   **`kubectl api-resources` の機械可読出力:** JSON および YAML の出力オプションが追加されました。
*   **スケジューラパフォーマンステストのメモリ追跡:** メモリリーク検出とメモリ使用パターンの監視に役立ちます。
*   **CEL 式のサポート (エスケープ名):** `[...]` を使用して、名前にエスケープが必要な文字が含まれる場合のクレイムやユーザーデータへのアクセスがサポートされました。
*   **`kubectl autoscale` の `--cpu`, `--memory` フラグ:** 追加され、`--cpu-percent` は非推奨となりました。
*   **`kubectl` の新しい出力フォーマット `kyaml`:** 導入されました。
*   **`DetectCacheInconsistency` feature gate:** API サーバーがキャッシュと etcd の整合性を定期的に検証できるようになりました。
*   **`SizeBasedListCostEstimate` feature gate (デフォルト有効):** LIST リクエストのデータロード量に基づいて APF シートが割り当てられます。
*   **Kube-apiserver の有用なエンドポイント:** 追加されました。
*   **Go 1.24.3 / 1.24.4 でのビルド:** Kubernetes がビルドされました。
*   **DRA API バージョン Bump:** `k8s.io/dynamic-resource-allocation` の `deviceattribute` パッケージで `v1` に Bump されました。
*   **`KubeletCgroupDriverFromCRI` GA:** GA に昇格し、サポート外の CRI 実装を追跡するメトリクスが追加されました。
*   **CRI API の認証フィールド:** デバッグでマスクされるようになりました。
*   **`CustomResourceDefinitions` の unrecognized formats:** 未認識フォーマットでのスキーマ書き込み時に警告が表示されるようになりました。
*   **DRA Kubelet の ResourceSlice クリーンアップ:** 一部の追加障害シナリオで `ResourceSlices` をクリーンアップできるようになりました。
*   **`DRAAdminAccess` デフォルト有効:** Privileged モードでの `ResourceClaims` および `ResourceClaimTemplates` 作成がサポートされ、管理者タスクのためのデバイスアクセスが可能になりました。
*   **KEP-5278 feature gates の Alpha への降格:** `ClearingNominatedNodeNameAfterBinding` および `NominatedNodeNameForExpectation` が Alpha に降格しました。
*   **`apiserver_storage_objects` メトリクス:** `apiserver_resource_objects` に置き換えられました。
*   **Service 作成時の遅延除去:** Helm チャート経由でデプロイされた外部リソースのポート目的の理解における遅延が解消されました。
*   **Watch cache の compact snapshots:** `etcd` compaction イベントに基づいて有効になりました。
*   **`kubectlrc` のエイリアス補完:** サポートされました。
*   **Guaranteed QoS Pod のメモリリサイズ:** `InPlacePodVerticalScalingExclusiveMemory` feature gate で制御され、デフォルトは false です。
*   **Pod スケジューリングバックオフ時間:** スケジューリング関連以外のエラー（ネットワークエラーなど）で延長されなくなりました。
*   **Pod スケジューリング時の API コール非同期実行:** `SchedulerAsyncAPICalls` feature gate で有効になりました。
*   **`kubelet_container_resize_requests_total` メトリクス:** すべてのリサイズ関連の更新を含むように修正されました。
*   **`ListFromCacheSnapshot`:** Beta 版に昇格しました。
*   **`PodLevelResources` feature:** Beta 版に昇格し、デフォルトで有効になりました。Pod 全体の CPU/メモリリソースを `pod.spec.resources` で定義できるようになります。
*   **`PodObservedGenerationTracking` feature:** Beta 版に昇格し、デフォルトで有効になりました。`status.observedGeneration` および `status.conditions[].observedGeneration` フィールドが PodSpec の `metadata.generation` を反映するようになります。
*   **`ResilientWatchCacheInitialization`:** GA に昇格しました。
*   **`StreamingCollectionEncodingToJSON` / `StreamingCollectionEncodingToProtobuf`:** GA に昇格しました。
*   **匿名認証のための設定可能エンドポイント:** GA に昇格しました。
*   **DNS 検索文字列の検証緩和:** GA に昇格しました。
*   **スケジューラ `QueueingHint` サポート:** GA に昇格しました。
*   **`WinOverlay` feature (kube-proxy):** GA に昇格し、デフォルトで有効になりました。
*   **`ConsistentListFromCache`:** GA に昇格しました。
*   **`WatchList` feature gate:** Kube-apiserver で Beta 版になり、KCM で `WatchListClient` が有効になりました。
*   **`WinDSR` feature (kube-proxy):** GA に昇格し、デフォルトで有効になりました。
*   **`PreBindPreFlight` の `Skip` 戻り値:** スケジューラが `PreBind` プラグインを実行しなくなりました。
*   **リサイズリクエストの優先順位付け:** `priorityClass` と QoS クラスに基づいて、ノードリソースが不足している場合のリサイズリクエストの優先順位付けが実装されました。
*   **`kubectl delete` の出力:** 名前空間が含まれるようになり、リソースの識別が容易になりました。
*   **APF max seats for LIST requests:** 100 に増加しました。
*   **`GetPCIeRootAttributeByPCIBusID` メソッド:** サードパーティ DRA ドライバが `resource.kubernetes.io/pcieRoot` デバイス属性の共通ロジックを提供できるようになりました。
*   **Kube-apiserver の構成ハッシュメトリクス:** 認証、認可、暗号化設定ファイルのロード後に、最後の設定ハッシュがメトリクスラベルとして報告されるようになりました。
*   **Kube-apiserver の etcd サーバオーバーライドヘルスチェック:** `--etcd-servers-overrides` で指定された各ユニークなセットに対してヘルスチェックが追加されました。
*   **Kube-apiserver の invalid whitespace-only `caBundle`:** 空白のみの `caBundle` を持つ `CustomResourceDefinition` オブジェクトが、変換を必要としないリクエストを処理できるようになりました。
*   **`ExternalServiceAccountTokenSigner` feature:** Beta 版に昇格し、外部署名と公開鍵取得がサポートされました。
*   **Kube-proxy の IPv6 利用チェック:** Linux で IPv6 が利用可能かどうかがチェックされるようになりました。
*   **Kubeadm ECDSA-P384 サポート:** v1beta4 で暗号化アルゴリズムタイプとして追加されました。
*   **Kubeadm etcd メンバー昇格バグ修正:** メンバーが既に昇格されていると報告されるエラーが修正されました。
*   **Kubeadm `NodeLocalCRISocket` feature gate:** Beta 版に昇格し、デフォルトで有効になりました。`containerRuntimeEndpoint` をカスタマイズするためのファイル生成などが含まれます。
*   **Kubeadm `WaitForAllControlPlaneComponents` feature gate:** GA に昇格し、すべてのコントロールプレーンコンポーネントのヘルスチェックが実行されるようになりました。
*   **Kubeadm Linux カーネルバージョン検証:** 警告からエラーではなくなりました。
*   **Kubelet CSI ボリュームマウント失敗検知:** CSI ドライバがノードのアタッチメント制限を超えた場合、Stateful Pod を Failed にマークし、コントローラーによる再作成を可能にしました。
*   **Kubelet credential provider config hash メトリクス:** Credential provider 設定のハッシュがメトリクスとして報告されるようになりました。
*   **Kubelet `--image-credential-provider-config`:** ディレクトリパスも指定できるようになりました。
*   **LeaseLocks カスタムラベル:** ホルダーが変更された場合に上書きされるカスタムラベルがサポートされました。
*   **メモリ制限の減少:** `NotRequired` リサイズ再起動ポリシーでメモリ制限を減少できるようになりました。
*   **`CertificateSigningRequest` の検証移行:** `DeclarativeValidation` feature gate によって、宣言的検証に移行されました。
*   **ボリューム拡張失敗からのリカバリ:** GA に昇格しました。
*   **Pod CPU/Memory アライメント:** PodSpec で Pod-level リソースが使用されている場合、Topology Manager からの CPU/Memory マネージャーによるアライメントやヒント生成が無効になりました。
*   **Linux ノード圧力停止情報 (PSI) メトリクス:** Beta 版に昇格しました。
*   **Windows 正常終了機能:** Alpha から Beta に昇格しました。
*   **Ordered Namespace Deletion テスト:** Conformance に昇格しました。
*   **`KubeletPodResourcesDynamicResources` / `KubeletPodResourcesGet` feature gates:** Beta 版に昇格し、デフォルトで有効になりました。
*   **`OrderedNamespaceDeletion` feature:** GA に昇格しました。
*   **APF デフォルト構成からの FlowSchemas 削除:** "endpoint-controller" と "workload-leader-election" が削除されました。
*   **Pod リサイズメトリクス記録:** 開始されました。
*   **Pod Topology Spread の `matchLabelKeys` マージ:** `topologySpreadConstraints` の `labelSelector` にマージされるようになりました。`MatchLabelKeysInPodTopologySpreadSelectorMerge` feature gate で制御されます。
*   **`PreferSameTrafficDistribution` feature gate:** デフォルトで有効になり、`PreferSameNode` トラフィック分散値がサポートされました。
*   **`dra_resource_claims_in_use` Kubelet メトリクス:** アクティブな `ResourceClaims` をドライバーごとに報告します。
*   **スケジューラ `nominatedNodeName` フィールドクリア:** Pod がノードにバインドされた後、`nominatedNodeName` フィールドがクリアされなくなりました。
*   **`CertificateSigningRequest` の `/status` および `/approval` サブプロセスの検証移行:** 宣言的検証に移行されました。
*   **`kube-controller-manager` イベント:** コンテキストログをサポートするように更新されました。
*   **Pause version:** `registry.k8s.io/pause:3.10.1` に更新されました。
*   **Go 1.24.5 でのビルド:** Kubernetes がビルドされました。
*   **`system:monitoring` ロール:** Kubelet メトリクスエンドポイントへのアクセス権限が付与されました。
*   **`RelaxedServiceNameValidation` feature gate:** 新しい Service 名の検証が緩和されます。
*   **集約 API サーバーへのプロキシ:** EndpointSlices を使用するようになりました。
*   **Pod バインド時の `nominatedNodeName` クリア:** Kube-apiserver が Pod の `nominatedNodeName` フィールドをクリアするようになりました。
*   **`DRAPrioritizedList` デフォルト有効:** `ResourceClaim` でサブリクエストの優先リストを提供できるようになりました。
*   **`PodLifecycleSleepAction`:** GA に昇格しました。
*   **`kube-controller-manager` ResourceClaim メトリクス:** `resourceclaim_controller_creates_total` と `resourceclaim_controller_resource_claims` メトリクスが追加されました。
*   **kubeadm 静的 Pod マニフェスト:** プローブポートの命名規則が変更されました。

#### 2.4. テストの失敗 (Failing Test)

*   **DRA driver helper:** Kubernetes バージョンと DRA ドライバのバージョン不一致時の apiserver 再起動時の処理が修正されました。
*   **e2e テストの Pod/namespace リーク:** CSI-hostpath ドライバのテストで Pod と namespace のリークが修正されました。
*   **Kube-apiserver `--service-account-signing-endpoint`:** 抽象ソケット名のフォーマットのみを検証するようになりました。

#### 2.5. バグまたはリグレッション (Bug or Regression)

*   **StatefulSet 作成時の `podSpec` 検証:** 追加されました。
*   **Kubelet リサイズフィールドチェック:** リカバリ機能のステータス決定で、より新しいリサイズフィールドがチェックされるようになりました。
*   **`kubectl delete --ignore-not-found`:** watch 操作でサポートされるようになりました。
*   **DRA ドライバの ResourceSlice 誤認:** ResourceSlice が削除された際に、リソースコントローラーが ResourceSlice を再作成しない問題が修正されました。
*   **DRA `adminAccess` ResourceClaims の重複割り当て防止:** `adminAccess` を持つ `ResourceClaims` が同じデバイスを複数回割り当てられることがなくなりました。
*   **ext/xfs ファイルシステム拡張のディスクジオメトリ読み取り無効化:** ディスクジオメトリの読み取りが無効になりました。
*   **SharedInformers の transformer/WatchList 連携:** transformer が提供され、`WatchList` がアクティブな場合、オブジェクトはストレージ前に変換されるようになりました。
*   **`StorageClassList` クエリの API レスポンス:** `ResourceVersion` が大きすぎる場合に、適切なエラーメッセージが返されるように修正されました。
*   **ReplicationController 調整:** `DeploymentReplicaSetTerminatingReplicas` feature gate が有効な場合の調整が修正されました。
*   **CEL `UnstructuredToVal` バグ:** Identical なオブジェクトで `==` が false になる問題が修正されました (Kubernetes API には影響なし)。
*   **Job コントローラーの不要な Pod 作成:** 完了した Job に対して不要な Pod を作成するバグが修正されました。
*   **新規 Job Pod 作成遅延:** Job の新規 Pod 作成における予期しない遅延が修正されました。
*   **ReplicaSet 更新時の二重検証バグ:** ReplicaSet 更新時の二重検証バグが修正されました。
*   **長すぎる Deployment 名での ReplicaSet 作成失敗バグ:** 修正されました。
*   **非同期プリエンプションの Preemptor Pod キュー保持バグ:** Preemptor Pod を不要にキューに保持する問題が修正されました。
*   **`kubectl revision history` パニック:** 修正されました。
*   **Watch client のデッドロック:** Watch が停止されない場合に発生する可能性のあるデッドロックが修正されました。
*   **Paginated LIST コール etcd フォールバック:** 1.33 で発生していた paginated LIST コールが etcd にフォールバックするリグレッションが修正されました。
*   **`kubeadm reset --config` エラーメッセージ:** `JoinConfigurationKind` への誤った参照が修正されました。
*   **Terminate 中の CRD による Server-Side Apply:** Terminate 中の CRD を使用した Custom Resource 作成が可能になる問題が修正されました。
*   **Windows kube-proxy `ModifyLoadBalancer` API:** HNS 状態との不一致が修正されました。
*   **`insufficientResources` ログ:** Pod プリエンプション中にポインタとしてログされる問題が修正され、ログが読みやすくなりました。
*   **Kubelet トークンキャッシュの stale token:** Service Account 再作成時に stale token を返す問題が修正され、キャッシュが UID 認識になりました。
*   **`PodTopologyLabelAdmission` Alpha feature:** 正しいラベルキーをチェックしていなかった問題が修正されました。
*   **ResourceClaim `AllocationMode: All` のバグ:** Subrequests で使用された場合の `AllocationMode: All` のバグが修正されました。
*   **Admission control メトリクスの応答コード:** 不適切な応答コードが修正されました。
*   **`x-int-or-string` CR スキーマのランタイムコスト推定:** 最大長での推定が修正されました。
*   **PVC ステータス検証の `allocatedResourceStatuses` mismatch:** 修正されました。
*   **Pod リサイズ条件の `observedGeneration`:** `InPlacePodVerticalScaling` と `PodObservedGenerationTracking` feature gate が有効な場合、関連する Pod generation を正確に反映するように修正されました。
*   **`/metrics/resource` エンドポイントの swap メトリクス:** swap メトリクスが利用できない問題が修正されました。
*   **コンテナレベルリソース要件の Pod レベル解釈:** Pod レベルでサポートされていないリソースをコンテナレベルで指定した場合の検証エラーが修正されました。
*   **Job `suspend=true` と `completions=0` の検証:** `Complete` 条件を設定するように修正されました。
*   **HPA ステータス メモリメトリクス:** Ki を使用して表示される問題が修正されました。
*   **ユーザー名前空間 Pod での Runtime 非サポートエラーメッセージ:** 改善されました。
*   **CronJob `spec.jobTemplate.spec.podFailurePolicy.rules[*].onPodConditions[*].status`:** ドキュメント通り、デフォルトで空のフィールドが設定され、検証エラーが回避されるようになりました。
*   **OIDC Discovery document publishing:** External Service Account Token Signing が有効な場合に修正されました。
*   **`iptables` CLI wait interval flag:** 削除されました。
*   **ResourceClaim あたりのデバイス数:** 16 から 32 に戻りました。
*   **Kubeadm local etcd image:** etcd バージョンが 3.6.0 未満の場合のデフォルト引数が修正されました。
*   **Static Pods の arbitrary ResourceClaims 参照:** 無効にするように修正されました。
*   **Kubelet CSI ドライバ `NodeResizeError`:** CSI ドライバがノードボリューム拡張をサポートせず、PVC が `ReadWriteMany` アクセスモードを持つ場合に、予期しない `NodeResizeError` 条件が表示される問題が修正されました。
*   **`podresources` API endpoint:** アクティブな Pod のみが考慮されるようになりました。
*   **User namespaces と `volumeDevices` の混在:** Pod が user-namespace (`hostUsers: false`) と `volumeDevices` を混在させることができなくなりました。
*   **Node unreachable taint 遅延:** `node.kubernetes.io/unreachable:NoExecute` を taint するまでの 5 秒の遅延が短縮されました。
*   **`make vet` target 削除:** `make lint` を使用するよう指示されました。
*   **`ip6tables-legacy-restore` binary:** 非推奨の `--wait-interval` フラグが削除されました。
*   **ReplicaSets and Deployments `status.availableReplicas`:** 正確なタイミングでカウントされるようになり、Deployment の条件の早期同期とロールアウトのブロック解除が可能になりました。
*   **DaemonSet 更新時の二重検証:** DaemonSet 更新時の不要な二重検証が解消されました。
*   **Pod backoff スキップ:** `PodMaxBackoffDuration` がゼロで `SchedulerPopFromBackoffQ` feature gate が有効な場合、Pod backoff が完全にスキップされるようになりました。
*   **PVC 拡張無効化:** `node-expand-not-required` アノテーションを持つ PVC の拡張が無効になりました。
*   **ノードでのボリューム拡張停止:** コントローラー側の拡張が完了した場合、ノードでの拡張が停止されるようになりました。
*   **Kubelet での拡張待ちエラーログ:** エラーログの記録が停止されました。
*   **CSI JSON ファイル削除停止:** ボリュームが既にマウントされている場合のエラー発生時に、CSI JSON ファイルの削除が停止されました。
*   **Pod Security Admission levels:** `baseline` および `restricted` レベルで、プローブおよびライフサイクルハンドラーの `host` フィールド設定がブロックされるようになりました。
*   **Garbage collection controller racing:** `ownerReferences` の変更と競合する問題が修正されました。
*   **`kubectl explain --output` shorthand:** 削除された shorthand が追加されました。
*   **Windows kube-proxy `EndpointSlice` port honoring:** Linux との整合性を保つために、内部トラフィックルーティングのために `EndpointSlice` で指定されたポートを正しく尊重するように更新されました。
*   **`conntrack` reconciler:** スパムフローエントリのクリーンアップで Service のターゲットポートが考慮されるようになりました。
*   **`kubeadm` etcd feature gate/flag:** `InitialCorruptCheck=true` etcd feature gate と `--watch-progress-notify-interval` が使用されるようになりました。
*   **`cri-tools` updated:** v1.33.0 に更新されました。
*   **etcd client library updated:** v3.6.4 に更新されました。
*   **CoreDNS upgraded:** v1.12.1 にアップグレードされました。
*   **`kubectl kustomize` functionality:** v5.7.0 にアップグレードされました。
*   **`HorizontalPodAutoscaler` APIVersion fields:** 検証が追加されました。

#### 2.6. その他 (Cleanup or Flake)

*   **`kubectl attach` 警告:** Log subresource を使用するよう促す警告が追加されました。
*   **CBOR エンコーディング/デコーディング:** 標準ライブラリインターフェースを実装した型が CBOR にエンコード/デコードできるようになりました。
*   **kube-dns bump:** v1.26.4 に bump されました。
*   **cel-go 依存性 bump:** v0.25.0 に bump されました。
*   **grpcnotrace tag:** デフォルトで有効になりました。
*   **Job controller:** Pod ルックアップに controller UID index を使用するように変更されました。
*   **Mutating webhook patch decode failure:** Webhook の failurePolicy をトリガーし、メトリクスをカウントするように変更されました。
*   **Crane digest:** `e2e-test-images/agnhost:2.56` に更新されました。
*   **DRA kubelet logging:** `pluginName` の代わりに `driverName` を使用するようにログが更新されました。
*   **DRA kubelet Recovery Simplification:** ドライバが実行されていないノードへの Pod スケジューリングミスからの回復が簡素化されました。
*   **フラグ説明/ログの空白文字修正:** 修正されました。
*   **`hack/update-codegen.sh`:** goimports および protoc を自動的に確認するようになりました。
*   **Kubelet package テストカバレッジ:** 92.3% に増加しました。
*   **Kube-apiserver deprecated metrics removal:** `apiserver_encryption_config_controller_automatic_reload_success_total` および `apiserver_encryption_config_controller_automatic_reload_failure_total` が削除され、`apiserver_encryption_config_controller_automatic_reloads_total` に置き換えられました。
*   **Kube-scheduler deprecated metric removal:** `scheduler_scheduler_cache_size` が `scheduler_cache_size` に置き換えられました。
*   **Kubeadm pause image mismatch warning space:** 修正されました。
*   **Kubeadm CoreDNS deployment manifest:** プローブポートの命名規則が統一されました。
*   **Kubectl interactive delete:** 空の改行入力を 'N' として扱うようになりました。
*   **Linux thermal interrupt information masking:** `/proc` および `/sys` 経由で公開される情報がマスクされるようになりました。
*   **Memory Manager Contextual Logging:** コンテキストログに移行されました。
*   **`pkg/kubelet/status` Contextual Logging:** コンテキストログに移行されました。
*   **`pkg/kubelet/volumemanager` Contextual Logging:** コンテキストログに移行されました。
*   **`pkg/kubelet/winstats` Contextual Logging:** コンテキストログに移行されました。
*   **NONW:** 変更はありません。
*   **`SeparateTaintEvictionController` feature gate:** GA に昇格し、無条件で有効になりました。
*   **BETA Metrics promotion:** `apiserver_authentication_config_controller_automatic_reloads_total` および `apiserver_authentication_config_controller_automatic_reload_last_timestamp_seconds` が BETA に昇格しました。
*   **EndpointSlice テスト conformance:** Service proxy 実装が EndpointSlices を使用することを確認するテストが Conformance に昇格しました。
*   **Volume Binding scheduler plugin logging reduction:** メッセージの冗長度が V(4) から V(5) に引き下げられました。
*   **gogo protocol definitions removal:** `k8s.io/externaljwt` から削除されました。
*   **gogo protocol definitions removal:** `k8s.io/kms/apis` から削除されました。
*   **gogo protocol definitions removal:** `k8s.io/kubelet/pkg/apis/deviceplugin` から削除されました。
*   **gogo protocol definitions removal:** `k8s.io/kubelet/pkg/apis/podresources` から削除されました。
*   **GA feature-gate removal:** `DevicePluginCDIDevices` が削除されました。
*   **GA feature-gate removal:** `PodDisruptionConditions` が削除されました。
*   **API streaming support removal:** REST client から削除されました。
*   **API streaming support removal:** typed client の `List()` メソッドから削除されました。
*   **API streaming support removal:** dynamic client の `List()` メソッドから削除されました。
*   **API streaming support removal:** metadata client の `List()` メソッドから削除されました。
*   **`kubernetes.io/initial-events-list-blueprint` annotation removal:** 削除されました。
*   **Kubelet deprecated argument removal:** `--register-schedulable` が削除されました。
*   **`toPtr` helper functions replacement:** `k8s.io/utils/ptr` の実装に置き換えられました。
*   **`k8s.io/utils/pointer` deprecation replacement:** 様々なパッケージで `k8s.io/utils/ptr` に置き換えられました。
*   **`LegacySidecarContainers` feature gate removal:** 完全に削除されました。
*   **Scheduler framework type relocation:** `pkg/scheduler/framework` から `staging` リポジトリに移動しました。
*   **Scheduler framework type relocation:** `pkg/scheduler/framework` から `k8s.io/kube-scheduler/framework` に移動しました。
*   **Scheduler framework type relocation:** `pkg/scheduler/framework` から `k8s.io/kube-scheduler/framework` に移動しました。
*   **Scheduler framework type relocation:** `pkg/scheduler/framework` から `staging` リポジトリに移動しました。
*   **CNI plugins updated:** v1.7.1 に更新されました。
*   **`conntrack` reconciler update:** Service のターゲットポートを考慮するようになりました。
*   **`kubeadm` etcd features:** `InitialCorruptCheck=true` etcd feature gate と `--watch-progress-notify-interval` が使用されるようになりました。
*   **`cri-tools` updated:** v1.33.0 に更新されました。
*   **etcd client library updated:** v3.6.4 に更新されました。
*   **CoreDNS upgraded:** v1.12.1 にアップグレードされました。
*   **`kubectl kustomize` functionality:** v5.7.0 にアップグレードされました。
*   **`HorizontalPodAutoscaler` APIVersion fields validation:** 追加されました。

### 3. 依存関係 (Dependencies)

*   **Added:** 新しい依存関係が追加されています。
*   **Changed:** 既存の依存関係が更新されています。特に `go.etcd.io/etcd` は `v3.6.4` に、`google.golang.org/grpc` は `v1.72.1` に更新されています。
*   **Removed:** 多くの `cloud.google.com/go` パッケージが削除されています。

## アップグレードにおける考慮事項

1.  **メトリクス監視:** 最優先で、監視ツールのクエリやアラート設定を更新してください。
2.  **Kubelet 設定:** `--cloud-config` フラグを使用している場合は、削除または代替策を検討してください。
3.  **DRA ユーザー:** DRA を利用している場合は、API および gRPC の変更点（特に v1alpha4 の削除、v1 への昇格）に注意してください。
4.  **スケジューラプラグイン:** カスタムスケジューラプラグインや、スケジューラフレームワークに依存するコンポーネントは、変更点に対応しているか確認してください。
5.  **Deprecation 警告:** 非推奨となった API やフラグについては、将来のバージョンでの削除を見据えて、対応を計画してください。
6.  **Go バージョン:** Kubernetes 1.34.0 は Go 1.24.3/1.24.4/1.24.5 でビルドされています。カスタムビルドや、Go バージョンに依存するプラグインを使用している場合は、互換性を確認してください。
7.  **Etcd バージョン:** Etcd のバージョンが v3.6.0/v3.6.1/v3.6.4 に更新されています。Etcd のアップグレードパスや互換性についても確認してください。

このリリースノートは非常に詳細ですが、上記に挙げた点は特にインフラエンジニアとして把握しておくべき重要な変更点です。アップグレード計画の際には、これらの情報を基に、各コンポーネントへの影響を評価し、必要な対応を実施してください。

---
# v1.33.5
承知いたしました。Kubernetes 1.33.5 のリリースノートですね。Google Cloud のインフラエンジニアの視点から、これらの変更点について解説します。

### Kubernetes 1.33.5 リリースノートの要約と注目点

このリリースは、主にバグ修正と、Go のバージョンアップ、および一部のクリーンアップ作業が中心です。1.33.x のメンテナンスリリースとして、安定性の向上に寄与する変更が含まれています。

#### 1. 新機能 (Feature)

*   **Go 1.24.6 でのビルド:**
    *   **変更点:** Kubernetes が Go 1.24.6 でビルドされるようになりました。
    *   **重要度:** **低**〜**中**。これはコンパイル環境の更新であり、通常、直接的な機能変更はありません。ただし、Go のアップデートにはセキュリティ修正やパフォーマンス改善が含まれる場合があるため、間接的に安定性やセキュリティが向上する可能性があります。
    *   **インフラエンジニアとしての観点:** 自身で Kubernetes バイナリをビルドする場合や、Go のバージョンに依存するツールを使用している場合は、この更新を把握しておく必要があります。

#### 2. バグまたはリグレッション (Bug or Regression)

*   **ServiceCIDR API の準拠性テスト調整:**
    *   **変更点:** ServiceCIDR API のパッチ (Patch) および更新 (Update) 操作が、準拠性テストの `ineligible_endpoints` としてマークされていたため、これらのテストが調整（削除）されました。
    *   **重要度:** **低**。これは主に Kubernetes のテストスイートに関する変更であり、プロダクション環境での Kubernetes の挙動に直接的な影響を与えるものではありません。

*   **SELinux Warning Controller のイベント発行:**
    *   **変更点:** SELinux ラベルの競合が発生した場合に、SELinux Warning Controller がイベントを発行しない問題が修正されました。
    *   **重要度:** **中**。SELinux を使用している環境では、SELinux ポリシー違反に関する警告やデバッグ情報が適切に取得できていなかった場合、問題の特定が遅れる可能性がありました。この修正により、SELinux ポリシー関連の問題がより迅速に検知できるようになります。
    *   **インフラエンジニアとしての観点:** SELinux を有効にしているノード（特に RHEL/CentOS/Fedora 系など）では、この修正により、SELinux ポリシー違反時のトラブルシューティングが容易になります。

*   **Kubeadm の `ClusterConfiguration.APIServer.TimeoutForControlPlane` 尊重:**
    *   **変更点:** Kubeadm が v1beta4 をデフォルトとして使用するようになった際、v1beta3 の `ClusterConfiguration.APIServer.TimeoutForControlPlane` 設定が正しく尊重されないバグが修正されました。
    *   **重要度:** **中**〜**高**。クラスタの初期化やアップグレード時に、API サーバーへのタイムアウト設定が正しく適用されないと、コントロールプレーンコンポーネントの起動に問題が発生する可能性があります。特に、API サーバーの起動が遅い環境や、ネットワーク遅延が大きい環境では影響が出やすいです。
    *   **インフラエンジニアとしての観点:** Kubeadm を使用してクラスタのライフサイクル管理を行っている場合、この修正は非常に重要です。API サーバーのタイムアウト設定が意図通りに機能しないと、クラスタのデプロイやアップグレードに失敗する原因となり得ます。

#### 3. その他 (Cleanup or Flake)

*   **/proc および /sys への Linux thermal interrupt 情報アクセス制限:**
    *   **変更点:** `/proc` および `/sys` ファイルシステム経由で公開されていた Linux のサーマル割り込み情報へのアクセスがマスク（制限）されるようになりました。
    *   **重要度:** **低**。これは主にセキュリティ強化または情報漏洩リスクの低減を目的とした変更であり、Kubernetes の通常の運用に直接影響を与えるものではありません。
    *   **インフラエンジニアとしての観点:** サーバーのハードウェア状態を詳細に監視している場合、この変更によって一部の情報にアクセスできなくなる可能性があります。ただし、Kubernetes の管理上、必須の情報ではないでしょう。

#### 4. 依存関係 (Dependencies)

*   **Added, Changed, Removed:** いずれも「Nothing has changed」と記載されているため、このリリースノートの範囲では**依存関係の変更はありません**。

### インフラエンジニアとしてのまとめと推奨事項

*   **Kubeadm ユーザーへの影響:** Kubeadm を使用してクラスタを管理している場合、特に API サーバーのタイムアウト設定 (`TimeoutForControlPlane`) に関連するバグ修正は重要です。1.33.5 へのアップデートは、この問題に遭遇している、あるいは将来的に遭遇するリスクを避けるために推奨されます。
*   **SELinux ユーザーへの恩恵:** SELinux を有効にしている環境では、SELinux ポリシー違反のデバッグが容易になるため、この修正は有益です。
*   **Go バージョンの更新:** Go 1.24.6 への更新は、一般的には安定性やセキュリティの向上に繋がります。
*   **影響の少ない変更:** ServiceCIDR API のテスト調整や、サーマル割り込み情報へのアクセス制限は、Kubernetes の日常的な運用に直接的な影響を与える可能性は低いです。

**全体として、Kubernetes 1.33.5 は、特に Kubeadm の設定に関する重要なバグ修正を含んだメンテナンスリリースです。** もし 1.33.x 系列のバージョンを使用しており、これらのバグに該当する状況がある場合は、速やかに 1.33.5 へのアップデートを検討することをお勧めします。


# v1.33.4
### **【最重要】セキュリティ脆弱性 CVE-2025-5187**

これは `NodeRestriction` アドミッションコントローラに存在する脆弱性です。

**問題の概要:**
この脆弱性を利用すると、ノード権限を持つユーザー（または侵害されたノード）が、`OwnerReference` というメタデータを自身に追加することで、対応するノードオブジェクトを削除できてしまいます。 デフォルトでは、ノードユーザーは自身のノードオブジェクトを削除する権限を持っていませんが、この脆弱性によりその制限を回避できます。

**影響:**
攻撃者がノードを侵害した場合、この脆弱性を悪用してノードオブジェクトを一度削除し、その後、異なるTaint（テイント）やLabel（ラベル）を持つノードとして再作成する可能性があります。これにより、本来スケジュールされるべきでないPodがそのノードで実行されたり、セキュリティポリシーを回避されたりするなど、クラスタ全体に影響が及ぶ可能性があります。

**影響を受けるバージョン:**
*   kube-apiserver v1.31.0 - v1.31.11
*   kube-apiserver v1.32.0 - v1.32.7
*   kube-apiserver v1.33.0 - v1.33.3

**修正済みバージョン:**
*   **kube-apiserver v1.31.12**
*   **kube-apiserver v1.32.8**
*   **kube-apiserver v1.33.4**

**推奨されるアクション:**
お使いのクラスタが影響を受けるバージョンであるかを確認し、**可及的速やかに修正済みのバージョンへアップグレードすること**を強く推奨します。

### **その他の変更点**

今回のリリースには、セキュリティ修正の他に以下の変更が含まれています。

*   **API変更/不具合修正:**
    *   `kube-scheduler`がリソース要求を集計する際にnilポインタでパニックに陥る可能性がある、v1.33の不具合が修正されました。
*   **機能:**
    *   Kubernetesのビルドに使用されるGoのバージョンが`1.24.5`に更新されました。
*   **不具合またはリグレッション:**
    *   CVE-2025-5187に対応するため、ノードが自身の`ownerReferences`を変更することを禁止するようにノード制限が変更されました。

### **まとめ**

今回のリリースは、中程度（CVSSスコア: 6.7）のセキュリティ脆弱性に対応する重要なパッチリリースです。特に`kube-apiserver`はクラスタの根幹をなすコンポーネントであるため、迅速な対応が求められます。

ご不明な点があれば、さらに詳しく解説しますのでお知らせください。

# v1.33.3

このアップデートは、主にバグ修正や安定性の向上に焦点を当てています。

---

### **主な変更点（バグ修正・リグレッション）**

| 種類 | 内容 |
|:---|:---|
| **バグ修正** | 新しく作成されたJobのPod（コンテナ）の作成が、予期せず遅延する不具合が修正されました。 |
| **リグレッション修正** | 1.33で発生していた、一部のページ分割されたリスト取得（LIST calls）がキャッシュからではなく、直接etcd（データベース）にアクセスしてしまい、パフォーマンスが低下する問題が修正されました。 |
| **バグ修正** | `suspend=true`（一時停止）かつ`completions=0`（完了数0）でJobを作成した場合に、正しく完了状態（Complete condition）が設定されない検証ロジックの不具合が修正されました。 |
| **Kubeadmの修正** | `kubeadm`において、etcd（データベース）のメンバーを昇格させる際に「すでに昇格済みです」というエラーで失敗することがある問題が修正されました。 |
| **その他** | Linux環境でコンテナのリソースを計算する際に、不要なログが大量に出力される問題が改善されました。 |

---

### **依存関係の変更**

今回のアップデートでは、ライブラリなどの依存関係に追加や変更、削除されたものはありません。

# 1.32.9
承知いたしました。Kubernetes 1.32.9 のリリースノートについて、Google Cloud のインフラエンジニアの視点から解説します。

### Kubernetes 1.32.9 リリースノートの要約と注目点

このリリースも、1.33.5 と同様に、Go のバージョンアップ、Kubeadm のバグ修正、そして一部のクリーンアップ作業が中心です。1.32.x 系列のメンテナンスリリースとして、安定性とセキュリティの向上を目的としています。

#### 1. 新機能 (Feature)

*   **Go 1.23.12 でのビルド:**
    *   **変更点:** Kubernetes が Go 1.23.12 でビルドされるようになりました。
    *   **重要度:** **低**〜**中**。これはコンパイル環境の更新であり、直接的な機能変更はありません。ただし、Go のアップデートにはセキュリティ修正やパフォーマンス改善が含まれる場合があるため、間接的に安定性やセキュリティが向上する可能性があります。
    *   **インフラエンジニアとしての観点:** 自身で Kubernetes バイナリをビルドする場合や、Go のバージョンに依存するツールを使用している場合は、この更新を把握しておく必要があります。

#### 2. バグまたはリグレッション (Bug or Regression)

*   **Kubeadm の `ClusterConfiguration.APIServer.TimeoutForControlPlane` 尊重:**
    *   **変更点:** Kubeadm が v1beta4 をデフォルトとして使用するようになった際、v1beta3 の `ClusterConfiguration.APIServer.TimeoutForControlPlane` 設定が正しく尊重されないバグが修正されました。
    *   **重要度:** **中**〜**高**。クラスタの初期化やアップグレード時に、API サーバーへのタイムアウト設定が正しく適用されないと、コントロールプレーンコンポーネントの起動に問題が発生する可能性があります。特に、API サーバーの起動が遅い環境や、ネットワーク遅延が大きい環境では影響が出やすいです。
    *   **インフラエンジニアとしての観点:** Kubeadm を使用してクラスタのライフサイクル管理を行っている場合、この修正は非常に重要です。API サーバーのタイムアウト設定が意図通りに機能しないと、クラスタのデプロイやアップグレードに失敗する原因となり得ます。

#### 3. その他 (Cleanup or Flake)

*   **/proc および /sys への Linux thermal interrupt 情報アクセス制限:**
    *   **変更点:** `/proc` および `/sys` ファイルシステム経由で公開されていた Linux のサーマル割り込み情報へのアクセスがマスク（制限）されるようになりました。
    *   **重要度:** **低**。これは主にセキュリティ強化または情報漏洩リスクの低減を目的とした変更であり、Kubernetes の通常の運用に直接影響を与えるものではありません。
    *   **インフラエンジニアとしての観点:** サーバーのハードウェア状態を詳細に監視している場合、この変更によって一部の情報にアクセスできなくなる可能性があります。ただし、Kubernetes の管理上、必須の情報ではないでしょう。

#### 4. 依存関係 (Dependencies)

*   **Added, Changed, Removed:** いずれも「Nothing has changed」と記載されているため、このリリースノートの範囲では**依存関係の変更はありません**。

### インフラエンジニアとしてのまとめと推奨事項

*   **Kubeadm ユーザーへの影響:** 1.33.5 と同様に、Kubeadm を使用してクラスタを管理している場合、API サーバーのタイムアウト設定 (`TimeoutForControlPlane`) に関連するバグ修正は重要です。1.32.9 へのアップデートは、この問題に遭遇している、あるいは将来的に遭遇するリスクを避けるために推奨されます。
*   **Go バージョンの更新:** Go 1.23.12 への更新は、一般的には安定性やセキュリティの向上に繋がります。
*   **影響の少ない変更:** サーマル割り込み情報へのアクセス制限は、Kubernetes の日常的な運用に直接的な影響を与える可能性は低いです。

**全体として、Kubernetes 1.32.9 は、Kubeadm の設定に関する重要なバグ修正を含んだメンテナンスリリースです。** もし 1.32.x 系列のバージョンを使用しており、Kubeadm によるクラスタ管理で API サーバーのタイムアウト設定に問題があった場合は、速やかに 1.32.9 へのアップデートを検討することをお勧めします。

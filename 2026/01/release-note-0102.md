
# Title: December 29, 2025 
Link: https://docs.cloud.google.com/release-notes#December_29_2025<br>
以下にリリースノートの内容を調査し、回答します。

---

# Apigee X
## Announcement
原文: On December 29th, 2025, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
Apigeeの更新バージョンが2025年12月29日にリリースされました。このリリースは本日よりロールアウトが開始されており、すべてのGoogle Cloudゾーンに適用されるまで4営業日以上かかる可能性があります。ロールアウトが完了するまで、お客様のApigeeインスタンスでは新機能や修正が利用できない場合があります。

影響有無：
影響はありません。これはサービスアップデートの通知であり、既存のApigeeインスタンスが自動的に更新されます。新機能や修正が適用されるまで時間差があるという注意喚起です。

対処方法：
特段の対処は不要です。ロールアウトの完了を待つことで、自動的に最新バージョンが適用されます。

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームであり、APIの設計、セキュア化、デプロイ、監視、分析、収益化を支援します。
*   **Rollout**: ソフトウェアやサービスの新しいバージョンが、段階的に、または特定の期間をかけてユーザーやインフラストラクチャ全体に展開されるプロセスです。

---

# Google Kubernetes Engine
## Announcement
原文: Kubernetes 1.35 is now available in the Rapid channel. For more information about the content of Kubernetes 1.35, read the Kubernetes 1.35 Release Notes and Kubernetes 1.35 Release Blog.

[Kubernetes 1.35 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#changelog-since-v1340)
[1.35 Release Blog](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/)

説明：
Kubernetes 1.35がGKEのRapidチャネルで利用可能になりました。詳細については、Kubernetes 1.35のリリースノートとブログを参照してください。

影響有無：
間接的な影響があります。
*   現在のGKEクラスターがRapidチャネルを使用している場合、このバージョンへのアップグレードが選択可能になります。
*   Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) は、Googleによって管理される特定のGKEバージョン（通常はRegularチャネル相当の長期サポートバージョン）で動作するため、現時点では直接このRapidチャネルのバージョンに影響されることはありません。しかし、将来的にComposerがこのGKEバージョンをサポートする可能性はあります。

対処方法：
*   GKEクラスターを運用している場合で、Rapidチャネルを使用している場合は、Kubernetes 1.35の変更内容を確認し、アプリケーションとの互換性を評価した上でアップグレードを検討してください。
*   Composerを利用している場合は、Composerの基盤となるGKEバージョンはGoogleによって管理されるため、ユーザー側での直接的なアクションは不要です。Composerのバージョンアップグレード時に、基盤GKEバージョンも更新される可能性があるため、その際にComposerのリリースノートを確認してください。

用語説明：
*   **Kubernetes**: コンテナ化されたワークロードとサービスを管理するためのオープンソースのオーケストレーションシステムです。
*   **GKE Rapid channel**: GKEのリリースチャネルの一つで、Kubernetesの最新のマイナーバージョンが比較的早く提供されます。ただし、その分、安定性よりも新機能や変更が先行する特性があります。

---

## Deprecated
原文: - The `PreferClose` value for a Kubernetes Service's `trafficDistribution` field is now deprecated in favor of the more explicit `PreferSameZone`.

[Kubernetes Service's](https://kubernetes.io/docs/concepts/services-networking/service/)
- Kubernetes has deprecated cgroup v1 support.
- GKE is removing cgroup v1 support in 1.35. If you have specifically configured your node pools to use cgroup v1 then upgrades will be blocked until you configure cgroup v2. To migrate to cgroup v2, see Migrate to cgroup v2.

[deprecated cgroup v1](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/#cgroup-v1-support)
[Migrate to cgroup v2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2#migrate)

説明：
2つの非推奨化に関するアナウンスです。
1.  Kubernetes Serviceの`trafficDistribution`フィールドにおける`PreferClose`値が非推奨となり、より明示的な`PreferSameZone`が推奨されます。
2.  Kubernetesがcgroup v1のサポートを非推奨化し、GKE 1.35からはcgroup v1のサポートが削除されます。ノードプールがcgroup v1を使用するように明示的に設定されている場合、GKE 1.35へのアップグレードがブロックされるため、cgroup v2への移行が必要です。

影響有無：
**1. `trafficDistribution`フィールドの非推奨化:**
影響は限定的です。通常のGoogle Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) の利用では、ユーザーが直接Kubernetes Serviceの`trafficDistribution`フィールドを設定することは稀です。カスタムのService設定をGKEクラスターにデプロイしている場合にのみ影響する可能性があります。

**2. cgroup v1サポートの非推奨化と削除:**
直接的な影響はありませんが、将来的な影響を考慮する必要があります。
*   現在のGKEクラスターがKubernetes 1.35未満であれば、直ちには影響しません。
*   Google Cloud Composer 2 は特定のGKEバージョン上で動作し、GKEノードプールの設定はGoogleが管理しています。Composerが利用しているGKEバージョンが1.35未満であるため、現時点ではcgroup v1を使用している場合でもComposerの運用に問題はありません。
*   しかし、将来的にComposerの基盤となるGKEバージョンが1.35以降にアップグレードされると、もしそのGKEノードプールがcgroup v1を使用していた場合、アップグレードがブロックされる可能性があります。通常、Google Cloud Composerのマネージド環境では、Googleが自動的にcgroup v2への移行を処理しますが、ユーザーが独自のGKEノードプール設定やカスタマイズを行っている場合は確認が必要です。

対処方法：
**1. `trafficDistribution`フィールドの非推奨化:**
*   もしGKEクラスターでKubernetes Serviceの`trafficDistribution: PreferClose`を使用している場合は、今後の互換性維持のため、`PreferSameZone`への変更を検討してください。

**2. cgroup v1サポートの非推奨化と削除:**
*   現在のGKEクラスターで明示的にcgroup v1を使用するように設定しているノードプールがないか確認してください。確認方法は、GKEのドキュメント「Migrate to cgroup v2」を参照してください。
*   もしcgroup v1を使用しているノードプールがある場合は、GKE 1.35へのアップグレード前にcgroup v2への移行を計画・実施してください。Composerに関しては、基盤GKEのcgroupバージョンはGoogleによって管理されるため、ユーザー側での直接的な操作は通常不要です。Composerの基盤GKEバージョンが1.35以降になる場合は、Composerのリリースノートで特に指示がないか確認してください。

用語説明：
*   **Kubernetes Service**: Kubernetesクラスタ内で実行されている一連のPodへのネットワークアクセスを提供するための抽象化された方法です。内部的なロードバランサーとして機能します。
*   **trafficDistribution**: Kubernetes Serviceにおけるトラフィックルーティングの挙動を制御するフィールドです。
*   **cgroup (control groups)**: Linuxカーネルの機能の一つで、プロセスグループにリソース（CPU、メモリ、I/Oなど）の割り当て、優先順位付け、およびアカウンティングを許可します。
*   **cgroup v1/v2**: cgroupのバージョンです。v2はv1と比較して、より統一された階層構造と改善されたリソース管理を提供します。GKE 1.35以降でcgroup v1のサポートが終了するため、v2への移行が推奨されます。

---

## Change
原文: **Windows containerd 2.1:** GKE Windows nodes will use containerd 2.1 in 1.35, upgraded from containerd 1.7 in GKE 1.34. Clusters containing Windows nodes will have auto-upgrades to 1.35 delayed until 1.34 EOL due to possible compatibility issues introduced in containerd 2.0. Check if you're using deprecated containerd features removed in 2.0 and migrate off of them, see Migrate nodes to containerd 2. After all deprecated features are removed, manually upgrade your cluster to 1.35.

[Migrate nodes to containerd 2](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2#migrate)

説明：
GKEのWindowsノードにおいて、バージョン1.35からcontainerd 2.1が使用されるようになります（GKE 1.34ではcontainerd 1.7）。containerd 2.0で導入された互換性の問題により、Windowsノードを含むクラスタのGKE 1.35への自動アップグレードは、GKE 1.34のEOL（End of Life）まで遅延されます。containerd 2.0で削除された非推奨機能を使用している場合は、それらの機能から移行する必要があり、その後手動でクラスタを1.35にアップグレードしてください。

影響有無：
影響はありません。
Google Cloud Composer 2 はLinuxベースのGKEノードを使用しており、Windowsノードは利用しません。したがって、この変更による影響は受けません。

対処方法：
特段の対処は不要です。

用語説明：
*   **containerd**: Kubernetesのコアランタイムであり、コンテナの実行、イメージの管理、およびストレージ機能を提供します。
*   **GKE Windows nodes**: Windows Serverオペレーティングシステムを実行しているGKEノードです。通常、Windowsコンテナを実行するために使用されます。

---

## Change
原文: GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

[GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明：
GKEクラスターの利用可能なバージョンが更新されました。新しいGKEクラスターの作成、および既存クラスターの手動コントロールプレーン/ノードアップグレード用に、以下のバージョンが利用可能になりました。

影響有無：
直接的な影響はありません。これは利用可能なGKEバージョンが増えたという一般的なアナウンスです。
Google Cloud Composer 2 の基盤となるGKEバージョンはGoogleによって管理されるため、ユーザーがこの情報に基づいてComposerの基盤GKEバージョンを手動でアップグレードすることはありません。

対処方法：
特段の対処は不要です。

用語説明：
*   **GKE cluster versions**: Google Kubernetes Engineクラスタが実行しているKubernetesのバージョンです。
*   **Control Plane**: Kubernetesクラスタの管理コンポーネント（APIサーバー、スケジューラー、コントローラーマネージャーなど）の集合です。

---

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Extended channel:

- 1.28.15-gke.3280000
- 1.29.15-gke.2613000
- 1.30.14-gke.1855000

- 1.28.15-gke.3280000
- 1.29.15-gke.2613000
- 1.30.14-gke.1855000

[1.28.15-gke.3280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1855000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)

説明：
GKEのExtendedチャネルで、以下のバージョンが利用可能になりました（ロールアウト中につき、まだ利用できないクラスターもあります）：1.28.15-gke.x、1.29.15-gke.x、1.30.14-gke.x。

影響有無：
直接的な影響はありません。
*   Google Cloud Composer 2 の基盤GKEは通常、ExtendedチャネルではなくRegularチャネルやStableチャネルを使用することが多いため、直接の関連は薄いです。
*   ご自身のGKEクラスターがExtendedチャネルを利用している場合に、これらのバージョンへのアップグレードが選択可能になります。

対処方法：
特段の対処は不要です。

用語説明：
*   **Extended channel**: GKEのリリースチャネルの一つで、長期的なサポートが必要なKubernetesバージョンを提供します。新しい機能よりも安定性を重視し、セキュリティパッチや重要なバグ修正のみが適用されます。

---

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available:

- 1.31.14-gke.1156000
- 1.32.9-gke.1711000
- 1.33.5-gke.2072000
- 1.34.1-gke.3899000

- The following node versions are now available:

- 1.28.15-gke.3280000
- 1.29.15-gke.2613000
- 1.30.14-gke.1855000
- 1.31.14-gke.1156000
- 1.32.9-gke.1711000
- 1.33.5-gke.2072000
- 1.34.1-gke.3899000

- 1.31.14-gke.1156000
- 1.32.9-gke.1711000
- 1.33.5-gke.2072000
- 1.34.1-gke.3899000

[1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
- 1.28.15-gke.3280000
- 1.29.15-gke.2613000
- 1.30.14-gke.1855000
- 1.31.14-gke.1156000
- 1.32.9-gke.1711000
- 1.33.5-gke.2072000
- 1.34.1-gke.3899000

[1.28.15-gke.3280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1855000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.9#v1329)
[1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.5#v1335)
[1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.1#v1341)

説明：
GKEの以下のコントロールプレーンおよびノードバージョンが利用可能になりました（ロールアウト中につき、まだ利用できないクラスターもあります）：1.31.x、1.32.x、1.33.x、1.34.x。また、ノードバージョンとして1.28.x、1.29.x、1.30.xも利用可能です。

影響有無：
直接的な影響はありません。
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) は、Kubernetes 1.27または1.28をベースに動作します。したがって、これらの新しいGKEバージョンは、現時点のComposer環境には直接影響しません。将来的にComposerのバージョンアップグレードにより、基盤GKEがこれらのバージョンに移行する可能性はあります。

対処方法：
特段の対処は不要です。

用語説明：
*   **Node versions**: GKEクラスターのワーカーノードが実行しているKubernetesおよびOSのバージョンです。Podが実際に実行される環境を提供します。

---

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Rapid channel:

- 1.31.14-gke.1156000
- 1.32.9-gke.1711000
- 1.33.5-gke.2072000
- 1.34.1-gke.3899000
- 1.35.0-gke.1272000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.35 to 1.35.0-gke.1272000

- 1.31.14-gke.1156000
- 1.32.9-gke.1711000
- 1.33.5-gke.2072000
- 1.34.1-gke.3899000
- 1.35.0-gke.1272000

[1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.9#v1329)
[1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.5#v1335)
[1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.1#v1341)
[1.35.0-gke.1272000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.0#v1350)
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.35 to 1.35.0-gke.1272000

[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
- 1.35 to 1.35.0-gke.1272000

[1.35.0-gke.1272000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.0#v1350)

説明：
GKEのRapidチャネルで、以下のバージョンが利用可能になりました（ロールアウト中につき、まだ利用できないクラスターもあります）：1.31.x、1.32.x、1.33.x、1.34.x、そして新たに1.35.0。このチャネルのクラスターは、記載されたマイナーバージョンを持つ場合に新しい自動アップグレードターゲットとなります。GKEは、マイナーバージョンアップグレードが利用できない場合や、メンテナンス除外などの要因がある場合に、クラスターを新しいパッチバージョン（例：1.35から1.35.0-gke.1272000）にアップグレードすることができます。

影響有無：
直接的な影響はありません。
Google Cloud Composer 2 はRapidチャネルを使用しないため、この変更による直接的な影響は受けません。ご自身のGKEクラスターがRapidチャネルを利用している場合に、これらのバージョンへのアップグレードや自動アップグレードの対象となります。

対処方法：
特段の対処は不要です。

用語説明：
*   **Auto-upgrade targets**: GKEが自動アップグレードの際にターゲットとするバージョンです。リリースチャネルやメンテナンスウィンドウ、除外設定によって対象バージョンが異なります。

---

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Regular channel:

- 1.31.14-gke.1081000
- 1.32.9-gke.1632000
- 1.33.5-gke.1956000

- 1.31.14-gke.1081000
- 1.32.9-gke.1632000
- 1.33.5-gke.1956000

[1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1632000](https://github.
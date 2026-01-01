
# Title: December 29, 2025 
Link: https://docs.cloud.google.com/release-notes#December_29_2025<br>
承知いたしました。Google Cloudのインフラエンジニアとして、提供されたリリースノートに基づき、既存のサービスへの影響調査結果を簡潔に、専門的な言葉遣いと書式設定で回答します。

---

# Apigee X
## Announcement
原文: On December 29th, 2025, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigeeの更新版が2025年12月29日にリリースされました。このロールアウトは本日より開始され、全てのGoogle Cloudゾーンでの完了には4営業日以上かかる場合があります。ロールアウトが完了するまで、新しい機能や修正がインスタンスで利用できない可能性があります。

影響有無: 軽微な影響。
*   既存のApigee Xインスタンスは、ロールアウトの完了を待つことで、自動的に新バージョンに更新されます。
*   このアナウンスは新機能の導入や既存機能の修正に関するものであり、後方互換性のない変更（Breaking Change）を示唆するものではないため、現在の運用に直接的な影響はありません。
*   新しい機能を利用したい場合は、ロールアウトの完了を待つ必要があります。

対処方法: 特に対応は不要です。必要に応じて、ロールアウト完了後に新機能や修正点を確認してください。

用語説明:
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォーム。APIの設計、セキュリティ、分析、モニタリングなどを一元的に管理します。
*   **ロールアウト (Rollout)**: 新しいソフトウェアバージョンや機能が段階的に展開され、全てのユーザーやインスタンスに適用されるプロセス。

---

# Google Kubernetes Engine
## Announcement
原文: Kubernetes 1.35 is now available in the Rapid channel. For more information about the content of Kubernetes 1.35, read the Kubernetes 1.35 Release Notes and Kubernetes 1.35 Release Blog.
[Kubernetes 1.35 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#changelog-since-v1340)
[1.35 Release Blog](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/)

説明: Kubernetes 1.35がGKEのRapidチャネルで利用可能になりました。詳細については、Kubernetes 1.35のリリースノートとリリースブログを参照してください。

影響有無: 潜在的な影響あり。
*   現在、当社の環境でGoogle Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) を利用していますが、Composerインスタンスの基盤となるGKEクラスターがRapidチャネルに設定されている場合、自動アップグレードの対象となる可能性があります。
*   Kubernetesのメジャーバージョンアップ（1.34から1.35）は、APIの変更や非推奨化された機能を含む可能性があるため、ワークロードの互換性確認が必要です。

対処方法:
1.  GKEクラスタがRapidチャネルを使用しているか確認し、使用している場合は、Kubernetes 1.35への自動アップグレードに備えて、既存のワークロードが互換性があることを検証してください。
2.  ComposerインスタンスのGKEバージョンおよびリリースチャネル設定を確認し、将来的な1.35へのアップグレードが予定されている場合は、事前にテスト環境で互換性検証を行うことを推奨します。

用語説明:
*   **Kubernetes 1.35**: オープンソースのコンテナオーケストレーションプラットフォームであるKubernetesのメジャーバージョン。
*   **Rapid channel**: GKEのリリースチャネルの一つで、最新のKubernetesバージョンが最も早く提供されます。新機能の早期アクセスが可能ですが、安定性は他のチャネル（Regular, Stable, Extended）に比べて低い傾向があります。

## Deprecated
原文:
- The `PreferClose` value for a Kubernetes Service's `trafficDistribution` field is now deprecated in favor of the more explicit `PreferSameZone`.
[Kubernetes Service's](https://kubernetes.io/docs/concepts/services-networking/service/)
- Kubernetes has deprecated cgroup v1 support.
- GKE is removing cgroup v1 support in 1.35. If you have specifically configured your node pools to use cgroup v1 then upgrades will be blocked until you configure cgroup v2. To migrate to cgroup v2, see Migrate to cgroup v2.
[deprecated cgroup v1](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/#cgroup-v1-support)
[Migrate to cgroup v2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2#migrate)

説明:
1.  Kubernetes Serviceの`trafficDistribution`フィールドにおける`PreferClose`値が非推奨となり、より明示的な`PreferSameZone`の使用が推奨されます。
2.  Kubernetes 1.35ではcgroup v1のサポートが非推奨となり、GKEも1.35でcgroup v1のサポートを削除します。ノードプールでcgroup v1を明示的に設定している場合、1.35へのアップグレードはブロックされます。cgroup v2への移行が必須となります。

影響有無:
1.  `trafficDistribution: PreferClose`を使用しているKubernetes Serviceがある場合に影響があります。しかし、デフォルト設定ではないため、明示的に設定していない限り影響は小さいです。
2.  **非常に大きな影響あり**。GKE 1.35へのアップグレード時（自動アップグレードを含む）に、ノードプールがcgroup v1を使用しているとアップグレードがブロックされます。当社で利用中のGoogle Cloud Composer 2はGKEを基盤としているため、Composerインスタンスが将来的にGKE 1.35へアップグレードされる際に、この変更による影響を受ける可能性があります。

対処方法:
1.  `trafficDistribution: PreferClose`を使用しているKubernetes Serviceがないか、`kubectl get svc -A -o yaml`などでクラスタ内のService設定を監査し、もし存在する場合は`PreferSameZone`への変更を検討してください。
2.  **最優先で対応が必要**。
    *   既存のGKEクラスタおよびComposerインスタンスの基盤となるGKEクラスタがcgroup v1を使用しているか確認します。
    *   cgroup v1を使用している場合は、GKE 1.35へのアップグレード前にcgroup v2への移行を計画し、実行してください。Google Cloudのドキュメント「Migrate to cgroup v2」を参照し、ノードプールの設定を更新する必要があります。
    *   ComposerインスタンスのGKE基盤のcgroup設定は直接変更できないため、Composerのバージョンアップグレードに伴うGKEバージョンアップグレード時に問題が発生しないよう、Composerのリリースノートやドキュメントでcgroup v2への対応状況を確認する必要があります。Composerのサポートチームへの問い合わせも検討してください。

用語説明:
*   **Kubernetes Service**: Kubernetesにおいて、一連のPodへのネットワークアクセスを定義する抽象化レイヤー。
*   **`trafficDistribution`**: Kubernetes Serviceのトラフィック分散方法を制御するフィールド。
*   **`PreferClose` / `PreferSameZone`**: クライアントに近いPod（同じゾーン内のPod）へのトラフィックを優先する設定。`PreferSameZone`はより明示的な設定名。
*   **cgroup (Control Group)**: Linuxカーネルの機能で、プロセスグループのリソース（CPU、メモリ、I/Oなど）使用量を制限・監視するために使用されます。
*   **cgroup v1 / cgroup v2**: cgroupのバージョン。v2はv1の機能を改善し、より統合されたリソース管理を提供します。Kubernetesの新しいバージョンではcgroup v2への移行が進んでいます。

## Change
原文: **Windows containerd 2.1:** GKE Windows nodes will use containerd 2.1 in 1.35, upgraded from containerd 1.7 in GKE 1.34. Clusters containing Windows nodes will have auto-upgrades to 1.35 delayed until 1.34 EOL due to possible compatibility issues introduced in containerd 2.0. Check if you're using deprecated containerd features removed in 2.0 and migrate off of them, see Migrate nodes to containerd 2. After all deprecated features are removed, manually upgrade your cluster to 1.35.
[Migrate nodes to containerd 2](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2#migrate)

説明: GKE Windowsノードは、GKE 1.35でcontainerd 2.1を使用するようになります（GKE 1.34ではcontainerd 1.7）。containerd 2.0で導入された互換性の問題により、Windowsノードを含むクラスターの1.35への自動アップグレードは、1.34のEOLまで遅延されます。containerd 2.0で削除された非推奨機能を使用している場合は、それらの機能から移行し、その後手動でクラスタを1.35にアップグレードする必要があります。

影響有無: 影響なし。
*   当社の環境ではWindowsノードを使用しているGKEクラスターがないため、この変更による直接的な影響はありません。Google Cloud Composer 2もLinuxベースのインスタンスを使用しているため、関連性はありません。

対処方法: なし。

用語説明:
*   **containerd**: CNCF（Cloud Native Computing Foundation）が提供するコンテナランタイムで、コンテナの実行、イメージの管理、ストレージなどを担当します。
*   **Windows nodes**: GKEクラスタ内でWindowsベースのコンテナを実行するためのノード（VMインスタンス）。通常はLinuxノードが主流です。

## Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明: GKEクラスタのバージョンが更新され、新しいバージョンが新規クラスタ作成、手動コントロールプレーンアップグレード、既存クラスタのノードアップグレードで利用可能になりました。

影響有無: 軽微な影響。
*   このアナウンス自体は具体的なバージョン情報を示すものではなく、GKEが継続的にバージョンアップされていることを示すものです。
*   今後のGKEクラスタの新規作成やバージョンアップグレードの計画に影響します。
*   Google Cloud Composer 2の基盤となるGKEバージョンも、Composerのアップデートサイクルに伴い更新される可能性があります。

対処方法: GKEのバージョン管理とサポートポリシーを定期的に確認し、今後のアップグレード計画に適切に反映させてください。

用語説明:
*   **GKE cluster versions**: GKEクラスタのコントロールプレーン（Kubernetes APIサーバーなど）およびノードプール（ワーカーノード）のKubernetesバージョン。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの管理層であり、APIサーバー、スケジューラー、コントローラーマネージャーなどが含まれます。
*   **ノードプール (Node Pool)**: GKEクラスタ内で同じ設定を持つVMインスタンス（ノード）のグループ。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Extended channel:
- 1.28.15-gke.3280000
- 1.29.15-gke.2613000
- 1.30.14-gke.1855000
[1.28.15-gke.3280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1855000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)

説明: Extendedチャネルで以下のGKEバージョンが利用可能になりました: 1.28.15-gke.3280000, 1.29.15-gke.2613000, 1.30.14-gke.1855000。これらのバージョンは既にロールアウトが進行中であり、全てのゾーンで利用可能になるには数日かかる場合があります。

影響有無: 潜在的な影響あり。
*   当社のGKEクラスタまたはGoogle Cloud Composer 2インスタンスの基盤となるGKEクラスターがExtendedチャネルを利用している場合、これらのバージョンへの自動アップグレードの対象となる可能性があります。
*   パッチバージョンアップですが、特定のバグ修正やセキュリティパッチが含まれているため、安定性向上に寄与します。

対処方法:
1.  Extendedチャネルを使用しているGKEクラスタがある場合は、これらのバージョンへのアップグレードに備え、必要に応じてテスト環境で検証を行ってください。
2.  ComposerインスタンスのGKE基盤のバージョンアップグレード計画を確認し、Extendedチャネルを使用している場合は、これらのバージョンへのアップグレードが問題なく行われるかComposerのドキュメントで確認してください。

用語説明:
*   **Extended channel**: GKEのリリースチャネルの一つで、Stableチャネルよりも長く特定のマイナーバージョンをサポートします。長期的な安定運用を目的としたクラスタに適しています。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
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
[1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.28.15-gke.3280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1855000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.9#v1329)
[1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

説明: 以下のGKEバージョンが新たに利用可能になりました。
*   コントロールプレーンおよびノードバージョン: 1.31.14-gke.1156000, 1.32.9-gke.1711000, 1.33.5-gke.2072000, 1.34.1-gke.3899000
*   ノードバージョンのみ: 1.28.15-gke.3280000, 1.29.15-gke.2613000, 1.30.14-gke.1855000（上記コントロールプレーンバージョンと合わせて使用可能）
これらのバージョンは既にロールアウトが進行中であり、全てのゾーンで利用可能になるには数日かかる場合があります。

影響有無: 軽微な影響。
*   GKEのパッチバージョンアップであり、主にバグ修正やセキュリティパッチが含まれます。
*   当社のGKEクラスタまたはGoogle Cloud Composer 2インスタンスの基盤となるGKEクラスターが、これらのGKEバージョンを現在使用しているか、または将来自動アップグレードの対象となる場合に影響します。一般的に、パッチバージョンアップは互換性問題を引き起こしにくいですが、リリースノートの変更ログで詳細を確認することが推奨されます。

対処方法:
1.  既存のGKEクラスタのバージョンがこれらのパッチバージョンに該当する場合、または自動アップグレードの対象となる場合、特別な対処は不要なことが多いですが、リリースノートを確認し、重要な変更がないか確認してください。
2.  ComposerインスタンスのGKE基盤バージョンアップグレード計画にこれらのバージョンが含まれていることを確認してください。

用語説明:
*   **パッチバージョン (Patch Version)**: バージョン番号の3番目の数字（例: 1.31.**14**）。主にバグ修正、セキュリティ修正、小さな改善が含まれ、後方互換性は維持されることが期待されます。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Rapid channel:
- 1.31.14-gke.1156000
- 1.32.9-gke.1711000
- 1.33.5-gke.2072000
- 1.34.1-gke.3899000
- 1.35.0-gke.1272000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.35 to 1.35.0-gke.1272000
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
[1.35.0-gke.1272000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)

説明: Rapidチャネルで以下のGKEバージョンが利用可能になりました: 1.31.14-gke.1156000, 1.32.9-gke.1711000, 1.33.5-gke.2072000, 1.34.1-gke.3899000, **1.35.0-gke.1272000**。このチャネルのクラスタは、上記のマイナーバージョンを実行している場合、新しい自動アップグレードターゲットを持つことになります。GKEは、コントロールプレーンとノードをこれらの新しいバージョンにアップグレードできます。

影響有無: 潜在的な影響あり。
*   当社のGKEクラスタまたはGoogle Cloud Composer 2インスタンスの基盤となるGKEクラスターがRapidチャネルを利用している場合、これらのバージョン、特にKubernetes 1.35.0への自動アップグレードの対象となる可能性があります。
*   Kubernetes 1.35へのメジャーバージョンアップグレードは、前述のcgroup v1サポート削除などの非互換性のある変更を含むため、既存のワークロードに影響を与える可能性が非常に高いです。

対処方法:
1.  **最優先で対応が必要**。Rapidチャネルを使用しているGKEクラスタがある場合、自動アップグレードが開始される前に、Kubernetes 1.35への互換性を徹底的にテストしてください。特にcgroup v1を使用している場合は、cgroup v2への移行を完了させる必要があります。
2.  ComposerインスタンスのGKE基盤のバージョンアップグレード計画を確認し、Rapidチャネルを使用している場合は、Kubernetes 1.35へのアップグレードがComposerの安定性に影響を与えないか、Composerのリリースノートやドキュメントで確認し、必要に応じてComposerのサポートチームと連携してください。

用語説明:
*   **自動アップグレードターゲット (Auto-upgrade targets)**: GKEクラスタが自動的にアップグレードされる先のバージョン。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Regular channel:
- 1.31.14-gke.108100
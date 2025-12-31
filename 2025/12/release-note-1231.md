
# Title: December 29, 2025 
Link: https://docs.cloud.google.com/release-notes#December_29_2025<br>
Google Cloudインフラエンジニアとして、ご提示いただいたリリースノートについて、製品ごとの影響有無および対処方法を以下に報告します。

---

# Apigee X
## Announcement
原文: On December 29th, 2025, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigeeの更新版が2025年12月29日にリリースされました。このロールアウトは本日開始され、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまで、インスタンスで新機能や修正が利用できない場合があります。
影響有無: **影響なし**
理由: このアナウンスはApigeeの新しいバージョンがリリースされたことを通知するものであり、具体的な機能変更、非互換性、または既存のデプロイメントに即座に影響を与えるような情報は含まれていません。新機能や修正が含まれると記載がありますが、既存の動作に影響する「Breaking Change」に関する言及がないため、現時点での直接的な運用影響はありません。
対処方法: 現時点での直接的な対応は不要です。今後Apigeeの更新に関する詳細なリリースノートや変更履歴が公開された際に、利用している機能に影響がないか確認することを推奨します。

---

# Google Kubernetes Engine
## Announcement
原文: Kubernetes 1.35 is now available in the Rapid channel. For more information about the content of Kubernetes 1.35, read the Kubernetes 1.35 Release Notes and Kubernetes 1.35 Release Blog.

説明: Kubernetes 1.35がGKEのRapidチャネルで利用可能になりました。Kubernetes 1.35の内容に関する詳細については、Kubernetes 1.35リリースノートとリリースブログを参照してください。
影響有無: **影響あり（ただし、Rapidチャネル利用者のみ）**
理由: 新しいマイナーバージョンであるKubernetes 1.35がRapidチャネルで提供開始されました。弊社がRapidチャネルを利用している場合、将来的にクラスタがこのバージョンに自動アップグレードされる可能性があります。マイナーバージョンアップグレードにはAPI変更や非互換性が含まれることがあり、アプリケーションの動作に影響を与える可能性があります。
対処方法:
1.  現在運用中のGKEクラスタが**Rapidチャネル**を利用しているか確認してください。
2.  Rapidチャネルを利用している場合、または将来的にRapidチャネルの利用を検討している場合は、リンク先の[Kubernetes 1.35 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#changelog-since-v1340)を確認し、APIの非互換性や非推奨になった機能がないか詳細に評価してください。
3.  自動アップグレードが有効な場合は、アップグレード前に開発/テスト環境でアプリケーションの互換性テストを実施することを強く推奨します。

用語説明:
*   **Rapid channel**: GKEのリリースチャネルの一つで、最新のKubernetesバージョンが最も早く提供されます。新機能の早期利用が可能ですが、安定版に比べて変更の頻度が高く、事前の検証がより重要になります。

## Deprecated
原文:
- The `PreferClose` value for a Kubernetes Service's `trafficDistribution` field is now deprecated in favor of the more explicit `PreferSameZone`.
- Kubernetes has deprecated cgroup v1 support.
- GKE is removing cgroup v1 support in 1.35. If you have specifically configured your node pools to use cgroup v1 then upgrades will be blocked until you configure cgroup v2. To migrate to cgroup v2, see Migrate to cgroup v2.

説明:
-   Kubernetes Serviceの`trafficDistribution`フィールドにおける`PreferClose`の値が非推奨となり、より明示的な`PreferSameZone`の使用が推奨されます。
-   Kubernetesはcgroup v1のサポートを非推奨としました。GKE 1.35ではcgroup v1のサポートが削除されます。ノードプールがcgroup v1を使用するように明示的に構成されている場合、cgroup v2に構成を変更するまでアップグレードがブロックされます。cgroup v2への移行については、提供されているドキュメントを参照してください。
影響有無: **影響あり（Breaking Changeの可能性あり）**
理由:
1.  **`PreferClose`**: 現在のKubernetes Service定義で`trafficDistribution: PreferClose`を使用している場合、将来的にこの値が削除される可能性があるため、移行計画が必要です。現時点では動作に影響はありませんが、非推奨警告が表示される可能性があります。
2.  **cgroup v1**: **GKE 1.35へのアップグレードに重大な影響があります。**もしノードプールがcgroup v1を使用するように設定されている場合、GKE 1.35への自動または手動アップグレードがブロックされます。これは、GKEを最新の状態に保つ上で看過できない影響です。
対処方法:
1.  **`trafficDistribution: PreferClose`について**:
    *   Kubernetes Serviceの設定をレビューし、`spec.trafficDistribution: PreferClose`を使用しているか確認してください。
    *   使用している場合は、`spec.trafficDistribution: PreferSameZone`への移行を検討してください。この変更は通常、サービス中断なしに行えますが、テスト環境での動作確認を推奨します。
2.  **cgroup v1サポート削除について**:
    *   現在運用中のGKEノードプールがcgroup v1を使用しているか確認してください。デフォルト設定ではcgroup v2が使用されますが、OSイメージのカスタマイズなどによってcgroup v1が使われている場合があります。ノードの`kubectl describe node <node-name>`の出力や、`gcloud container node-pools describe`コマンドで確認できます。
    *   もしcgroup v1を使用している場合は、直ちに[Migrate to cgroup v2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2#migrate)のドキュメントを参照し、cgroup v2への移行を実施してください。ノードプールの再作成やローリングアップデートが必要となる場合があります。
    *   この移行を行わないと、GKE 1.35（およびそれ以降）へのアップグレードが不可能になります。

用語説明:
*   **cgroup (control groups)**: Linuxカーネルの機能で、プロセスグループのリソース（CPU、メモリ、I/Oなど）の使用を管理・制限します。v1は古いバージョン、v2は新しいバージョンで、より柔軟なリソース管理が可能です。

## Change
原文: **Windows containerd 2.1:** GKE Windows nodes will use containerd 2.1 in 1.35, upgraded from containerd 1.7 in GKE 1.34. Clusters containing Windows nodes will have auto-upgrades to 1.35 delayed until 1.34 EOL due to possible compatibility issues introduced in containerd 2.0. Check if you're using deprecated containerd features removed in 2.0 and migrate off of them, see Migrate nodes to containerd 2. After all deprecated features are removed, manually upgrade your cluster to 1.35.

説明: GKEのWindowsノードは、GKE 1.35でcontainerd 2.1を使用するようになります（GKE 1.34のcontainerd 1.7からのアップグレード）。containerd 2.0で導入された互換性の問題により、Windowsノードを含むクラスタの1.35への自動アップグレードは、GKE 1.34のEOLまで遅延されます。非推奨となったcontainerd 2.0で削除された機能を使用している場合は、それらの機能から移行する必要があります。すべての非推奨機能の移行が完了した後、手動でクラスタを1.35にアップグレードしてください。
影響有無: **影響なし（Windowsノードを使用している場合のみ影響あり）**
理由: 弊社はGoogle Cloud Composer 2を利用しており、これはLinuxベースの環境で動作するため、Windowsノードは通常使用していません。したがって、この変更は弊社のGKE環境には直接的な影響を与えません。
対処方法: なし。

用語説明:
*   **containerd**: コンテナの実行と管理を行うオープンソースのコンテナランタイムです。Dockerなどの上位レイヤーのツールから利用され、イメージの転送、保存、コンテナの実行、監視、ネットワークアタッチなどを扱います。

## Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

説明: GKEクラスタのバージョンが更新され、新しいバージョンが利用可能になりました。これらのバージョンは、新規GKEクラスタの作成、および既存クラスタのコントロールプレーンとノードの手動アップグレードに利用できます。バージョン管理とアップグレードに関する詳細情報は、関連ドキュメントを参照してください。
影響有無: **影響なし**
理由: これは一般的なアナウンスであり、特定のバージョンや非互換性に関する直接的な言及はありません。新しいバージョンが利用可能になったことを通知するもので、現在の運用に直接的な影響を与えるものではありません。
対処方法: GKEのアップグレード計画を立てる際、利用可能な最新バージョンを考慮に入れることができます。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Extended channel:
- 1.28.15-gke.3280000
- 1.29.15-gke.2613000
- 1.30.14-gke.1855000

説明: Extendedチャネルで以下の新しいバージョンが利用可能になりました: 1.28.15-gke.3280000、1.29.15-gke.2613000、1.30.14-gke.1855000。これらのバージョンは現在ロールアウト中であり、全てのGoogle Cloudゾーンで利用可能になるまでに数日かかる場合があります。
影響有無: **影響あり（Extendedチャネル利用者のみ）**
理由: 弊社がGKEクラスタでExtendedチャネルを利用している場合、これらのパッチバージョンに自動アップグレードされる可能性があります。パッチバージョンアップグレードは通常、安定性の向上やセキュリティ修正が主であり、大きな非互換性は稀ですが、念のため確認は必要です。
対処方法:
1.  現在運用中のGKEクラスタが**Extendedチャネル**を利用しているか確認してください。
2.  Extendedチャネルを利用している場合、これらの新しいパッチバージョンが自動アップグレードの対象となることを認識しておいてください。
3.  各バージョンの具体的な変更点については、提供されているKubernetes CHANGELOGのリンク（例: [1.28.15-gke.3280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)）を参照し、潜在的な影響がないか確認できます。

用語説明:
*   **Extended channel**: GKEのリリースチャネルの一つで、Regularチャネルよりも長期的なサポートを提供し、安定性を重視します。セキュリティパッチや重要なバグ修正のみが適用されます。

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

説明: 以下のGKEバージョン（コントロールプレーンおよびノード）が利用可能になりました: 1.31.14-gke.1156000、1.32.9-gke.1711000、1.33.5-gke.2072000、1.34.1-gke.3899000。また、ノードバージョンとして1.28.15-gke.3280000、1.29.15-gke.2613000、1.30.14-gke.1855000も利用可能です。これらのバージョンは現在ロールアウト中であり、全てのGoogle Cloudゾーンで利用可能になるまでに数日かかる場合があります。
影響有無: **影響なし**
理由: これらのバージョンはパッチバージョンであり、通常は安定性向上やバグ修正が目的です。既存の運用中のGKEクラスタが自動アップグレードの対象となる可能性はありますが、重大な非互換性リスクは低いと判断されます。
対処方法: 現在運用中のGKEクラスタがこれらのバージョンに該当する場合、特に必要な対応はありませんが、自動アップグレードが適用されることを認識しておいてください。手動アップグレードを計画している場合は、これらの最新パッチバージョンを検討できます。

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

説明: Rapidチャネルで、Kubernetes 1.35.0-gke.1272000を含む複数の新しいバージョンが利用可能になりました。このチャネルのクラスタは、記載されたマイナーバージョンに基づいて新しい自動アップグレードターゲットを持つことになります。GKEは、マイナーバージョンアップグレードが利用できない場合や、メンテナンス除外期間などの要因がある場合に、クラスターを新しいパッチバージョン（例: 1.35から1.35.0-gke.1272000）にアップグレードできます。これらのバージョンは現在ロールアウト中であり、全てのGoogle Cloudゾーンで利用可能になるまでに数日かかる場合があります。
影響有無: **影響あり（Rapidチャネル利用者のみ）**
理由: Rapidチャネルを利用している場合、Kubernetes 1.35への自動アップグレードの可能性が高まります。前述の「Deprecated」セクションで説明した通り、Kubernetes 1.35ではcgroup v1のサポートが削除されるため、これを使用しているクラスタはアップグレードがブロックされるか、互換性の問題が発生する可能性があります。
対処方法:
1.  現在運用中のGKEクラスタが**Rapidチャネル**を利用しているか確認してください。
2.  Rapidチャネルを利用している場合、Kubernetes 1.35へのアップグレードが予定されるため、アプリケーションの互換性テストを事前に実施
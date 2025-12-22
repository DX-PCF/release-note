
# Title: December 18, 2025 
Link: https://docs.cloud.google.com/release-notes#December_18_2025<br>
## Google Kubernetes Engine
### Change
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

説明: 新しいGKEクラスタ、および既存クラスタの手動コントロールプレーン・ノードアップグレード用に、新しいGKEクラスタバージョンが利用可能になりました。これにより、最新の機能、セキュリティ修正、パフォーマンス改善が利用できるようになります。

影響有無:
- **間接的に影響あり。** 現在運用中のGoogle Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) はGKE上に構築されており、GKEのバージョンアップはComposer環境の基盤に影響します。
- 既存のGKEクラスタが自動アップグレードチャネルに登録されている場合、これらの新しいバージョンに自動的にアップグレードされる可能性があります。ComposerがサポートするGKEのバージョン範囲内であれば、セキュリティと機能の向上が期待できます。

対処方法:
- 既存のGKEクラスタがどのアップグレードチャネルに登録されているかを確認し、自動アップグレードポリシーを把握してください。
- Composer 2.7.1がサポートするGKEバージョンと、現在利用中のGKEバージョンを照合し、今回のリリースに含まれる新しいバージョンへのアップグレードがComposerの安定性に影響を与えないか、Composerの公式ドキュメントで互換性を確認してください。
- 必要に応じて、ステージング環境でアップグレード後の動作検証を実施することを推奨します。

用語説明:
- **GKEクラスタバージョン (GKE cluster version)**: Google Kubernetes Engineで使用されるKubernetesのバージョンと、Google Cloud固有の拡張機能のバージョンを組み合わせたものです。コントロールプレーンとノードプールの両方に適用されます。
- **コントロールプレーン (Control Plane)**: Kubernetesクラスタの脳となる部分で、APIサーバー、スケジューラー、コントローラーマネージャーなどが含まれます。
- **ノード (Node)**: コンテナ化されたワークロードを実行する仮想マシンまたは物理マシンです。
- **アップグレードチャネル (Upgrade Channel)**: GKEクラスタの自動アップグレードの頻度と安定性を選択するための設定です。Rapid、Regular、Stable、Extendedなどがあります。

### Security
原文: This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

GKE version
Container-Optimized OS version
Details
1.34.1-gke.3759000
cos-125-19216-104-45
cos-125-19216-104-45 release notes

[cos-125-19216-104-45 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-104-45_)

説明: 新しいGKEバージョンには、更新されたContainer-Optimized OS (COS) イメージが使用されています。これらのイメージには、前回のGKEリリース以降に公開されたCOSのセキュリティ修正がすべて含まれています。これにより、GKEクラスタのノードのセキュリティが強化されます。

影響有無:
- **ポジティブな影響あり。** セキュリティ脆弱性の修正が含まれるため、クラスタのセキュリティ体制が向上します。
- GKEバージョン 1.34.1-gke.3759000 を使用するクラスタ（または今後そのバージョンにアップグレードされるクラスタ）のノードに、自動的に最新のセキュリティパッチが適用されます。Composerの基盤GKEも同様です。

対処方法:
- 特段の対処は不要です。GKEクラスタが自動アップグレードチャネルに登録されている場合、適切なタイミングでセキュリティ修正が適用されたノードイメージが利用されるようになります。
- 手動アップグレードを計画している場合は、これらのセキュリティ修正が含まれる最新のGKEバージョンへのアップグレードを推奨します。

用語説明:
- **Container-Optimized OS (COS)**: Googleが提供する、コンテナの実行に最適化されたオペレーティングシステムです。セキュリティと信頼性を重視しており、GKEクラスタのノードイメージとして広く利用されます。

### Change
原文: GKE Standard clusters enrolled in the Regular channel now
support Autopilot features. Autopilot features include the container-optimized
compute platform and fully managed nodes, letting you use Autopilot's
advantages without migrating to a dedicated Autopilot cluster.

To use Autopilot features in Standard clusters, use either of the
following configurations:

- Enroll a cluster in the Regular channel with GKE version 1.34.1-gke.1829001
or later.
- Enroll a cluster in the Rapid channel with GKE version 1.33.1-gke.1107000
or later.

For more information, see
Run workloads in Autopilot mode in Standard clusters.

[Run workloads in Autopilot mode in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters)

説明: Regularチャネルに登録されたGKE Standardクラスタで、Autopilotの機能がサポートされるようになりました。これにより、StandardクラスタをAutopilotクラスタに移行することなく、Autopilotのメリット（コンテナ最適化されたコンピューティングプラットフォームやフルマネージドノード）を利用できるようになります。この機能を利用するには、RegularチャネルでGKEバージョン1.34.1-gke.1829001以降、またはRapidチャネルでGKEバージョン1.33.1-gke.1107000以降を使用する必要があります。

影響有無:
- **直接的な影響なし、将来的な選択肢の増加。** 既存のGKE Standardクラスタが自動的にAutopilotモードに切り替わるわけではありません。
- Composer 2はGKE Standardクラスタを基盤としているため、将来的にAutopilotの利点をComposer環境に適用できる可能性を示唆しています。ただし、ComposerがこのAutopilot機能を直接サポートするかは、今後のComposer側のリリースを確認する必要があります。

対処方法:
- 現時点では特段の対処は不要です。
- 将来的にGKE StandardクラスタでAutopilot機能の利用を検討する場合、そのメリット（運用負担軽減、コスト最適化など）と、既存のワークロードへの適合性を評価してください。

用語説明:
- **GKE Standardクラスタ (GKE Standard cluster)**: ユーザーがノードの管理、スケーリング、アップグレードなどを詳細に制御できるGKEクラスタの種類です。
- **GKE Autopilotクラスタ (GKE Autopilot cluster)**: ノードの管理やスケーリング、アップグレードなどが完全にGoogleによって自動化されるGKEクラスタの種類です。ワークロードを定義するだけで、Googleが最適な基盤を管理します。
- **フルマネージドノード (Fully managed nodes)**: GKE Autopilotの主要な特徴の一つで、ノードのプロビジョニング、構成、アップグレード、スケーリング、パッチ適用などがGoogleによって自動的に行われ、ユーザーの運用負担が大幅に軽減されます。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Extended channel:

- 1.28.15-gke.3251000
- 1.29.15-gke.2585000
- 1.30.14-gke.1820000

[1.28.15-gke.3251000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2585000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)

説明: GKEのExtendedチャネルにおいて、1.28.15-gke.3251000、1.29.15-gke.2585000、1.30.14-gke.1820000の各バージョンが利用可能になりました。これらのバージョンは、特定の地域やゾーンに展開が完了するまでに時間を要する場合があります。

影響有無:
- **間接的に影響あり。** Google Cloud Composer 2.7.1は通常、GKEのRegularまたはStableチャネルをサポートすることが多いですが、もしExtendedチャネルを利用しているGKEクラスタでComposerが稼働している場合、これらのバージョンが自動アップグレードの対象となる可能性があります。
- これらのバージョンは長期サポート対象であり、安定性と既存のKubernetesバージョンに対するパッチリリースが含まれています。

対処方法:
- 現在稼働中のComposer環境が利用しているGKEのバージョンとアップグレードチャネルを確認してください。
- もしExtendedチャネルを利用しており、自動アップグレードが有効な場合は、アップグレードが既存のComposerワークロードに影響を与えないか、事前にテスト環境で検証することをお勧めします。

用語説明:
- **Extendedチャネル (Extended channel)**: GKEのアップグレードチャネルの一つで、長期にわたるサポートと安定性を提供するバージョンが利用可能です。通常、最新機能の導入よりも安定性と後方互換性が重視されます。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available:

- 1.31.14-gke.1114000
- 1.32.9-gke.1675000
- 1.33.5-gke.2019000
- 1.34.0-gke.2201000
- 1.34.1-gke.2541000
- 1.34.1-gke.3759000

- The following node versions are now available:

- 1.28.15-gke.3251000
- 1.29.15-gke.2585000
- 1.30.14-gke.1820000
- 1.31.14-gke.1114000
- 1.32.9-gke.1675000
- 1.33.5-gke.2019000
- 1.34.0-gke.2201000
- 1.34.1-gke.3759000

[1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
[1.34.1-gke.2541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.34.1-gke.3759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
- 1.28.15-gke.3251000
- 1.29.15-gke.2585000
- 1.30.14-gke.1820000
- 1.31.14-gke.1114000
- 1.32.9-gke.1675000
- 1.33.5-gke.2019000
- 1.34.0-gke.2201000
- 1.34.1-gke.3759000

[1.28.15-gke.3251000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2585000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.9)
[1.33.5-gke.2019000](https://github.google.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
[1.34.1-gke.3759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

説明: 様々なGKEバージョン（コントロールプレーンおよびノード）が新たに利用可能になりました。これらのバージョンは、地域やゾーンによって利用可能になるまでに時間がかかる場合があります。

影響有無:
- **間接的に影響あり。** GKEクラスタが自動アップグレードチャネル（特にRegularやRapidチャネル）に登録されている場合、これらの新しいバージョンにアップグレードされる可能性があります。
- Composer 2.7.1がサポートするGKEバージョンによっては、自動アップグレードの対象となり、パフォーマンス向上やバグ修正の恩恵を受ける可能性があります。一方で、Kubernetesのメジャーバージョンアップ（例: 1.30.xから1.31.xなど）は、APIの変更を含む場合があるため、互換性の確認が重要です。

対処方法:
- 現在運用中のComposer環境のGKEバージョンとアップグレードチャネルを確認してください。
- GKEのバージョンアップは、通常、後方互換性を保ちますが、Kubernetesのメジャーバージョンアップを含む場合、非推奨となったAPIや機能の利用がないか、ワークロードを確認することを推奨します。
- GKEの自動アップグレード前に、テスト環境でComposerワークロードの動作検証を実施してください。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Rapid channel:

- 1.31.14-gke.1114000
- 1.32.9-gke.1675000
- 1.33.5-gke.2019000
- 1.34.0-gke.2201000
- 1.34.1-gke.2541000
- 1.34.1-gke.3759000

[1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
[1.34.1-gke.2541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.34.1-gke.3759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

説明: Rapidチャネルにおいて、1.31.14-gke.1114000から1.34.1-gke.3759000までのGKEバージョンが利用可能になりました。これらのバージョンも、地域やゾーンによって利用可能になるまでに時間がかかる場合があります。

影響有無:
- **間接的に影響あり。** Rapidチャネルは最も早く最新のGKEバージョンが提供されるチャネルです。もしComposer 2.7.1環境がRapidチャネルのGKEクラスタで運用されている場合、これらのバージョンへの自動アップグレードの対象となる可能性があります。
- Rapidチャネルは最新機能が提供される一方で、比較的安定性テスト期間が短いため、既存ワークロードへの影響をより慎重に評価する必要があります。

対処方法:
- 現在運用中のComposer環境のGKEバージョンとアップグレードチャネルを確認してください。
- Rapidチャネルを利用している場合、GKEのバージョンアップが頻繁に発生し、APIの変更を含む可能性があるため、Composerワークロードへの影響を最小限に抑えるために、厳格なテストプロセス（ステージング環境での検証）を確立することが非常に重要です。
- Composer 2.7.1がサポートするGKEバージョンの範囲を逸脱しないよう注意してください。

用語説明:
- **Rapidチャネル (Rapid channel)**: GKEのアップグレードチャネルの一つで、最新のGKEバージョンと機能が最も早く提供されます。新機能をいち早く利用したい場合や、開発環境などに適しています。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

There are no new releases in the Regular channel.

説明: Regularチャネルにおいて、今回のリリースノートでは新しいGKEバージョンはリリースされていません。このため、Regularチャネルに登録されているクラスタには、このリリースノートにおけるGKEバージョンに関する直接的な更新は適用されません。

影響有無:
- **影響なし。** 現在運用中のGKEクラスタがRegularチャネルに登録されている場合、今回のリリースノートに含まれる新しいGKEバージョンへの自動アップグレードは発生しません。

対処方法:
- 特段の対処は不要です。

用語説明:
- **Regularチャネル (Regular channel)**: GKEのアップグレードチャネルの一つで、最新機能と安定性のバランスが良いチャネルです。多くのプロダクション環境で使用されることが推奨されます。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

説明: Stableチャネルにおいて、今回のリリースノートでは新しいGKEバージョンはリリースされていません。このため、Stableチャネルに登録されているクラスタには、このリリースノートにおけるGKEバージョンに関する直接的な更新は適用されません。

影響有無:
- **影響なし。** 現在運用中のGKEクラスタがStableチャネルに登録されている場合、今回のリリースノートに含まれる新しいGKEバージョンへの自動アップグレードは発生しません。

対処方法:
- 特段の対処は不要です。

用語説明:
- **Stableチャネル (Stable channel)**: GKEのアップグレードチャネルの一つで、最も安定性が高く、長期間にわたる運用が求められるプロダクション環境に適しています。新機能の導入は他のチャネルよりも遅くなります。
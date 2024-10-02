package net.jotred.playershops_tfc.common.blocks;

import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.common.blocks.wood.Wood;
import net.jotred.playershops_tfc.common.items.PlayershopsTFCItems;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.MapColor;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import net.dries007.tfc.util.registry.RegistrationHelpers;
import org.jetbrains.annotations.Nullable;

import java.util.Map;
import java.util.function.Function;
import java.util.function.Supplier;

public class PlayershopsTFCBlocks {
	
	public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, "playershops_tfc");
	
	public static final Map<Wood, RegistryObject<Block>> TFC_WOOD_PLAYER_SHOP_BLOCKS =
			Helpers.mapOfKeys(Wood.class, woodTypes ->
					register("wood/player_shops/"+woodTypes.name(),
							() -> new PlayerShopTFCBlock(BlockBehaviour.Properties
							.copy(Blocks.BARRIER)
							.sound(SoundType.WOOD)
							.mapColor(MapColor.WOOD)
							.strength(-1.0F,
									3600000.8F).noOcclusion())));
	
	
	private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> blockSupplier)
	{
		return register(name, blockSupplier, block -> new BlockItem(block, new Item.Properties()));
	}
	
	private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> blockSupplier,
	                                                            @Nullable Function<T, ? extends BlockItem> blockItemFactory)
	{
		return RegistrationHelpers.registerBlock(PlayershopsTFCBlocks.BLOCKS, PlayershopsTFCItems.ITEMS, name, blockSupplier, blockItemFactory);
	}
}